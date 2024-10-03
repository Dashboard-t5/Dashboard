from django.contrib import admin

from .models import Domain, Competence, Skill, Rating


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    """Админка для модели Domain."""

    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)

@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    """Админка для модели Competence."""

    list_display = ("name", "domain")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Админка для модели Rating."""

    list_display = ("employee", "skill", "rating_date", "rating_value", "suitability")
    search_fields = ("skill__name",)
    list_filter = ("skill", "rating_value", "suitability")
    ordering = ("employee", "rating_date")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Админка для модели Skill."""

    list_display = ("name", "competence")
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
