#        План тестирования Модель Skill
# 1) Проверка существования полей модели
# 2) Проверка типов полей модели
# 3) Проверка, что обязательные поля не могут быть пустыми
# 4) Проверка, что текстовые поля не могут быть blank.
# 5) Проверка валидации поля name
# 6) Проверка уникальности поля name
# 7) Проверка успешного создания объекта
# 8) Проверка успешного удаления объекта
# 9) Проверка, что при удалении Компетенции удаляются связанные
#       навыки 	(on_delete=models.CASCADE).
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

from ratings.constants import COMPETENCE_NAME_MAX_LENGTH, SKILL_NAME_MAX_LENGTH
from ratings.models import Competence, Domain, Skill

User = get_user_model()


class TestSkillModel(TestCase):
    """
    Тесты для модели Навыка Skill.
    """

    REQUIRED_FIELDS = ("name", "competence", )
    NOT_BLANK_FIELDS = ("name", "competence", )
    validation_data = [
        ("name", "", False),  #Проверка на blank=False.
        ("name", "a" * SKILL_NAME_MAX_LENGTH, True),
        ("name", "a" * (SKILL_NAME_MAX_LENGTH + 1), False),
    ]

    @classmethod
    def setUpTestData(cls):
        cls.skill = baker.make(
            "ratings.SKILL",
            name="Название навыка №1"
        )

    def test_team_fields_existence(self):
        """Проверка существования полей модели."""
        fields = Skill._meta.fields
        fields_names = (field.name for field in fields)
        self.assertIn("id", fields_names)
        self.assertIn("name", fields_names)
        self.assertIn("competence", fields_names)

    def test_team_fields_types(self):
        """
        Проверка типов полей модели.
        """
        self.assertIsInstance(
            Skill._meta.get_field("id"),
            BigAutoField
        )
        self.assertIsInstance(
            Skill._meta.get_field("name"),
            CharField
        )
        self.assertIsInstance(
            Skill._meta.get_field("competence"),
            ForeignKey
        )

    def test_required_fields_cannot_be_null(self):
        """
        Проверка, что обязательные поля не могут быть пустыми.
        """
        for field in self.REQUIRED_FIELDS:
            with transaction.atomic():
                setattr(self.skill, field, None)
                with self.assertRaises(IntegrityError):
                    self.skill.save()

    def test_fields_validation(self):
        """Проверка валидации полей."""
        for field, value, is_valid in self.validation_data:
            skill = baker.prepare(
                "ratings.Skill",
                competence=baker.make("ratings.Competence"),
                **{field: value},
            )
            if is_valid:
                try:
                    skill.full_clean()
                    skill.save()
                    skill.refresh_from_db()
                    self.assertEqual(
                        getattr(skill, field),
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
                    skill.full_clean()

    def test_unique_name(self):
        """Проверка уникальности."""
        skill_2 = baker.prepare(
            "ratings.Skill",
            competence=baker.make("ratings.Competence"),
            name=self.skill.name,
        )
        with self.assertRaises(ValidationError):
            skill_2.full_clean()

        with self.assertRaises(IntegrityError):
            skill_2.save()

    # Проверки функциональности
    def test_skill_successful_creation(self):
        """Проверка успешного создания объекта."""
        self.assertEqual(
            Skill.objects.count(),
            1,
            "Ошибка при создании объекта.",
        )

    def test_skill_successful_deletion(self):
        """Проверка успешного удаления объекта."""
        self.assertEqual(
            Skill.objects.count(),
            1,
        )
        self.skill.delete()
        self.assertEqual(
            Skill.objects.count(),
            0,
            "Ошибка при удалении объекта.",
        )

    # Проверки связанных полей
    def test_competence_on_delete_cascade(self):
        """
        Проверка, что при удалении Компетенции удаляются
        связанные Навыки (on_delete=models.CASCADE).
        """
        self.assertEqual(Competence.objects.count(), 1,)
        self.skill.competence.delete()
        self.assertEqual(Competence.objects.count(), 0,)

    # Проверки класса Meta
    def test_competence_related_name(self):
        """Проверка related_name для поля competence."""
        competence = self.skill.competence
        self.assertQuerySetEqual(
            competence.skills.all(),
            Skill.objects.filter(competence=competence),
            transform=lambda x: x,
            msg="'related_name' должно быть 'skills'."
        )

    def test_ordering(self):
        """Проверка сортировки."""
        self.skill.delete()
        self.assertEqual(Skill.objects.count(), 0,)

        skills_names = (
            "Работа в команде",
            "Лидерские качества",
            "Тайм-менеджмент",
            "Знание языков программирования"
        )
        skills_number = len(skills_names)

        baker.make(
            "ratings.Skill",
            competence=baker.make("ratings.Competence"),
            name=(name for name in skills_names),
            _quantity=skills_number,
        )
        expected_skills = list(Skill.objects.all())
        expected_skills.sort(key=lambda x: x.name)

        self.assertEqual(
            expected_skills,
            list(Skill.objects.all()),
            "Навыки должны быть отсортированы по названию"
        )

    # Тесты строкового представления (__str__):
    def test_str(self):
        self.assertEqual(
            str(self.skill),
            "Название навыка №1",
        )
