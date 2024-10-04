from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PositionViewSet,
    TeamViewSet,
    EmployeeViewSet,
    RatingViewSet,
    SkillViewSet,
    CompetenceViewSet,
    DomainViewSet,
)

app_name = "api"

router = DefaultRouter()
router.register("positions", PositionViewSet, basename="positions")
router.register("teams", TeamViewSet, basename="teams")
router.register("employees", EmployeeViewSet, basename="employees")
router.register("domains", DomainViewSet, basename="domains")
router.register("skills", SkillViewSet, basename="skills")
router.register("competences", CompetenceViewSet, basename="competences")
router.register("raitings", RatingViewSet, basename="raitings")

urlpatterns = [path("", include(router.urls))]
