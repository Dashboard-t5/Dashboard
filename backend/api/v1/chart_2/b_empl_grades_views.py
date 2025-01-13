from django.db.models import Count, IntegerField, Value
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.v1.filters import RatingFilter
from api.v1.chart_2.b_empl_grades_serializers import (
    EmployeeGradesWithPositionsSerializer,
    EmployeeGradesSerializer
)
from ratings.models import Rating


# --------------------------------------------
#    Чарт 2 Вкладка b
# --------------------------------------------


class EmployeeGradesViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для работы с чартом
    "Количество сотрудников по грейдам".
    """

    serializer_class = EmployeeGradesSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RatingFilter

    def get_queryset(self):
        queryset = Rating.objects.select_related(
            "employee",
        ).values(
            "employee__grade",
        ).annotate(
            grade_employee_count=Count(
                "employee",
                distinct=True,
            )
        ).order_by(
            "grade_employee_count",
        )

        filtered_queryset = self.filter_queryset(queryset)
        total_employee_count = sum(
            item["grade_employee_count"] for item in filtered_queryset
        )

        return filtered_queryset.annotate(
            total_employee_count=Value(
                total_employee_count,
                output_field=IntegerField(),
            )
        )


# --------------------------------------------
#    Чарт 2 Вкладка b после "проваливания"
# --------------------------------------------



class EmployeeGradesWithPositionsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Вьюсет для работы с чартом
    "Количество сотрудников по грейдам".
    для ВЫБРАННОГО ГРЕЙДА.
    """

    serializer_class = EmployeeGradesWithPositionsSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RatingFilter

    def get_queryset(self):
        grade_name = self.kwargs.get("grade_name")
        queryset = Rating.objects.select_related(
            "employee",
            "position"
        ).filter(
            employee__grade=grade_name,
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
