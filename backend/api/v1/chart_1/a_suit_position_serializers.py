from rest_framework import serializers

from ratings.models import Rating


# --------------------------------------------
#    Чарт 1 Вкладка A1
# --------------------------------------------


class SuitabilityPositionSerializer(
    serializers.ModelSerializer
):
    """Сериализатор для чарта "Соответствие должности"."""

    employee_id = serializers.CharField(
        source="employee__id",
    )
    employee = serializers.CharField(
        source="employee__full_name",
    )
    total_yes = serializers.IntegerField()
    total = serializers.IntegerField()
    percentage = serializers.FloatField()

    class Meta:
        model = Rating
        fields = (
            "employee_id",
            "employee",
            "total_yes",
            "total",
            "percentage"
        )
        read_only_fields = (
            "__all__",
        )


# --------------------------------------------
#    Чарт 1 Вкладка A2 после "проваливания"
#           в выбранного сотрудника.
# --------------------------------------------


class EmployeeSkillAverageRatingSerializer(
    serializers.ModelSerializer
):
    """Сериализатор для чарта "Уровень владения навыками"."""

    skill_name = serializers.CharField(
        source="skill__name",
    )
    average_rating = serializers.FloatField()

    class Meta:
        model = Rating
        fields = (
            "skill_name",
            "average_rating",
        )
        read_only_fields = (
            "__all__",
        )
