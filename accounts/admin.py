from django.contrib import admin
from .models import User, Address


# Register your models here.
class ViewOnlyAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(User, ViewOnlyAdmin)
admin.site.register(Address, ViewOnlyAdmin)
