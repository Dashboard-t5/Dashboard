from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CompetenceViewSet, DomainViewSet, EmployeeViewSet,
                    PositionViewSet, RatingViewSet, SkillViewSet,
                    SuitabilityPositionViewSet, TeamViewSet)

app_name = "api"

router = DefaultRouter()
router.register("positions", PositionViewSet, basename="positions")
router.register("teams", TeamViewSet, basename="teams")
router.register("employees", EmployeeViewSet, basename="employees")
router.register("domains", DomainViewSet, basename="domains")
router.register("skills", SkillViewSet, basename="skills")
router.register("competences", CompetenceViewSet, basename="competences")
router.register("raitings", RatingViewSet, basename="raitings")
router.register(
    "dashboard/suitability_position",
    SuitabilityPositionViewSet,
    basename="suitability_position"
)

urlpatterns = [path("", include(router.urls))]
