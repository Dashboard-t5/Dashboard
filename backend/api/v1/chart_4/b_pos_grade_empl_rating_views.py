from django.db.models import Avg
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.v1.filters import RatingFilter
from api.v1.chart_4.b_pos_grade_empl_rating_serializers import (
    EmployeeRatingSerializer,
    GradeRatingSerializer,
    PositionRatingSerializer
)
from api.v1.chart_4.schemas import (
    CHART_4_B1_SCHEMA,
    CHART_4_B2_SCHEMA,
    CHART_4_B3_SCHEMA
)
from employees.models import Position
from ratings.models import Rating


# --------------------------------------------
#    Чарт 4 Вкладка B1
# --------------------------------------------


@extend_schema_view(**CHART_4_B1_SCHEMA)
class PositionRatingViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Оценки сотрудников по должностям".
    """

    serializer_class = PositionRatingSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.select_related(
            "employee",
            "employee__position",
        ).values(
            "employee__position__name",
            "employee__position__id",
        ).annotate(
            average_rating=Avg("rating_value"),
        ).order_by(
            "average_rating",
        )



# --------------------------------------------
#    Чарт 4 Вкладка B2 после "проваливания" в
#           выбранную должность
# --------------------------------------------


@extend_schema_view(**CHART_4_B2_SCHEMA)
class GradeRatingViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Оценки сотрудников по должностям".
     для ВЫБРАННОЙ ДОЛЖНОСТИ.
    """

    serializer_class = GradeRatingSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RatingFilter

    def get_queryset(self):
        position = get_object_or_404(
            Position,
            id=self.kwargs.get("position_id"),
        )
        return Rating.objects.select_related(
            "employee",
            "employee__position",
        ).filter(
            employee__position=position,
        ).values(
            "employee__grade",
        ).annotate(
            average_rating=Avg("rating_value"),
        ).order_by(
            "average_rating",
        )


# --------------------------------------------
#    Чарт 4 Вкладка B3 после "проваливания" в
#           выбранный грейд
# --------------------------------------------


@extend_schema_view(**CHART_4_B3_SCHEMA)
class EmployeeRatingViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Оценки сотрудников по должностям".
     для ВЫБРАННОЙ ДОЛЖНОСТИ И ГРЕЙДА.
    """

    serializer_class = EmployeeRatingSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RatingFilter

    def get_queryset(self):
        position = get_object_or_404(
            Position,
            id=self.kwargs.get("position_id"),
        )
        grade_name = self.kwargs.get("grade_name")
        return Rating.objects.select_related(
            "employee",
            "employee__position",
        ).filter(
            employee__position=position,
            employee__grade=grade_name,
        ).values(
            "employee__id",
            "employee__full_name",
        ).annotate(
            average_rating=Avg("rating_value"),
        ).order_by(
            "average_rating",
        )
