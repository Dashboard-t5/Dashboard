from rest_framework import serializers

from ratings.models import Rating


# --------------------------------------------
#    Чарт 2 Вкладка a
# --------------------------------------------


class EmployeePositionsSerializer(
    serializers.ModelSerializer
):
    """Сериализатор для чарта "Должности сотрудников"."""

    position = serializers.CharField(
        source="employee__position__name",
    )
    position_employee_count = serializers.IntegerField()
    total_employee_count = serializers.IntegerField()
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
        Процент сотрудников, работающих на должности.
        """
        return round(
            (obj["position_employee_count"]
             / obj["total_employee_count"])
            * 100,
            1,
        )


class EmployeeGradesWithPositionsSerializer(serializers.ModelSerializer):
    """Сериализатор для чарта "Количество сотрудников по грейдам".
    для ВЫБРАННОГО ГРЕЙДА
    """

    position = serializers.CharField(
        source="employee__position__name", read_only=True
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

    def get_percentage(self, obj):
        return round(
            obj["position_employee_count"] * 100 / obj["total_employee_count"],
            1,
        )
