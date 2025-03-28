from django.db.models import Avg, Count, F, IntegerField, Q
from django.db.models.functions import Cast, Round
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.v1.chart_1.a_suit_position_serializers import (
    EmployeeSkillAverageRatingSerializer,
    SuitabilityPositionSerializer
)
from api.v1.chart_1.schemas import (
    CHART_1_A1_SCHEMA,
    CHART_1_A2_SCHEMA
)
from api.v1.filters import RatingFilter
from employees.models import Employee
from ratings.models import Rating


# --------------------------------------------
#    Чарт 1 Вкладка A1
# --------------------------------------------


@extend_schema_view(**CHART_1_A1_SCHEMA)
class SuitabilityPositionViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Вьюсет для работы с чартом
    "Соответствие должности".
    """

    serializer_class = SuitabilityPositionSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.select_related(
            "employee",
            "employee__team",
        ).values(
            "employee__id",
            "employee__full_name",
        ).annotate(
            total=Count(
                "skill",
                # distinct=True,
                filter=~Q(suitability="не требуется"),
            ),
            total_yes=Count(
                "skill",
                # distinct=True,
                filter=Q(suitability="да")
            ),
            percentage=Cast(
                F("total_yes") * 100.0 / F("total"),
                output_field=IntegerField(),
            ),
        ).order_by(
            "percentage",
        )


# --------------------------------------------
#    Чарт 1 Вкладка A2 после "проваливания"
#           в выбранного сотрудника.
# --------------------------------------------


@extend_schema_view(**CHART_1_A2_SCHEMA)
class EmployeeSkillsAverageRatingViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Вьюсет для работы с чартом
    "Соответствие должности"
    для выбранного сотрудника.
    """

    serializer_class = EmployeeSkillAverageRatingSerializer
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        employee = get_object_or_404(
            Employee,
            id=self.kwargs.get("employee_id")
        )

        # Группируем данные по навыкам и
        # считаем среднюю оценку для каждого навыка
        return Rating.objects.filter(
            employee=employee
        ).values(
            "skill__name"
        ).annotate(
            average_rating=Round(Avg("rating_value"), precision=1)
        ).order_by(
            "average_rating"
        )
