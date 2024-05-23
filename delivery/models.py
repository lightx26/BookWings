from django.db import models
from accounts.models import Address
from orders.models import Order


# Create your models here.
class Shipping(models.Model):
    shipping_company_name = models.CharField(max_length=255)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.shipping_company_name

    class Meta:
        verbose_name = 'Shipping company'
        verbose_name_plural = 'Shipping companies'


class DeliveryStatus(models.TextChoices):
    PREPARING = 'PREPARING', 'Preparing'
    IN_TRANSIT = 'IN_TRANSIT', 'In transit'
    ARRIVED = 'ARRIVED', 'Arrived'
    DELIVERING = 'DELIVERING', 'Delivering'
    DELIVERED = 'DELIVERED', 'Delivered'


class Shipment(models.Model):
    # Relationships
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    shipping_company = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    delivery_by = models.ForeignKey('accounts.User', on_delete=models.SET_NULL, null=True)

    # Attributes
    start_delivery_date = models.DateTimeField(auto_now_add=True)
    finish_delivery_date = models.DateTimeField(default=None, null=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=DeliveryStatus.choices, default=DeliveryStatus.PREPARING)

    def __str__(self):
        return f'Delivery for order {self.order.id}'
