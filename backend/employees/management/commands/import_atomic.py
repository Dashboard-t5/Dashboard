import pandas as pd
import os

from django.core.management.base import BaseCommand
from django.db import transaction

from dashboard_backend.settings import BASE_DIR
from config import FILE_DIRECTORY, FILE_NAME
from employees.models import Employee, Position, Team
from ratings.models import Competence, Domain, Rating, Skill


class Command(BaseCommand):

    def handle(self, *args, **options):
        file_path = os.path.join(BASE_DIR, FILE_DIRECTORY, FILE_NAME)

        # Проверка существования файла
        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"Файл не найден: {file_path}"))
            return

        # Проверка, что файл читается как Excel
        try:
            df = pd.read_excel(file_path, engine="openpyxl")
        except Exception as e:
            self.stdout.write(self.style.ERROR(
                f"Ошибка при чтении файла: {e}")
            )
            return

        self.stdout.write(self.style.SUCCESS(
            f"Файл успешно прочитан: {file_path}")
        )

        # Списки для массовой вставки
        positions = {}
        teams = {}
        domains = {}
        competences = {}
        skills = {}
        employees = {}
        ratings = []

        # Начало транзакции для массовой вставки
        with transaction.atomic():
            for index, row in df.iterrows():
                last_name, first_name = row['сотрудник'].split()

                # Массовое создание уникальных объектов для каждой модели
                if row['должность'] not in positions:
                    position, created = Position.objects.get_or_create(
                        name=row['должность']
                    )
                    positions[row['должность']] = position

                if row['команда'] not in teams:
                    team, created = Team.objects.get_or_create(
                        name=row['команда']
                    )
                    teams[row['команда']] = team

                if row['домен'] not in domains:
                    domain, created = Domain.objects.get_or_create(
                        name=row['домен']
                    )
                    domains[row['домен']] = domain

                competence_key = (row['компетенция'], row['домен'])
                if competence_key not in competences:
                    competence, created = Competence.objects.get_or_create(
                        name=row['компетенция'],
                        domain=domains[row['домен']]
                    )
                    competences[competence_key] = competence

                if row['навык'] not in skills:
                    skill, created = Skill.objects.get_or_create(
                        name=row['навык'],
                        competence=competences[competence_key]
                    )
                    skills[row['навык']] = skill

                employee_key = (
                    first_name,
                    last_name,
                    row['грейд'],
                    row['должность'],
                    row['команда']
                )
                if employee_key not in employees:
                    employee, created = Employee.objects.get_or_create(
                        first_name=first_name,
                        last_name=last_name,
                        position=positions[row['должность']],
                        team=teams[row['команда']],
                        grade=row['грейд'],
                    )
                    employees[employee_key] = employee

                # Добавляем рейтинг в список для bulk_create
                ratings.append(
                    Rating(
                        employee=employees[employee_key],
                        skill=skills[row['навык']],
                        rating_date=row['дата'],
                        rating_value=row['оценка_'],
                        suitability=row['соответствие'],
                    )
                )

                self.stdout.write(self.style.SUCCESS(
                    f'Employee {employees[employee_key]} processed')
                )

            # Массовая вставка для рейтингов
            Rating.objects.bulk_create(ratings, batch_size=999)
