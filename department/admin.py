import datetime

from django.contrib import admin
from django.db.models import Count
from datetime import datetime
from client.models import Client, ClientAddedToDepartmentDate
from department.models import Department


class ClientInline(admin.TabularInline):
    model = Client.department.through
    min_num = 0
    extra = 0


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = 'department_id', 'title', 'show_clients_count',
    inlines = (ClientInline,)

    def save_related(self, request, form, formsets, change):
        for formset in formsets:
            list_comment = formset.save(commit=False)
            for comment in list_comment:
                if comment:
                    ClientAddedToDepartmentDate.objects.get_or_create(client=comment.client,
                                                                      department=comment.department,
                                                                      added_date=datetime.now().today())
        return super().save_related(request, form, formsets, change)

    def show_clients_count(self, obj):
        return obj.clients_count

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.prefetch_related('clients').annotate(clients_count=Count('clients'))
