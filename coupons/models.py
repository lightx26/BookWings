from django.db import models


# Create your models here.
# class CouponType(models.Model):
#     type_name = models.CharField(max_length=20)


class Coupon(models.Model):
    class CouponType(models.TextChoices):
        PERCENTAGE = 'PERCENTAGE'
        FIXED = 'FIXED'

    class UsageType(models.TextChoices):
        ORDER = 'ORDER'
        DELIVERY = 'DELIVERY'

    code = models.CharField(max_length=20, unique=True)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=20, choices=CouponType.choices)
    usage_type = models.CharField(max_length=20, choices=UsageType.choices)
    usage_limit = models.IntegerField()
    is_expired = models.BooleanField(default=False)
    minimum_order_value = models.DecimalField(max_digits=10, decimal_places=2)
