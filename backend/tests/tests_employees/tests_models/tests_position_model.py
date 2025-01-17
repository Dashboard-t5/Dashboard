#        План тестирования Модель Position
# 1) Проверка существования полей модели
# 2) Проверка типов полей модели
# 3) Проверка, что обязательные поля не могут быть пустыми
# 4) Проверка, что текстовые поля не могут быть blank.
# 5) Проверка, валидации поля name
# 6) Проверка успешного создания объекта
# 7) Проверка успешного удаления объекта
# 8) Тестирование класса Meta
# 9) Тесты строкового представления (__str__)

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
from employees.models import Position

User = get_user_model()


class TestPositionModel(TestCase):
    """
    Тесты для модели должности Position.
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
        cls.position = baker.make(
            "employees.Position",
            name="Название должности №1"
        )

    def test_position_fields_existence(self):
        """Проверка существования полей модели."""
        fields = Position._meta.fields
        fields_names = (field.name for field in fields)
        self.assertIn("id", fields_names)
        self.assertIn("name", fields_names)

    def test_position_fields_types(self):
        """
        Проверка типов полей модели.
        """
        self.assertIsInstance(
            Position._meta.get_field("id"),
            BigAutoField
        )
        self.assertIsInstance(
            Position._meta.get_field("name"),
            CharField
        )

    def test_required_fields_cannot_be_null(self):
        """
        Проверка, что обязательные поля не могут быть пустыми.
        """
        for field in self.REQUIRED_FIELDS:
            with transaction.atomic():
                setattr(self.position, field, None)
                with self.assertRaises(IntegrityError):
                    self.position.save()

    def test_fields_validation(self):
        """Проверка валидации полей."""
        for field, value, is_valid in self.validation_data:
            position = baker.prepare(
                "employees.Position",
                **{field: value},
            )
            if is_valid:
                try:

                    position.full_clean()
                    position.save()
                    position.refresh_from_db()
                    self.assertEqual(
                        getattr(position, field),
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
                    position.full_clean()

    # Проверки функциональности
    def test_position_successful_creation(self):
        """Проверка успешного создания объекта."""
        self.assertEqual(
            Position.objects.count(),
            1,
            "Ошибка при создании объекта.",
        )

    def test_position_successful_deletion(self):
        """Проверка успешного удаления объекта."""
        self.assertEqual(
            Position.objects.count(),
            1,
        )
        self.position.delete()
        self.assertEqual(
            Position.objects.count(),
            0,
            "Ошибка при удалении объекта.",
        )

    # Проверки класса Meta
    def test_ordering(self):
        """Проверка сортировки."""
        self.position.delete()
        self.assertEqual(Position.objects.count(), 0,)

        position_names = (
            "Системный Аналитик",
            "Бизнес Аналитик",
            "Разработчик",
            "Тестировщик"
        )
        names_number = len(position_names)

        baker.make(
            "employees.Position",
            name=(name for name in position_names),
            _quantity=names_number,
        )
        expected_positions = list(Position.objects.all())
        expected_positions.sort(key=lambda x: x.name)

        self.assertEqual(
            expected_positions,
            list(Position.objects.all()),
            "Должности должны быть отсортированы по алфавиту"
        )

    # Тесты строкового представления (__str__):
    def test_str(self):
        self.assertEqual(
            str(self.position),
            "Название должности №1",
        )
