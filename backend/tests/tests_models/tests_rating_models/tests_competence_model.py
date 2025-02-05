#        План тестирования Модель Competence
# 1) Проверка существования полей модели
# 2) Проверка типов полей модели
# 3) Проверка, что обязательные поля не могут быть пустыми
# 4) Проверка, что текстовые поля не могут быть blank.
# 5) Проверка валидации поля name
# 6) Проверка уникальности поля name
# 7) Проверка успешного создания объекта
# 8) Проверка успешного удаления объекта
# 9) Проверка, что при удалении Домена удаляются связанные
#       компетенции 	(on_delete=models.CASCADE).
# 10) Проверка related_name связанных полей
# 11) Тестирование класса Meta
# 12) Тесты строкового представления (__str__)

from model_bakery import baker

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models import (
    BigAutoField,
    CharField,
    ForeignKey,
)
from django.test import TestCase

from ratings.constants import COMPETENCE_NAME_MAX_LENGTH
from ratings.models import Competence, Domain

User = get_user_model()


class TestCompetenceModel(TestCase):
    """
    Тесты для модели компетенций Competence.
    """

    REQUIRED_FIELDS = ("name", "domain", )
    NOT_BLANK_FIELDS = ("name", "domain", )
    validation_data = [
        ("name", "", False),  #Проверка на blank=False.
        ("name", "a" * COMPETENCE_NAME_MAX_LENGTH, True),
        ("name", "a" * (COMPETENCE_NAME_MAX_LENGTH + 1), False),
    ]

    @classmethod
    def setUpTestData(cls):
        cls.competence = baker.make(
            "ratings.Competence",
            name="Название компетенции №1"
        )

    def test_team_fields_existence(self):
        """Проверка существования полей модели."""
        fields = Competence._meta.fields
        fields_names = (field.name for field in fields)
        self.assertIn("id", fields_names)
        self.assertIn("name", fields_names)
        self.assertIn("domain", fields_names)

    def test_team_fields_types(self):
        """
        Проверка типов полей модели.
        """
        self.assertIsInstance(
            Competence._meta.get_field("id"),
            BigAutoField
        )
        self.assertIsInstance(
            Competence._meta.get_field("name"),
            CharField
        )
        self.assertIsInstance(
            Competence._meta.get_field("domain"),
            ForeignKey
        )

    def test_required_fields_cannot_be_null(self):
        """
        Проверка, что обязательные поля не могут быть пустыми.
        """
        for field in self.REQUIRED_FIELDS:
            with transaction.atomic():
                setattr(self.competence, field, None)
                with self.assertRaises(IntegrityError):
                    self.competence.save()

    def test_fields_validation(self):
        """Проверка валидации полей."""
        for field, value, is_valid in self.validation_data:
            competence = baker.prepare(
                "ratings.Competence",
                domain=baker.make("ratings.Domain"),
                **{field: value},
            )
            if is_valid:
                try:
                    competence.full_clean()
                    competence.save()
                    competence.refresh_from_db()
                    self.assertEqual(
                        getattr(competence, field),
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
                    competence.full_clean()

    def test_unique_name(self):
        """Проверка уникальности."""
        competence_2 = baker.prepare(
            "ratings.Competence",
            domain=baker.make("ratings.Domain"),
            name=self.competence.name,
        )
        with self.assertRaises(ValidationError):
            competence_2.full_clean()

        with self.assertRaises(IntegrityError):
            competence_2.save()

    # Проверки функциональности
    def test_competence_successful_creation(self):
        """Проверка успешного создания объекта."""
        self.assertEqual(
            Competence.objects.count(),
            1,
            "Ошибка при создании объекта.",
        )

    def test_competence_successful_deletion(self):
        """Проверка успешного удаления объекта."""
        self.assertEqual(
            Competence.objects.count(),
            1,
        )
        self.competence.delete()
        self.assertEqual(
            Competence.objects.count(),
            0,
            "Ошибка при удалении объекта.",
        )

    # Проверки связанных полей
    def test_domain_on_delete_cascade(self):
        """
        Проверка, что при удалении Домена удаляются
        связанные компетенции (on_delete=models.CASCADE).
        """
        self.assertEqual(Competence.objects.count(), 1,)
        self.competence.domain.delete()
        self.assertEqual(Competence.objects.count(), 0,)

    # Проверки класса Meta
    def test_domain_related_name(self):
        """Проверка related_name для поля domain."""
        domain = self.competence.domain
        self.assertQuerySetEqual(
            domain.competencies.all(),
            Competence.objects.filter(domain=domain),
            transform=lambda x: x,
            msg="'related_name' должно быть 'competencies'."
        )

    def test_ordering(self):
        """Проверка сортировки."""
        self.competence.delete()
        self.assertEqual(Competence.objects.count(), 0,)

        competences_names = (
            "Работа в команде",
            "Лидерские качества",
            "Тайм-менеджмент",
            "Знание языков программирования"
        )
        names_number = len(competences_names)

        baker.make(
            "ratings.Competence",
            domain=baker.make("ratings.Domain"),
            name=(name for name in competences_names),
            _quantity=names_number,
        )
        expected_competences = list(Competence.objects.all())
        expected_competences.sort(key=lambda x: x.name)

        self.assertEqual(
            expected_competences,
            list(Competence.objects.all()),
            "Компетенции должны быть отсортированы по названию"
        )

    # Тесты строкового представления (__str__):
    def test_str(self):
        self.assertEqual(
            str(self.competence),
            "Название компетенции №1",
        )
