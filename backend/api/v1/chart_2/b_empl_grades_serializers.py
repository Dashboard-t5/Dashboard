from rest_framework import serializers

from ratings.models import Rating


# --------------------------------------------
#    Чарт 2 Вкладка b
# --------------------------------------------


class EmployeeGradesSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта
    "Количество сотрудников по грейдам".
    """

    grade = serializers.CharField(
        source="employee__grade",
    )
    grade_employee_count = serializers.IntegerField()
    total_employee_count = serializers.IntegerField()
    percentage = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = (
            "grade",
            "grade_employee_count",
            "total_employee_count",
            "percentage",
        )
        read_only_fields = (
            "__all__",
        )

    def get_percentage(self, obj):
        """
        Процент сотрудников с грейдом.
        """
        return round(
            (obj["grade_employee_count"]
             / obj["total_employee_count"])
            * 100,
            1,
        )


# --------------------------------------------
#    Чарт 2 Вкладка b после "проваливания"
# --------------------------------------------


class EmployeeGradesWithPositionsSerializer(
    serializers.ModelSerializer
):
    """Сериализатор для чарта
    "Количество сотрудников по грейдам".
    для ВЫБРАННОГО ГРЕЙДА
    """

    position = serializers.CharField(
        source="employee__position__name",
        read_only=True
    )
    position_employee_count = serializers.IntegerField(read_only=True)
    total_employee_count = serializers.IntegerField(read_only=True)
    percentage = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = (
            "position",
            "position_employee_count",
            "total_employee_count",
            "percentage",
        )
        read_only_fields = (
            "__all__",
        )

    def get_percentage(self, obj):
        """
        Процент сотрудников с выбранным грейдом в выборке.
        """
        return round(
            (obj["position_employee_count"]
             / obj["total_employee_count"])
            * 100,
            1,
        )
