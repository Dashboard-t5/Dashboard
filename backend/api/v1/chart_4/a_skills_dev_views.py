from django.db.models import Avg, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.v1.filters import RatingFilter
from api.v1.chart_4.a_skills_dev_serializers import (
    SkillsDevelopmentSerializer
)
from ratings.models import Rating


# --------------------------------------------
#    Чарт 4 Вкладка a
# --------------------------------------------


class SkillsDevelopmentViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Динамика развития навыков".
    """

    serializer_class = SkillsDevelopmentSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.select_related(
            "skill",
            "skill__competence",
            "skill__competence__domain",
        ).values(
            "rating_date",
        ).annotate(
            average_rating=Avg("rating_value"),
            average_rating_hard=Avg(
                "rating_value",
                filter=Q(skill__competence__domain__name="Hard skills"),
            ),
            average_rating_soft=Avg(
                "rating_value",
                filter=Q(skill__competence__domain__name="Soft skills"),
            ),
        ).order_by(
            "rating_date",
        )
