from rest_framework import serializers

from ratings.models import Rating


# --------------------------------------------
#    Чарт 4 Вкладка B1
# --------------------------------------------


class PositionRatingSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта
    "Оценки сотрудников по должностям".
    """

    position = serializers.CharField(
        source="employee__position__name",
    )
    position_id = serializers.CharField(
        source="employee__position__id",
    )
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        model = Rating
        fields = (
            "position",
            "position_id",
            "average_rating",
        )
        read_only_fields = (
            "__all__",
        )


# --------------------------------------------
#    Чарт 4 Вкладка B2 после "проваливания" в
#           выбранную должность
# --------------------------------------------


class GradeRatingSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта
    "Оценки сотрудников по должностям".
    для ВЫБРАННОЙ ДОЛЖНОСТИ
    """
    grade = serializers.CharField(
        source="employee__grade",
    )
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        model = Rating
        fields = (
            "grade",
            "average_rating",
        )
        read_only_fields = (
            "__all__",
        )


# --------------------------------------------
#    Чарт 4 Вкладка B3 после "проваливания" в
#           выбранный грейд
# --------------------------------------------


class EmployeeRatingSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта
    "Оценки сотрудников по должностям".
    для ВЫБРАННОЙ ДОЛЖНОСТИ И ГРЕЙДА
    """

    employee = serializers.CharField(
        source="employee__full_name",
    )
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        model = Rating
        fields = (
            "employee",
            "average_rating",
        )
        read_only_fields = (
            "__all__",
        )
