from rest_framework import serializers

from ratings.models import Rating


# --------------------------------------------
#    Чарт 3 Вкладка a
# --------------------------------------------


class SkillsLevelSerializer(
    serializers.ModelSerializer
):
    """Сериализатор для чарта "Уровень владения навыками"."""

    domain = serializers.CharField(
        source="skill__competence__domain__name",
    )
    skill_name = serializers.CharField(
        source="skill__name",
    )
    skill_level = serializers.DecimalField(
        max_digits=3,
        decimal_places=2,
    )

    class Meta:
        model = Rating
        fields = (
            "domain",
            "skill_name",
            "skill_level",
        )
        read_only_fields = (
            "__all__",
        )
