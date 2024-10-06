from django.contrib.auth import get_user_model
from django.db.models import Max, OuterRef, Subquery
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from api.v1.serializers import SkillSerializer, SkillEmployeeSerializer
from ratings.models import Rating, Skill


User = get_user_model()


class SkillViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для фильтра <Колличество сотрудников,
    владеющих навыком> для всех навыков.
    """
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ("get",)


class SkillEmployeeViewSet(viewsets.ModelViewSet):
    """
    Вьюесет для фильтра <Колличество сотрудников,
    владеющих навыком> для выбранного навыка.
    """
    queryset = Rating.objects.all()
    serializer_class = SkillEmployeeSerializer
    http_method_names = ("get",)

    def get_queryset(self):
        # skill = get_object_or_404(
        #     Skill,
        #     id=self.kwargs.get("skill_id"),
        #
        # )
        skill_id = self.kwargs.get("skill_id")
        domain_id = self.kwargs.get("domain_id")
        latest_date_subquery = Rating.objects.filter(
            employee=OuterRef('employee'),
            skill=skill_id
        ).values('employee').annotate(
            latest_date=Max('rating_date')
        ).values('latest_date')
        result = Rating.objects.filter(
            skill=skill_id,
            skill__competence__domain_id=domain_id,
            rating_date=Subquery(latest_date_subquery),
            suitability="да",
        )
        return result
