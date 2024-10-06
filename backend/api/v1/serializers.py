from django.contrib.auth import get_user_model
from django.db.models import Max, OuterRef, Subquery
from rest_framework import serializers

from ratings.models import Rating, Skill

User = get_user_model()


class SkillSerializer(serializers.ModelSerializer):
    """
    Сериализатор для фильтра <Колличество сотрудников,
    владеющих навыком> для всех навыков.
    """
    count_employees = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ("name", "count_employees")

    def get_count_employees(self, obj):
        latest_date_subquery = Rating.objects.filter(
            employee=OuterRef('employee'),
            skill=obj
        ).values('employee').annotate(
            latest_date=Max('rating_date')
        ).values('latest_date')
        result = obj.ratings.filter(
            rating_date=Subquery(latest_date_subquery),
            suitability="да",
        ).count()
        return result


class SkillEmployeeSerializer(serializers.ModelSerializer):
    """
    Сериализатор для фильтра <Колличество сотрудников,
    владеющих навыком> для выбранного навыка.
    """
    skill = serializers.StringRelatedField(
        read_only=True,
    )
    employee = serializers.StringRelatedField(
        read_only=True,
    )
    count_employees = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = ("skill", "employee", "count_employees")

    def get_count_employees(self, obj):
        return 1
