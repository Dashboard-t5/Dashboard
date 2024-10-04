from rest_framework import serializers

from employees.models import Team, Position, Employee
from ratings.models import Domain, Skill, Competence, Rating


class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с командами."""

    class Meta:
        model = Team
        fields = ("name",)


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с должностями."""

    class Meta:
        model = Position
        fields = ("name",)


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с сотрудниками."""

    class Meta:
        model = Employee
        exclude = ["id"]


class DomainSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с доменами."""

    class Meta:
        model = Domain
        fields = ("name",)


class CompetenceSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с компетенциями."""

    class Meta:
        model = Competence
        fields = ("name",)


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с навыками."""

    class Meta:
        model = Skill
        fields = ("name",)


class RatingSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с оценками."""

    class Meta:
        model = Rating
        fields = "__all__"
