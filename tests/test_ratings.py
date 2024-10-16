from http import HTTPStatus

import pytest
from django.urls import reverse


@pytest.mark.django_db(transaction=True)
class TestEndpointsAPI:
    """Тестирование маршрутов."""

    @pytest.mark.parametrize(
        "name",
        ("api:skills-list", "api:domains-list", "api:competences-list",
         "api:employees-list", "api:positions-list", "api:raitings-list",
         "api:teams-list", "api:suitability_position-list",
         "api:employees_count_with_skills-list", "api:employee_grades-list",
         "api:employee_positions-list", "api:skill_level-list",
         "api:employee_scores-list", "api:skills_development-list",
         "api:position_rating-list",)
    )
    def test_availability_for_list_endpoints(self, client, name):
        url = reverse(name)
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK

    @pytest.mark.parametrize(
        "name",
        ("api:skills-detail", "api:skill_employee-list")
    )
    def test_availability_for_detail_endpoints(self, client, name, skill):
        url = reverse(name,  args=[skill.id])
        response = client.get(url)
        assert response.status_code == HTTPStatus.OK
