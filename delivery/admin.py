from django.contrib import admin
from delivery.models import Shipping, DeliveryInformation


# Register your models here.
class DeliveryInfoAdmin(admin.ModelAdmin):
    readonly_fields = ['order', 'address', 'shipping_company', 'delivery_by',
                       'start_delivery_date', 'finish_delivery_date', 'delivery_fee']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Shipping)
admin.site.register(DeliveryInformation, DeliveryInfoAdmin)
