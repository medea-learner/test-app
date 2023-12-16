from django.contrib import admin

from .models import Role

class RoleAdminView(admin.ModelAdmin):
    exclude = ('users',)

admin.site.register(Role, RoleAdminView)
