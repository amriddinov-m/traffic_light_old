from rest_framework import serializers

from department.models import Department
from entity.serializer import EntityListSerializer


class DepartmentListSerializer(serializers.ModelSerializer):
    """Список департаментов"""
    entity = EntityListSerializer()

    class Meta:
        model = Department
        fields = '__all__'
