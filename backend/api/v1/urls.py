from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import SkillViewSet, SkillEmployeeViewSet

router_v1 = DefaultRouter()

router_v1.register(
    "skills",
    SkillViewSet,
    basename="skills",
)
router_v1.register(
    r"domains/(?P<domain_id>\d+)/skills/(?P<skill_id>\d+)/employees",
    SkillEmployeeViewSet,
    basename="skill_employee",
)

urlpatterns = [
    path("dashboard/", include(router_v1.urls)),
]
