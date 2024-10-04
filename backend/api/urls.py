from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PositionViewSet, TeamViewSet, EmployeeViewSet, RatingViewSet

app_name = "api"

router = DefaultRouter()
router.register("positions", PositionViewSet, basename="positions")
router.register("teams", TeamViewSet, basename="teams")
router.register("employees", EmployeeViewSet, basename="employees")
router.register("raitings", RatingViewSet, basename="raitings")

urlpatterns = [path("", include(router.urls))]
