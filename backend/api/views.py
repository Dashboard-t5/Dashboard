from django.db.models import Count, F, IntegerField, Q, Value
from django.db.models.functions import Cast, Concat
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from employees.models import Employee, Position, Team
from ratings.models import Competence, Domain, Rating, Skill

from .filters import RatingFilter
from .serializers import (CompetenceSerializer, DomainSerializer,
                          EmployeeSerializer, PositionSerializer,
                          RatingSerializer, SkillSerializer,
                          SuitabilityPositionSerializer, TeamSerializer)


class PositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с должностями."""

    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = 'name'


class TeamViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с командами."""

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = 'name'


class EmployeeViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с сотрудниками."""

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = 'name'


class DomainViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с доменами."""

    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = 'name'


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с навыками."""

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = 'name'


class CompetenceViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с компетенциями."""

    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    ordering_fields = 'name'


class RatingViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с оценками сотрудников."""

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter


class SuitabilityPositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с отчетом "Соответствие должности"."""

    queryset = Rating.objects.all()
    serializer_class = SuitabilityPositionSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.all().select_related('employee').values(full_name=Concat(
                "employee__last_name",
                Value(' '),
                "employee__first_name"
            )).annotate(
            total=Count('skill', distinct=True, filter=~Q(suitability="не требуется")),
            total_yes=Count('skill', distinct=True, filter=Q(suitability="да")),
            percentage=Cast(F('total_yes') * 100.0 / F('total'), output_field=IntegerField())
        ).order_by('percentage')
