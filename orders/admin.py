from django.contrib import admin
from orders.models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total', 'date_ordered']
    list_filter = ['date_ordered']
    search_fields = ['customer__phone', 'customer__email']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Order, OrderAdmin)
