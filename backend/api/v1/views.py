from django.db.models import Avg, Count, F, IntegerField, Q, Value
from django.db.models.functions import Cast, Concat
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.v1.filters import RatingFilter
from api.v1.serializers import (CompetenceSerializer, DomainSerializer,
                                EmployeePositionsSerializer,
                                EmployeeSerializer,
                                EmployeeSkillAverageRatingSerializer,
                                PositionSerializer, RatingSerializer,
                                SkillSerializer, SuitabilityPositionSerializer,
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


class SuitabilityPositionViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с чартом "Соответствие должности"."""

    queryset = Rating.objects.all()
    serializer_class = SuitabilityPositionSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter

    def get_queryset(self):
        return Rating.objects.all().select_related("employee").values(
            full_name=Concat(
                "employee__last_name",
                Value(" "),
                "employee__first_name"
            )
        ).annotate(
            total=Count(
                "skill",
                distinct=True,
                filter=~Q(suitability="не требуется")
            ),
            total_yes=Count(
                "skill",
                distinct=True,
                filter=Q(suitability="да")
            ),
            percentage=Cast(
                F("total_yes") * 100.0 / F("total"),
                output_field=IntegerField()
            )
        ).order_by("percentage")


class EmployeeSkillsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с чартом "Уровень владения навыками"."""

    serializer_class = EmployeeSkillAverageRatingSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = RatingFilter

    def get_queryset(self):
        # Получаем employee_id из URL
        employee_id = self.kwargs.get("employee_id")

        # Проверяем, существует ли сотрудник с этим employee_id
        employeee = get_object_or_404(Employee, id=employee_id)

        # Группируем данные по навыкам и
        # считаем среднюю оценку для каждого навыка
        return Rating.objects.filter(
            employee_id=employee_id
        ).values(
            "skill__name"
        ).annotate(
            average_rating=Avg("rating_value")
        ).order_by(
            "average_rating"
        )


class EmployeePositionsViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет для работы с чартом "Должности сотрудников"."""

    serializer_class = EmployeePositionsSerializer
    permission_classes = (AllowAny,)
    pagination_class = None
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatingFilter

    def get_queryset(self):

        return Rating.objects.all().values(
            "employee__position__name"
        ).annotate(
            count_positions=Count(
                "employee",
                distinct=True,
            )
        ).order_by('count_positions')
