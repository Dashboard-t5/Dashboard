#       План тестирования Модель Employee
# 1) Проверка существования полей модели
# 2) Проверка типов полей модели
# 3) Проверка, что обязательные поля не могут быть пустыми
# 4) Проверка, что текстовые поля не могут быть blank.
# 5) Проверка, валидации полей
# 6) поле "grade":
# 	1. дефолтное значение равно JUNIOR.
# 	2. значение grade соответствует одному из GRADE_CHOICES
# 7) Проверка успешного создания объекта
# 8) Проверка успешного удаления объекта
# 9) Проверка, что при удалении Должности удаляются связанные
#       сотрудники 	(on_delete=models.CASCADE).
# 10) Проверка, что при удалении Команды удаляются связанные
#       сотрудники 	(on_delete=models.CASCADE).
# 11) Проверка related_name связанных полей
# 12) Тестирование класса Meta (сортировка)
# 13) Тесты строкового представления (__str__)
# 14) Тесты метода save()

from model_bakery import baker

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError, transaction
from django.db.models import (
    BigAutoField,
    CharField,
    ForeignKey
)
from django.test import TestCase

from employees.constants import (
    FIRST_NAME_MAX_LENGTH,
    FIRST_NAME_MIN_LENGTH,
    FULL_NAME_MAX_LENGTH,
    GRADE_CHOICES,
    GRADE_MAX_LENGTH,
    JUNIOR,
    LAST_NAME_MAX_LENGTH,
    LAST_NAME_MIN_LENGTH,
)
from employees.models import Employee

User = get_user_model()


