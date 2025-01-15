import django_filters

from ratings.models import Rating


class RatingFilter(django_filters.FilterSet):

    team = django_filters.NumberFilter(
        field_name="employee__team__id",
    )
    grade = django_filters.NumberFilter(
        field_name="employee__grade__id",
    )
    position = django_filters.NumberFilter(
        field_name="employee__position__id",
    )
    skill = django_filters.NumberFilter(
        field_name="skill__id",
    )
    employee = django_filters.NumberFilter(
        field_name="employee__id",
    )
    competence = django_filters.NumberFilter(
        field_name="skill__competence__id",
    )
    domain = django_filters.NumberFilter(
        field_name="skill__competence__domain__id",
    )
    start_date = django_filters.DateFilter(
        field_name="rating_date",
        lookup_expr="gte",
    )
    end_date = django_filters.DateFilter(
        field_name="rating_date",
        lookup_expr="lte",
    )

    class Meta:
        model = Rating
        fields = (
            "team",
            "grade",
            "skill",
            "position",
            "employee",
            "competence",
            "domain",
            "start_date",
            "end_date",
        )
