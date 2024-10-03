import pandas as pd
import os

from django.core.management.base import BaseCommand

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
            self.stdout.write(self.style.ERROR(f"Ошибка при чтении файла: {e}"))
            return

        # Если все прошло успешно, выводим данные
        self.stdout.write(self.style.SUCCESS(f"Файл успешно прочитан: {file_path}"))

        for index, row in df.iterrows():
            first_name, last_name = row['сотрудник'].split()

            position, created = Position.objects.get_or_create(name=row['должность'])
            team, created = Team.objects.get_or_create(name=row['команда'])
            domain, created = Domain.objects.get_or_create(name=row['домен'])
            competence, created = Competence.objects.get_or_create(name=row['компетенция'], domain=domain)
            skill, created = Skill.objects.get_or_create(name=row['навык'], competence=competence)
            employee, created = Employee.objects.update_or_create(
                first_name=first_name,
                last_name=last_name,
                defaults={
                    'position': position,
                    'team': team
                }
            )
            rating, created = Rating.objects.get_or_create(
                employee=employee,
                skill=skill,
                rating_date=row['дата'],
                rating_value=row['оценка_'],
            )

            self.stdout.write(self.style.SUCCESS(f'Employee {employee} processed'))
