from rest_framework import serializers

from client.models import Client
from department.serializer import DepartmentListSerializer
from entity.serializer import EntityListSerializer


class ClientListSerializer(serializers.ModelSerializer):
    """Список клиентов"""

    department = DepartmentListSerializer(many=True)
    entity = EntityListSerializer()

    class Meta:
        model = Client
        fields = '__all__'
