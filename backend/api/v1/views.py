from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.v1.filters import RatingFilter
from api.v1.serializers import (BusFactorSerializer, CompetenceSerializer,
                                DomainSerializer,
                                EmployeeSerializer,
                                PositionSerializer,
                                RatingSerializer,
                                SkillSerializer,
                                TeamSerializer)
from employees.models import Employee, Position, Team
from ratings.models import Competence, Domain, Rating, Skill


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с должностями."""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = "name"


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с командами."""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = "name"


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с сотрудниками."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = "name"


class DomainViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с доменами."""

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = "name"


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с навыками."""

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = "name"


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с компетенциями."""

    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = "name"


class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с оценками сотрудников."""

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter


# --------------------------------------------
#    Bus-фактор
# --------------------------------------------
class BusFactorViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Вьюсет для Bus-фактора."""

    serializer_class = BusFactorSerializer
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.select_related(
            "skill"
        ).filter(
            suitability="да"
        ).values(
            "skill__name",
        ).annotate(
            skill_employee_count=Count(
                "employee",
                distinct=True,
            )
        ).order_by(
            "skill_employee_count",
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(
            queryset[0]
        )
        return Response(serializer.data)
