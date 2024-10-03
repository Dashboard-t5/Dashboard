from django.db import models


class Domain(models.Model):
    """Модель домена."""

    name = models.CharField(
        max_length=50,
        verbose_name="Название домена",
        unique=True
    )

    class Meta:
        verbose_name = "Домен"
        verbose_name_plural = "Домены"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Competence(models.Model):
    """Модель компетенции."""

    name = models.CharField(
        max_length=200,
        verbose_name="Название компетенции",
        unique=True
    )
    domain = models.ForeignKey(
        Domain,
        on_delete=models.CASCADE,
        verbose_name="Домен",
        related_name="competencies"
    )

    class Meta:
        verbose_name = "Компетенция"
        verbose_name_plural = "Компетенции"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Skill(models.Model):
    """Модель навыка."""

    name = models.CharField(
        max_length=200, verbose_name="Название навыка", unique=True
    )
    competence = models.ForeignKey(
        Competence,
        on_delete=models.CASCADE,
        verbose_name="Компетенция",
        related_name="skills"
    )

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        ordering = ["name"]

    def __str__(self):
        return self.name
