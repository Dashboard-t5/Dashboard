from django.db import models


class Position(models.Model):
    """Модель должности."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название должности",
        unique=True,
    )

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Team(models.Model):
    """Модель команды."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название команды",
        unique=True
    )

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Модель сотрудника."""

    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя сотрудника",
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия сотрудника",
        blank=False,
        null=False,
    )
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        verbose_name="Должность",
        related_name="employee_position"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        verbose_name="Команда",
        related_name="employee_team"
    )

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
        ordering = ["name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"