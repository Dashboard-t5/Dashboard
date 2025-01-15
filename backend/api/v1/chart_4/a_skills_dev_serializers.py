from rest_framework import serializers

from ratings.models import Rating

# --------------------------------------------
#    Чарт 4 Вкладка A
# --------------------------------------------


class SkillsDevelopmentSerializer(
    serializers.ModelSerializer
):
    """
    Сериализатор для чарта
    "Динамика развития навыков".
    """

    rating_date = serializers.DateField()
    average_rating = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    average_rating_hard = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )
    average_rating_soft = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        model = Rating
        fields = (
            "rating_date",
            "average_rating",
            "average_rating_hard",
            "average_rating_soft",
        )
        read_only_fields = (
            "__all__",
        )
