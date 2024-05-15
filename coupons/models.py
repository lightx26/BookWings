from django.db import models

from accounts.models import CustomerRank


# Create your models here.
# class CouponType(models.Model):
#     type_name = models.CharField(max_length=20)
class CouponType(models.TextChoices):
    PERCENTAGE = 'PERCENTAGE'
    FIXED = 'FIXED'


class UsageType(models.TextChoices):
    ORDER = 'ORDER'
    DELIVERY = 'DELIVERY'


class Coupon(models.Model):
    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    max_discount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=CouponType.choices)
    usage_type = models.CharField(max_length=20, choices=UsageType.choices)
    usage_limit = models.IntegerField()
    expiration_date = models.DateField()
    min_order_value = models.DecimalField(max_digits=10, decimal_places=2)
    min_customer_rank = models.IntegerField(choices=CustomerRank.choices, default=CustomerRank.BRONZE)

    def __str__(self):
        return self.code
