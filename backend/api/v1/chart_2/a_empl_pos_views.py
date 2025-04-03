from django.db.models import Count, IntegerField, Value
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.v1.filters import RatingFilter
from api.v1.chart_2.a_empl_pos_serializers import (
    EmployeePositionsSerializer
)
from api.v1.chart_2.schemas import CHART_2_A_SCHEMA
from ratings.models import Rating

# --------------------------------------------
#    Чарт 2 Вкладка A
# --------------------------------------------


@extend_schema_view(**CHART_2_A_SCHEMA)
class EmployeePositionsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Должности сотрудников".
    """

    serializer_class = EmployeePositionsSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RatingFilter

    def get_queryset(self):
        queryset = Rating.objects.select_related(
            "employee",
            "employee__position",
        ).values(
            "employee__position__name",
        ).annotate(
            position_employee_count=Count(
                "employee",
                distinct=True,
            )
        ).order_by(
            "position_employee_count",
        )

        filtered_queryset = self.filter_queryset(queryset)
        total_employee_count = sum(
            item["position_employee_count"] for item in filtered_queryset
        )

        return filtered_queryset.annotate(
            total_employee_count=Value(
                total_employee_count,
                output_field=IntegerField(),
            )
        )
