from django.db import models
from accounts.models import User as Customer
from books.models import Book


# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def add(self, book, add_quantity):
        if BookInCart.objects.filter(cart=self, book=book).exists():
            book_in_cart = BookInCart.objects.get(cart=self, book=book)
            book_in_cart.quantity += add_quantity
            book_in_cart.save()
        else:
            book_in_cart = BookInCart(cart=self, book=book, quantity=add_quantity)
            book_in_cart.save()


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
