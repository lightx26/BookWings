from django.contrib import admin
from orders.models import Order
from accounts.admin import ViewOnlyAdmin


# Register your models here.
class OrderAdmin(ViewOnlyAdmin):
    list_filter = ['date_ordered']
    search_fields = ['customer__phone_number', 'customer__email']


admin.site.register(Order, OrderAdmin)
