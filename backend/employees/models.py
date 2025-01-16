from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator

from employees.constants import (
    FIRST_NAME_MAX_LENGTH,
    FIRST_NAME_MIN_LENGTH,
    FULL_NAME_MAX_LENGTH,
    GRADE_CHOICES,
    GRADE_MAX_LENGTH,
    JUNIOR,
    LAST_NAME_MAX_LENGTH,
    LAST_NAME_MIN_LENGTH,
    POSITION_NAME_MAX_LENGTH,
    TEAM_NAME_MAX_LENGTH,
    VALID_NAME_REGEX
)


class Position(models.Model):
    """Модель должности."""

    name = models.CharField(
        max_length=POSITION_NAME_MAX_LENGTH,
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
        max_length=TEAM_NAME_MAX_LENGTH,
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

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        verbose_name="Имя сотрудника",
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=VALID_NAME_REGEX,
                message="Введены недопустимые символы.",
                code="invalid_employee_first_name",
            ),
            MinLengthValidator(
                limit_value=FIRST_NAME_MIN_LENGTH
            ),
        ],
    )
    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        verbose_name="Фамилия сотрудника",
        blank=False,
        null=False,
        validators=[
            RegexValidator(
                regex=VALID_NAME_REGEX,
                message="Введены недопустимые символы.",
                code="invalid_employee_last_name",
            ),
            MinLengthValidator(
                limit_value=LAST_NAME_MIN_LENGTH
            ),
        ],
    )
    full_name = models.CharField(
        max_length=FULL_NAME_MAX_LENGTH,
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
        max_length=GRADE_MAX_LENGTH,
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
