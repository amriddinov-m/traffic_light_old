from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from client.models import Client
from client.serializer import ClientListSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects\
        .select_related('entity')\
        .prefetch_related('department', 'department__entity')
    serializer_class = ClientListSerializer
    permission_classes = [AllowAny]
    http_method_names = ['get']
