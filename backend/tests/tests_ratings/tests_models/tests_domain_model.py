#        План тестирования Модель Domain
# 1) Проверка существования полей модели
# 2) Проверка типов полей модели
# 3) Проверка, что обязательные поля не могут быть пустыми
# 4) Проверка, что текстовые поля не могут быть blank.
# 5) Проверка валидации поля name
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

from ratings.constants import DOMAIN_NAME_MAX_LENGTH
from ratings.models import Domain

User = get_user_model()


class TestDomainModel(TestCase):
    """
    Тесты для модели домен Domain.
    """

    REQUIRED_FIELDS = ("name", )
    NOT_BLANK_FIELDS = ("name", )
    validation_data = [
        ("name", "", False),  #Проверка на blank=False.
        ("name", "a" * DOMAIN_NAME_MAX_LENGTH, True),
        ("name", "a" * (DOMAIN_NAME_MAX_LENGTH + 1), False),
    ]

    @classmethod
    def setUpTestData(cls):
        cls.domain = baker.make(
            "ratings.Domain",
            name="Hard Skills"
        )

    def test_team_fields_existence(self):
        """Проверка существования полей модели."""
        fields = Domain._meta.fields
        fields_names = (field.name for field in fields)
        self.assertIn("id", fields_names)
        self.assertIn("name", fields_names)

    def test_team_fields_types(self):
        """
        Проверка типов полей модели.
        """
        self.assertIsInstance(
            Domain._meta.get_field("id"),
            BigAutoField
        )
        self.assertIsInstance(
            Domain._meta.get_field("name"),
            CharField
        )


    def test_required_fields_cannot_be_null(self):
        """
        Проверка, что обязательные поля не могут быть пустыми.
        """
        for field in self.REQUIRED_FIELDS:
            with transaction.atomic():
                setattr(self.domain, field, None)
                with self.assertRaises(IntegrityError):
                    self.domain.save()

    def test_fields_validation(self):
        """Проверка валидации полей."""
        for field, value, is_valid in self.validation_data:
            domain = baker.prepare(
                "ratings.Domain",
                **{field: value},
            )
            if is_valid:
                try:

                    domain.full_clean()
                    domain.save()
                    domain.refresh_from_db()
                    self.assertEqual(
                        getattr(domain, field),
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
                    domain.full_clean()

    def test_unique_name(self):
        """Проверка уникальности."""
        domain_2 = baker.prepare(
            "ratings.Domain",
            name=self.domain.name,
        )
        with self.assertRaises(ValidationError):
            domain_2.full_clean()

        with self.assertRaises(IntegrityError):
            domain_2.save()

    # Проверки функциональности
    def test_team_successful_creation(self):
        """Проверка успешного создания объекта."""
        self.assertEqual(
            Domain.objects.count(),
            1,
            "Ошибка при создании объекта.",
        )

    def test_team_successful_deletion(self):
        """Проверка успешного удаления объекта."""
        self.assertEqual(
            Domain.objects.count(),
            1,
        )
        self.domain.delete()
        self.assertEqual(
            Domain.objects.count(),
            0,
            "Ошибка при удалении объекта.",
        )

    # Проверки класса Meta
    def test_ordering(self):
        """Проверка сортировки."""
        self.domain.delete()
        self.assertEqual(Domain.objects.count(), 0,)

        domains_names = (
            "Hard Skills",
            "Soft Skills",
            "Super Slim Skills",
            "Base Skills"
        )
        names_number = len(domains_names)

        baker.make(
            "ratings.Domain",
            name=(name for name in domains_names),
            _quantity=names_number,
        )
        expected_domains = list(Domain.objects.all())
        expected_domains.sort(key=lambda x: x.name)

        self.assertEqual(
            expected_domains,
            list(Domain.objects.all()),
            "Домены должны быть отсортированы по названию"
        )

    # Тесты строкового представления (__str__):
    def test_str(self):
        self.assertEqual(
            str(self.domain),
            "Hard Skills",
        )
