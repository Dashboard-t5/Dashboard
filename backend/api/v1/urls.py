from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import (CompetenceViewSet, DomainViewSet,
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
# router_v1.register(
#     r"domains/(?P<domain_id>\d+)/skills/(?P<skill_id>\d+)/employees",
#     SkillEmployeeViewSet,
#     basename="skill_employee",
# )
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

router_v1.register(
    r"dashboard/employee_positions",
    EmployeePositionsViewSet,
    basename="employee_positions",
)

router_v1.register(
    r"dashboard/employee_grades",
    EmployeeGradesViewSet,
    basename="employee_grades",
)

router_v1.register(
    r"dashboard/skills_development",
    SkillsDevelopmentViewSet,
    basename="skills_development",
)

urlpatterns = [
    path("", include(router_v1.urls)),
]
