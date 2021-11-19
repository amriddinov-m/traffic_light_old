from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from entity.models import Entity
from entity.serializer import EntityListSerializer


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntityListSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']
