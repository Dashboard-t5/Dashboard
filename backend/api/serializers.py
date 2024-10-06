from rest_framework import serializers

from employees.models import Team, Position, Employee
from ratings.models import Domain, Skill, Competence, Rating


class TeamSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с командами."""

    class Meta:
        model = Team
        fields = ("id", "name")


class PositionSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с должностями."""

    class Meta:
        model = Position
        fields = ("id", "name")


class EmployeeSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с сотрудниками."""

    team = serializers.StringRelatedField(
        source='team.name', read_only=True
    )
    position = serializers.StringRelatedField(
        source='position.name', read_only=True
    )

    class Meta:
        model = Employee
        fields = "__all__"


class DomainSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с доменами."""

    class Meta:
        model = Domain
        fields = ("id", "name")


class CompetenceSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с компетенциями."""

    class Meta:
        model = Competence
        fields = ("id", "name")


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с навыками."""

    class Meta:
        model = Skill
        fields = ("id", "name")


class RatingSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с оценками."""

    employee = serializers.StringRelatedField(
        read_only=True
    )
    team = serializers.StringRelatedField(
        source='employee.team', read_only=True
    )
    position = serializers.StringRelatedField(
        source='employee.position', read_only=True
    )
    grade = serializers.StringRelatedField(
        source='employee.grade', read_only=True
    )
    skill = serializers.StringRelatedField(
        source='skill.name', read_only=True
    )
    # domain = serializers.StringRelatedField(
    #     source='skill.competence.domain', read_only=True
    # )

    class Meta:
        model = Rating
        fields = (
            "employee",
            "team",
            "grade",
            "position",
            "skill",
            # "domain",
            "rating_date",
            "rating_value",
            "suitability"
        )
