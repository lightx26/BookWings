from django.contrib import admin

from accounts.admin import ViewOnlyAdmin
from delivery.models import Shipping, DeliveryInformation


# Register your models here.
class DeliveryInfoAdmin(ViewOnlyAdmin):
    readonly_fields = ['order', 'address', 'shipping_company', 'delivery_by',
                       'start_delivery_date', 'finish_delivery_date', 'delivery_fee']

    def has_change_permission(self, request, obj=None):
        return True


admin.site.register(Shipping)
admin.site.register(DeliveryInformation, DeliveryInfoAdmin)
