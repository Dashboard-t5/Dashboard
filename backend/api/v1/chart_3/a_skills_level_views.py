from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins, viewsets

from api.v1.filters import RatingFilter
from api.v1.chart_3.a_skills_level_serializers import (
    SkillsLevelSerializer
)
from api.v1.chart_3.schemas import CHART_3_A_SCHEMA
from ratings.models import Rating


# --------------------------------------------
#    Чарт 3 Вкладка A
# --------------------------------------------


@extend_schema_view(**CHART_3_A_SCHEMA)
class SkillsLevelViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Уровень владения навыками".
    """

    serializer_class = SkillsLevelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.select_related(
            "skill",
            "skill__competence",
            "skill__competence__domain",
        ).values(
            "skill__competence__domain__name",
            "skill__name"
        ).annotate(
            skill_level=Avg("rating_value")
        ).order_by(
            "skill_level"
        )
