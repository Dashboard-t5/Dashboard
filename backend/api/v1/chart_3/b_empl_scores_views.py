from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins, viewsets

from api.v1.filters import RatingFilter
from api.v1.chart_3.b_empl_scores_serializers import (
    EmployeeScoresSerializer
)
from api.v1.chart_3.schemas import CHART_3_B_SCHEMA
from ratings.models import Rating


# --------------------------------------------
#    Чарт 3 Вкладка B
# --------------------------------------------


@extend_schema_view(**CHART_3_B_SCHEMA)
class EmployeeScoresViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Балы сотрудников по навыкам и датам".
    """

    serializer_class = EmployeeScoresSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.select_related(
            "employee",
            "skill",
            "skill__competence",
            "skill__competence__domain"
        ).values(
            "employee__full_name",
            "skill__competence__domain__name",
            "skill__competence__name",
            "skill__name",
            "rating_date",
            "rating_value",
        ).order_by(
            "employee__full_name"
        )
