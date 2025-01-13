from rest_framework import serializers

from ratings.models import Rating


# --------------------------------------------
#    Чарт 1 Вкладка b
# --------------------------------------------


class EmployeesCountWithSkillsSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта "Количество сотрудников,
    владеющих навыком" для ВСЕХ НАВЫКОВ.
    """

    domain = serializers.CharField(
        source="skill__competence__domain__name",
    )
    skill_id = serializers.CharField(
        source="skill__id",
    )
    skill_name = serializers.CharField(
        source="skill__name",
    )
    count_employees = serializers.IntegerField(
        source="skill_employee_count",
    )

    class Meta:
        model = Rating
        fields = (
            "domain",
            "skill_id",
            "skill_name",
            "count_employees",
        )
        read_only_fields = (
            "__all__",
        )


# --------------------------------------------
#    Чарт 1 Вкладка b после "проваливания"
# --------------------------------------------


class EmployeesWithSkillSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта "Количество сотрудников,
    владеющих навыком" для ВЫБРАННОГО НАВЫКА.
    """

    domain = serializers.CharField(
        source="skill__competence__domain__name",
    )
    employee = serializers.CharField(
        source="employee__full_name",
    )
    count_employees = serializers.IntegerField(
        source="skill_employee_count",
    )

    class Meta:
        model = Rating
        fields = (
            "domain",
            "employee",
            "count_employees",
        )
        read_only_fields = (
            "__all__",
        )