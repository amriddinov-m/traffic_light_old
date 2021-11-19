from django.contrib import admin
from tabbed_admin import TabbedModelAdmin
from client.models import Client, ClientExtraPhone, VK, FB, ClientAddedToDepartmentDate


class ClientExtraPhoneInline(admin.TabularInline):
    model = ClientExtraPhone
    min_num = 0
    extra = 0


class VKInline(admin.TabularInline):
    model = VK
    min_num = 0
    extra = 0


class FBInline(admin.TabularInline):
    model = FB
    min_num = 0
    extra = 0


@admin.register(Client)
class ClientAdmin(TabbedModelAdmin):
    list_display = 'client_id', 'get_full_name', 'phone', 'created_at'
    list_filter = 'status',
    search_fields = 'first_name', 'surname', 'patronymic'

    first_tab = (
        (None, {
            'fields': ('first_name', 'surname', 'patronymic'),
        }),
    )
    second_tab = (
        (None, {
            'fields': ('phone',),
        }),
        ClientExtraPhoneInline,
    )
    third_tab = (
        (None, {
            'fields': ('status', '_type', 'sex', 'timezone'),
        }),
    )
    fourth_tab = (
        (None, {
            'fields': ('entity', 'department')
        }),
    )
    fifth_tab = (
        (None, {
            'fields': ('ok', 'instagram', 'telegram', 'whatsapp', 'viber'),
        }),
        VKInline,
        FBInline,
    )
    tabs = [
        ('Основная информация', first_tab),
        ('Номер телефона', second_tab),
        ('Характеристики', third_tab),
        ('Организация', fourth_tab),
        ('Соц сети', fifth_tab),
    ]


@admin.register(ClientAddedToDepartmentDate)
class ClientAddedToDepartmentDateAdmin(admin.ModelAdmin):
    pass
