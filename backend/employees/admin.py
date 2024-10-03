from django.contrib import admin

from .models import Position, Employee, Team


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    """Админка для модели Position."""

    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    """Админка для модели Employee."""

    list_display = ("first_name", "last_name", "position", "team", "grade")
    search_fields = ("grade__name",)
    list_filter = ("team", "position", "grade")
    ordering = ("first_name", "last_name")

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    """Админка для модели Team."""

    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)
