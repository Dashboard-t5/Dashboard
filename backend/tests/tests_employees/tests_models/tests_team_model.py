#        План тестирования Модель Team
# 1) Проверка существования полей модели
# 2) Проверка типов полей модели
# 3) Проверка, что обязательные поля не могут быть пустыми
# 4) Проверка, что текстовые поля не могут быть blank.
# 5) Проверка, валидации поля name
# 6) Проверка уникальности поля name
# 7) Проверка успешного создания объекта
# 8) Проверка успешного удаления объекта
# 9) Тестирование класса Meta
# 10) Тесты строкового представления (__str__)

from model_bakery import baker

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models import (
    BigAutoField,
    CharField,
)
from django.test import TestCase

from config import NAME_MAX_LENGTH
from employees.models import Team

User = get_user_model()


class TestTeamModel(TestCase):
    """
    Тесты для модели должности Team.
    """

    REQUIRED_FIELDS = ("name", )
    NOT_BLANK_FIELDS = ("name", )
    validation_data = [
        ("name", "", False),  #Проверка на blank=False.
        ("name", "a" * NAME_MAX_LENGTH, True),
        ("name", "a" * (NAME_MAX_LENGTH + 1), False),
    ]

    @classmethod
    def setUpTestData(cls):
        cls.team = baker.make(
            "employees.Team",
            name="Название команды №1"
        )

    def test_team_fields_existence(self):
        """Проверка существования полей модели."""
        fields = Team._meta.fields
        fields_names = (field.name for field in fields)
        self.assertIn("id", fields_names)
        self.assertIn("name", fields_names)

    def test_team_fields_types(self):
        """
        Проверка типов полей модели.
        """
        self.assertIsInstance(
            Team._meta.get_field("id"),
            BigAutoField
        )
        self.assertIsInstance(
            Team._meta.get_field("name"),
            CharField
        )


    def test_required_fields_cannot_be_null(self):
        """
        Проверка, что обязательные поля не могут быть пустыми.
        """
        for field in self.REQUIRED_FIELDS:
            with transaction.atomic():
                setattr(self.team, field, None)
                with self.assertRaises(IntegrityError):
                    self.team.save()

    def test_fields_validation(self):
        """Проверка валидации полей."""
        for field, value, is_valid in self.validation_data:
            team = baker.prepare(
                "employees.Team",
                **{field: value},
            )
            if is_valid:
                try:

                    team.full_clean()
                    team.save()
                    team.refresh_from_db()
                    self.assertEqual(
                        getattr(team, field),
                        value,
                        f"Не удалось записать значение "
                        f"'{value}' в поле {field}"
                    )
                except ValidationError:
                    self.fail(
                        f"Валидация провалена для значения: "
                        f"{value} в поле: {field}"
                    )
            else:
                with self.assertRaises(ValidationError):
                    team.full_clean()

    def test_unique_name(self):
        """Проверка уникальности."""
        team_2 = baker.prepare(
            "employees.Team",
            name=self.team.name,
        )
        with self.assertRaises(ValidationError):
            team_2.full_clean()

        with self.assertRaises(IntegrityError):
            team_2.save()

    # Проверки функциональности
    def test_team_successful_creation(self):
        """Проверка успешного создания объекта."""
        self.assertEqual(
            Team.objects.count(),
            1,
            "Ошибка при создании объекта.",
        )

    def test_team_successful_deletion(self):
        """Проверка успешного удаления объекта."""
        self.assertEqual(
            Team.objects.count(),
            1,
        )
        self.team.delete()
        self.assertEqual(
            Team.objects.count(),
            0,
            "Ошибка при удалении объекта.",
        )

    # Проверки класса Meta
    def test_ordering(self):
        """Проверка сортировки."""
        self.team.delete()
        self.assertEqual(Team.objects.count(), 0,)

        team_names = (
            "Медиа",
            "Эквайринг",
            "Приложение",
            "Юл"
        )
        names_number = len(team_names)

        baker.make(
            "employees.Team",
            name=(name for name in team_names),
            _quantity=names_number,
        )
        expected_teams = list(Team.objects.all())
        expected_teams.sort(key=lambda x: x.name)

        self.assertEqual(
            expected_teams,
            list(Team.objects.all()),
            "Команды должны быть отсортированы по алфавиту"
        )

    # Тесты строкового представления (__str__):
    def test_str(self):
        self.assertEqual(
            str(self.team),
            "Название команды №1",
        )
