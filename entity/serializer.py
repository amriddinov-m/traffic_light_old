from rest_framework import serializers

from entity.models import Entity


class EntityListSerializer(serializers.ModelSerializer):
    """Список юридических лиц"""

    class Meta:
        model = Entity
        fields = '__all__'
