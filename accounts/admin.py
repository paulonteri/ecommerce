from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Address


class UserAdmin(UserAdmin):
    # Display
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_admin',)}),
    )

    # Create User
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'is_admin',)}),
    )

    # List display
    list_display = ('username', 'email', 'is_active', 'is_admin', 'is_staff',)
    list_filter = ('is_admin', 'is_active', 'is_superuser', 'is_staff',)

    search_fields = ('username', 'email',)
    ordering = ('username', 'email',)


admin.site.register(User, UserAdmin)

admin.site.register(Address)
