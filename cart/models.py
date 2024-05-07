from django.db import models
from accounts.models import User as Customer
from books.models import Book


# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
