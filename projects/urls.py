from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet,EmployeeProjectViewSet

router = DefaultRouter()
router.register("projects",ProjectViewSet)
router.register("employee-projects",EmployeeProjectViewSet)

urlpatterns = router.urls