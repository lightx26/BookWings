from django.db import models
from books.models import Book
from accounts.models import User as Customer, Address
from coupons.models import Coupon
from django.utils.module_loading import import_string


# Create your models here.
class Order(models.Model):
    # Relationships
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    coupon = models.ManyToManyField(Coupon)

    # Attributes
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def set_delivery_info(self, address, shipping_company, delivery_fee):
        DeliveryInformation = import_string('delivery.models.DeliveryInformation')
        return DeliveryInformation.objects.create(order=self,
                                                  address=address,
                                                  shipping_company=shipping_company,
                                                  delivery_fee=delivery_fee,
                                                  status='PREPARING')

    def add_product(self, book, quantity):
        return BookInOrder.objects.create(order=self, book=book, quantity=quantity)

    def __str__(self):
        return f'Order {self.id}'


class BookInOrder(models.Model):
    # Relationships
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    # Attributes
    quantity = models.IntegerField()
