from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import (CompetenceViewSet, DomainViewSet,
                          EmployeesCountWithSkillsViewSet,
                          EmployeesWithSkillViewSet,
                          EmployeeGradesViewSet, EmployeePositionsViewSet,
                          EmployeeSkillsAverageRatingViewSet, EmployeeViewSet,
                          PositionViewSet, RatingViewSet,
                          SkillsDevelopmentViewSet, SkillViewSet,
                          SuitabilityPositionViewSet, TeamViewSet)

router_v1 = DefaultRouter()
router_v1.register("positions", PositionViewSet, basename="positions")
router_v1.register("teams", TeamViewSet, basename="teams")
router_v1.register("employees", EmployeeViewSet, basename="employees")
router_v1.register("domains", DomainViewSet, basename="domains")
router_v1.register("skills", SkillViewSet, basename="skills")
router_v1.register("competences", CompetenceViewSet, basename="competences")
router_v1.register("raitings", RatingViewSet, basename="raitings")

# --------------------------------------------
#    Чарт 1 Вкладка 1
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
#    Чарт 1 Вкладка 2
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
#    Чарт 2 Вкладка 1
# --------------------------------------------
router_v1.register(
    r"dashboard/employee_positions",
    EmployeePositionsViewSet,
    basename="employee_positions",
)

# --------------------------------------------
#    Чарт 2 Вкладка 2
# --------------------------------------------
router_v1.register(
    r"dashboard/employee_grades",
    EmployeeGradesViewSet,
    basename="employee_grades",
)

# --------------------------------------------
#    Чарт 4 Вкладка 1
# --------------------------------------------
router_v1.register(
    r"dashboard/skills_development",
    SkillsDevelopmentViewSet,
    basename="skills_development",
)

urlpatterns = [
    path("", include(router_v1.urls)),
]
