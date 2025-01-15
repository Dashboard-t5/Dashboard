from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from config import MIN_LENGTH, MAX_LENGTH


class Position(models.Model):
    """Модель должности."""

    name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name="Название должности",
        unique=True,
    )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Team(models.Model):
    """Модель команды."""

    name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name="Название команды",
        unique=True
    )

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Модель сотрудника."""

    JUNIOR = "Junior"
    MIDDLE = "Middle"
    SENIOR = "Senior"
    INTERN = "Intern"
    LEAD = "Lead"
    HEAD = "Head"

    GRADE_CHOICES = (
        (JUNIOR, "Джуниор"),
        (MIDDLE, "Мидл"),
        (SENIOR, "Сеньор"),
        (INTERN, "Cтажер"),
        (LEAD, "Ведущий специалист"),
        (HEAD, "Руководитель"),
    )
    first_name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name="Имя сотрудника",
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r"^[а-яА-ЯёЁa-zA-Z]+(\s?\-?[а-яА-ЯёЁa-zA-Z]+){0,5}$",
                message="Введены недопустимые символы.",
                code="invalid_employee_first_name",
            ),
            MinLengthValidator(limit_value=2),
        ],
    )
    last_name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name="Фамилия сотрудника",
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=r"^[а-яА-ЯёЁa-zA-Z]+(\s?\-?[а-яА-ЯёЁa-zA-Z]+){0,5}$",
                message="Введены недопустимые символы.",
                code="invalid_employee_last_name",
            ),
            MinLengthValidator(limit_value=2),
        ],
    )
    full_name = models.CharField(
        max_length=MAX_LENGTH,
        verbose_name="Полное имя сотрудника",
        blank=True,
        null=True,
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name="Должность",
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        verbose_name="Команда",
    )
    grade = models.CharField(
        max_length=max(len(grade) for grade, _ in GRADE_CHOICES),
        verbose_name="Грейд сотрудника",
        choices=GRADE_CHOICES,
        default=JUNIOR,
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        default_related_name = "employees"
        ordering = ("last_name", "first_name")

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def save(self, *args, **kwargs):
        self.full_name = f"{self.last_name} {self.first_name}"
        super().save(*args, **kwargs)
