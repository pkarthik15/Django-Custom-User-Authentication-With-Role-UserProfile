from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from accounts.models import User, Role, UserProfile


admin.site.site_header = 'My Application'
admin.site.site_title = "My Application"
admin.site.index_title = "Welcome"



class UserAdmin(BaseUserAdmin):
    
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'last_login')
    list_filter = ('is_staff', )
    fieldsets = (
        ('Login Details', {'fields': ('email', 'password')}),
        ('Personal Details', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes' : ('wide',),
                'fields' : (
                    'email', 'first_name', 'last_name', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser'
                )
            }
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', 'first_name', 'last_name', 'date_joined')

admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(UserProfile)
admin.site.unregister(Group)


