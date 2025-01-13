import django_filters

from ratings.models import Rating


class RatingFilter(django_filters.FilterSet):

    team = django_filters.CharFilter(
        field_name="employee__team__name",
        lookup_expr="iexact",
    )
    grade = django_filters.CharFilter(
        field_name="employee__grade",
        lookup_expr="iexact",
    )
    position = django_filters.CharFilter(
        field_name="employee__position__name",
        lookup_expr="iexact",
    )
    skill = django_filters.CharFilter(
        field_name="skill__name",
        lookup_expr="iexact",
    )
    employee = django_filters.NumberFilter(
        field_name="employee__id",
    )
    competence = django_filters.CharFilter(
        field_name="skill__competence__name",
        lookup_expr="iexact",
    )
    domain = django_filters.CharFilter(
        field_name="skill__competence__domain__name",
        lookup_expr="iexact",
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
