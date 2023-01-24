from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_employee')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'is_employee')
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_employee')
    exclude = ('password',)
    readonly_fields = ('last_login', 'date_joined')
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ['is_employee']
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
