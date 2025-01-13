from django.db.models import Count
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from api.v1.filters import RatingFilter
from ratings.models import Rating, Skill
from api.v1.chart_1.b_empl_with_skills_serializers import (
    EmployeesCountWithSkillsSerializer,
    EmployeesWithSkillSerializer,
)


# --------------------------------------------
#    Чарт 1 Вкладка b
# --------------------------------------------


class EmployeesCountWithSkillsViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """
    Вьюсет для чарта "Количество сотрудников, владеющих навыком"
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
#    Чарт 1 Вкладка b после "проваливания"
# --------------------------------------------


class EmployeesWithSkillViewSet(
    viewsets.ReadOnlyModelViewSet
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