class TestEmployeeModel(TestCase):
    """
    Тесты для модели сотрудника Employee.
    """

    REQUIRED_FIELDS = ("first_name", "last_name", "position", "team", "grade")
    validation_data = [
        ("first_name", "", False),  # Проверка на blank=False.
        ("last_name", "", False),  # Проверка на blank=False.
        ("grade", "", False),  # Проверка на blank=False.
        ("first_name", "a" * (FIRST_NAME_MIN_LENGTH - 1), False),
        ("first_name", "a" * (FIRST_NAME_MAX_LENGTH + 1), False),
        ("last_name", "a" * (LAST_NAME_MIN_LENGTH - 1), False),
        ("last_name", "a" * (LAST_NAME_MAX_LENGTH + 1), False),
        ("full_name", "a" * (FULL_NAME_MAX_LENGTH + 1), False),
        ("grade", "a" * (GRADE_MAX_LENGTH + 1), False),
        ("first_name", "иван", True),
        ("first_name", "Иван", True),
        ("first_name", "12345", False),
        ("first_name", "Иван!", False),
        ("first_name", "Иван Ив@нов", False),
        ("first_name", "Иван- Иванов", False),
        ("last_name", "Иванов", True),
        ("last_name", "иванов", True),
        ("last_name", "12345", False),
        ("last_name", "Иванов!", False),
        ("last_name", "Иван Ив@нов", False),
        ("last_name", "Иван- Иванов", False),
        ("grade", "Кочегар", False), # Проверка на значение не из CHOICES.
        ("grade", "Kochegar", False), # Проверка на значение не из CHOICES.
    ]

    @classmethod
    def setUpTestData(cls):
        cls.team = baker.make(
            "employees.Team",
            name="Название команды №1",
        )
        cls.position = baker.make(
            "employees.Position",
            name="Название должности №1",
        )
        cls.employee = baker.make(
            "employees.Employee",
            position=cls.position,
            team=cls.team,
            first_name="Имя",
            last_name="Фамилия",
        )

    def test_employee_fields_existence(self):
        """Проверка существования полей модели."""
        fields = Employee._meta.fields
        fields_names = (field.name for field in fields)
        self.assertIn("id", fields_names)
        self.assertIn("first_name", fields_names)
        self.assertIn("last_name", fields_names)
        self.assertIn("full_name", fields_names)
        self.assertIn("position", fields_names)
        self.assertIn("team", fields_names)
        self.assertIn("grade", fields_names)

    def test_employee_fields_types(self):
        """
        Проверка типов полей модели.
        """
        self.assertIsInstance(
            Employee._meta.get_field("id"),
            BigAutoField
        )
        self.assertIsInstance(
            Employee._meta.get_field("first_name"),
            CharField
        )
        self.assertIsInstance(
            Employee._meta.get_field("last_name"),
            CharField
        )
        self.assertIsInstance(
            Employee._meta.get_field("full_name"),
            CharField
        )
        self.assertIsInstance(
            Employee._meta.get_field("position"),
            ForeignKey
        )
        self.assertIsInstance(
            Employee._meta.get_field("team"),
            ForeignKey
        )
        self.assertIsInstance(
            Employee._meta.get_field("grade"),
            CharField
        )

    def test_required_fields_cannot_be_null(self):
        """
        Проверка, что обязательные поля не могут быть пустыми.
        """
        for field in self.REQUIRED_FIELDS:
            with transaction.atomic():
                setattr(self.employee, field, None)
                with self.assertRaises(IntegrityError):
                    self.employee.save()

    def test_fields_validation(self):
        """Проверка валидации полей."""
        for field, value, is_valid in self.validation_data:
            employee = baker.prepare(
                "employees.Employee",
                team=baker.make("employees.Team"),
                position=baker.make("employees.Position"),
                **{field: value},
            )
            if is_valid:
                try:
                    employee.full_clean()
                    employee.save()
                    employee.refresh_from_db()
                    self.assertEqual(
                        getattr(employee, field),
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
                    employee.full_clean()

    def test_default_grade_field(self):
        self.assertIs(
            self.employee.grade,
            JUNIOR,
            f"Грейд по умолчанию должен быть {JUNIOR}."
        )

    def test_valid_grade_choices(self):
        """Проверка, что поле 'grade' принимает только допустимые значения."""
        valid_grades = (value for value, _ in GRADE_CHOICES)
        for grade in valid_grades:
            employee = baker.prepare(
                "employees.Employee",
                team=baker.make("employees.Team"),
                position=baker.make("employees.Position"),
                grade=grade,
            )
            try:
                employee.full_clean()
            except ValidationError:
                self.fail(f"Значение grade '{grade}' не прошло валидацию")

    # Проверки функциональности
    def test_employee_successful_creation(self):
        """Проверка успешного создания объекта."""
        self.assertEqual(
            Employee.objects.count(),
            1,
            "Ошибка при создании объекта.",
        )

    def test_employee_successful_deletion(self):
        """Проверка успешного удаления объекта."""
        self.assertEqual(
            Employee.objects.count(),
            1,
        )
        self.employee.delete()
        self.assertEqual(
            Employee.objects.count(),
            0,
            "Ошибка при удалении объекта.",
        )

    # Проверки связанных полей
    def test_position_on_delete_cascade(self):
        """
        Проверка, что при удалении Должности удаляются
        связанные сотрудники (on_delete=models.CASCADE).
        """
        self.assertEqual(Employee.objects.count(), 1,)
        self.employee.position.delete()
        self.assertEqual(Employee.objects.count(), 0,)

    def test_team_on_delete_cascade(self):
        """
        Проверка, что при удалении Команды удаляются
        связанные сотрудники (on_delete=models.CASCADE).
        """
        self.assertEqual(Employee.objects.count(), 1,)
        self.employee.team.delete()
        self.assertEqual(Employee.objects.count(), 0,)

    # Проверки класса Meta
    def test_position_related_name(self):
        """Проверка related_name для поля position."""
        position = self.employee.position
        self.assertQuerySetEqual(
            position.employees.all(),
            Employee.objects.filter(position=position),
            transform=lambda x: x,
            msg="'related_name' должно быть 'employees'."
        )

    def test_team_related_name(self):
        """Проверка related_name для поля team."""
        team = self.employee.team
        self.assertQuerySetEqual(
            team.employees.all(),
            Employee.objects.filter(team=team),
            transform=lambda x: x,
            msg="'related_name' должно быть 'employees'."
        )

    def test_ordering(self):
        """Проверка сортировки."""
        self.employee.delete()
        self.assertEqual(Employee.objects.count(), 0,)

        # Создаем список объектов Employee
        employees = baker.make(
            "employees.Employee",
            _quantity=5,
        )

        employees.sort(key=lambda x: (x.last_name, x.first_name))

        self.assertEqual(
            employees,
            list(Employee.objects.all()),
            "Сотрудники должны быть отсортированы "
            "по 'last_name', 'first_name'."
        )

    # Тесты строкового представления (__str__):
    def test_str(self):
        self.employee.first_name = "Максим"
        self.employee.last_name = "Богданович"
        self.assertEqual(
            str(self.employee),
            f"Богданович Максим"
        )

    # Тесты метода save()
    def test_save_method_behavior(self):
        employee = baker.make(
            "employees.Employee",
            first_name="Максим",
            last_name="Богданович",
        )
        self.assertEqual(
            employee.full_name,
            "Богданович Максим"
        )
