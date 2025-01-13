from rest_framework import serializers

from ratings.models import Rating


# --------------------------------------------
#    Чарт 3 Вкладка b
# --------------------------------------------


class EmployeeScoresSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта
    "Балы сотрудников по навыкам и датам".
    """

    employee = serializers.CharField(
        source="employee__full_name",
    )
    domain = serializers.CharField(
        source="skill__competence__domain__name",
    )
    competence_name = serializers.CharField(
        source="skill__competence__name",
    )
    skill_name = serializers.CharField(
        source="skill__name",
    )

    class Meta:
        model = Rating
        fields = (
            "employee",
            "domain",
            "competence_name",
            "skill_name",
            "rating_date",
        )
        read_only_fields = (
            "__all__",
        )
