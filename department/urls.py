from rest_framework import routers

from department.views import DepartamentViewSet

router = routers.SimpleRouter()
router.register('api/v1/departments', DepartamentViewSet)
