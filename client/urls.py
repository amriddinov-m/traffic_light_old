from rest_framework import routers

from client.views import ClientViewSet

router = routers.SimpleRouter()
router.register('api/v1/clients', ClientViewSet)
