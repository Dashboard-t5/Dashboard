from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.v1.filters import RatingFilter
from api.v1.chart_1.b_empl_with_skills_serializers import (
    EmployeesCountWithSkillsSerializer,
    EmployeesWithSkillSerializer,
)
from api.v1.chart_1.schemas import (
    CHART_1_B1_SCHEMA,
    CHART_1_B2_SCHEMA
)
from ratings.models import Rating, Skill


# --------------------------------------------
#    Чарт 1 Вкладка B1
# --------------------------------------------


@extend_schema_view(**CHART_1_B1_SCHEMA)
class EmployeesCountWithSkillsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для чарта
    "Количество сотрудников, владеющих навыками"
     для ВСЕХ НАВЫКОВ.
    """

    serializer_class = EmployeesCountWithSkillsSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.select_related(
            "skill"
        ).filter(
            suitability="да"
        ).values(
            "skill__id",
            "skill__name",
            "skill__competence__domain__name",
        ).annotate(
            skill_employee_count=Count(
                "employee",
                distinct=True,
            )
        ).order_by(
            "skill_employee_count",
        )


# --------------------------------------------
#    Чарт 1 Вкладка B2 после "проваливания"
#           в выбранный навык.
# --------------------------------------------


@extend_schema_view(**CHART_1_B2_SCHEMA)
class EmployeesWithSkillViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для чарта
    "Количество сотрудников, владеющих навыком"
     для ВЫБРАННОГО НАВЫКА.
    """

    serializer_class = EmployeesWithSkillSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RatingFilter

    def get_queryset(self):
        skill = get_object_or_404(
            Skill,
            id=self.kwargs.get("skill_id"),
        )
        return Rating.objects.select_related(
            "employee",
            "skill",
            "skill__competence",
            "skill__competence__domain",
        ).filter(
            suitability="да",
            skill=skill,
        ).values(
            "skill__competence__domain__name",
            "employee__full_name",
        ).annotate(
            skill_employee_count=Count(
                "employee",
                distinct=True,
            ),
        )
