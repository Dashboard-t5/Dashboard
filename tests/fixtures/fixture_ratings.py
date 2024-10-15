import pytest
from employees.models import Employee, Position, Team
from ratings.models import Competence, Domain, Rating, Skill


@pytest.fixture
def position():
    """Тестовые данные для должности."""
    return Position.objects.create(name="Новая должность")


@pytest.fixture
def team():
    """Тестовые данные для команды."""
    return Team.objects.create(name="Новая команда")


@pytest.fixture
def employee(team, position):
    """Тестовые данные для сотрудника."""
    return Employee.objects.create(
        first_name="Вася",
        last_name="Пупкин",
        position=position,
        team=team,
        grade="Junior",
    )


@pytest.fixture
def domain():
    """Тестовые данные для домена."""
    return Domain.objects.create(name="Новый домен")


@pytest.fixture
def competence(domain):
    """Тестовые данные для компетенции."""
    return Competence.objects.create(name="Новая команда", domain=domain)


@pytest.fixture
def skill(competence):
    """Тестовые данные для навыка."""
    return Skill.objects.create(
        name="Новый навык",
        competence=competence,
    )


@pytest.fixture
def rating(skill, employee):
    """Тестовые данные для оценки навыка."""
    return Rating.objects.create(
        employee=employee,
        skill=skill,
        rating_date="2024-10-15",
        rating_value=5,
        suitability="да",
    )
