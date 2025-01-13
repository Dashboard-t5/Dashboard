from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.chart_1.a_suit_position_views import (
    EmployeeSkillsAverageRatingViewSet,
    SuitabilityPositionViewSet
)
from api.v1.chart_1.b_empl_with_skills_views import (
    EmployeesCountWithSkillsViewSet,
    EmployeesWithSkillViewSet
)
from api.v1.chart_2.a_empl_pos_views import (
    EmployeePositionsViewSet
)
from api.v1.chart_2.b_empl_grades_views import (
    EmployeeGradesWithPositionsViewSet,
    EmployeeGradesViewSet
)
from api.v1.chart_3.a_skills_level_views import (
    SkillsLevelViewSet
)
from api.v1.chart_3.b_empl_scores_views import (
    EmployeeScoresViewSet
)
from api.v1.chart_4.a_skills_dev_views import (
    SkillsDevelopmentViewSet
)
from api.v1.chart_4.b_pos_grade_empl_rating_views import (
    EmployeeRatingViewSet,
    GradeRatingViewSet,
    PositionRatingViewSet
)
from api.v1.views import (
    BusFactorViewSet,
    CompetenceViewSet,
    DomainViewSet,
    EmployeeViewSet,
    PositionViewSet,
    RatingViewSet,
    SkillViewSet,
    TeamViewSet
)

router_v1 = DefaultRouter()
router_v1.register("positions", PositionViewSet, basename="positions")
router_v1.register("teams", TeamViewSet, basename="teams")
router_v1.register("employees", EmployeeViewSet, basename="employees")
router_v1.register("domains", DomainViewSet, basename="domains")
router_v1.register("skills", SkillViewSet, basename="skills")
router_v1.register("competences", CompetenceViewSet, basename="competences")
router_v1.register("raitings", RatingViewSet, basename="raitings")

# --------------------------------------------
#    Чарт 1 Вкладка a
# --------------------------------------------
router_v1.register(
    "dashboard/suitability_position",
    SuitabilityPositionViewSet,
    basename="suitability_position"
)
router_v1.register(
    r"dashboard/suitability_position/(?P<employee_id>\d+)/skills",
    EmployeeSkillsAverageRatingViewSet,
    basename="employee_skills",
)

# --------------------------------------------
#    Чарт 1 Вкладка b
# --------------------------------------------
router_v1.register(
    r"dashboard/employees_count_with_skills",
    EmployeesCountWithSkillsViewSet,
    basename="employees_count_with_skills",
)
router_v1.register(
    r"dashboard/employees_with_skill/(?P<skill_id>\d+)/employees",
    EmployeesWithSkillViewSet,
    basename="skill_employee",
)

# --------------------------------------------
#    Чарт 2 Вкладка a
# --------------------------------------------
router_v1.register(
    r"dashboard/employee_positions",
    EmployeePositionsViewSet,
    basename="employee_positions",
)

# --------------------------------------------
#    Чарт 2 Вкладка b
# --------------------------------------------
router_v1.register(
    r"dashboard/employee_grades",
    EmployeeGradesViewSet,
    basename="employee_grades",
)
router_v1.register(
    r"dashboard/employee_grades/(?P<grade_name>\w+)/positions",
    EmployeeGradesWithPositionsViewSet,
    basename="employee_grades_positions",
)
# --------------------------------------------
#    Чарт 3 Вкладка a
# --------------------------------------------
router_v1.register(
    r"dashboard/skill_level",
    SkillsLevelViewSet,
    basename="skill_level",
)
# --------------------------------------------
#    Чарт 3 Вкладка b
# --------------------------------------------
router_v1.register(
    r"dashboard/employee_scores",
    EmployeeScoresViewSet,
    basename="employee_scores",
)
# --------------------------------------------
#    Чарт 4 Вкладка a
# --------------------------------------------
router_v1.register(
    r"dashboard/skills_development",
    SkillsDevelopmentViewSet,
    basename="skills_development",
)

# --------------------------------------------
#    Чарт 4 Вкладка b
# --------------------------------------------
router_v1.register(
    r"dashboard/position_rating",
    PositionRatingViewSet,
    basename="position_rating",
)
router_v1.register(
    r"dashboard/position_rating/(?P<position_id>\d+)/grades",
    GradeRatingViewSet,
    basename="grade_rating",
)
router_v1.register(
    r"dashboard/position_rating/(?P<position_id>\d+)/grades/(?P<grade_name>\w+)",
    EmployeeRatingViewSet,
    basename="employee_rating",
)

# --------------------------------------------
#    Bus-фактор
# --------------------------------------------
router_v1.register(
    r"dashboard/bus_factor",
    BusFactorViewSet,
    basename="bus_factor",
)

urlpatterns = [
    path("", include(router_v1.urls)),
]
