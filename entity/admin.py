from django.contrib import admin

from entity.models import Entity


@admin.register(Entity)
class EntityAdmin(admin.ModelAdmin):
    list_display = 'entity_id', 'full_name', 'created_at'
