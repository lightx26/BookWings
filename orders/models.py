from django.db import models
from books.models import Book
from accounts.models import User as Customer, Address
from coupons.models import Coupon


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coupon = models.ManyToManyField(Coupon)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class Shipping(models.Model):
    shipping_company_name = models.CharField(max_length=255)
    shipping_fee = models.DecimalField(max_digits=10, decimal_places=2)


class DeliveryInformation(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    shipping_company = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    start_delivery_date = models.DateTimeField(auto_now_add=True)
    finish_delivery_date = models.DateTimeField(default=None, null=True)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)


class BookInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
