from rest_framework import routers

from entity.views import EntityViewSet

router = routers.SimpleRouter()
router.register('api/v1/entity', EntityViewSet)
