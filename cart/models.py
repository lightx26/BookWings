from django.db import models
from accounts.models import User as Customer
from books.models import Book


# Create your models here.
class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def add(self, book_id, add_quantity):
        book = Book.objects.get(pk=book_id)
        if BookInCart.objects.filter(cart=self, book=book).exists():
            book_in_cart = BookInCart.objects.get(cart=self, book=book)
            book_in_cart.quantity += add_quantity
            book_in_cart.save()
        else:
            book_in_cart = BookInCart(cart=self, book=book, quantity=add_quantity)
            book_in_cart.save()

    def remove(self, book_id):
        book = Book.objects.get(pk=book_id)
        if BookInCart.objects.filter(cart=self, book=book).exists():
            book_in_cart = BookInCart.objects.get(cart=self, book=book)
            book_in_cart.delete()

    def decrease(self, book_id):
        book = Book.objects.get(pk=book_id)
        if BookInCart.objects.filter(cart=self, book=book).exists():
            book_in_cart = BookInCart.objects.get(cart=self, book=book)
            book_in_cart.quantity -= 1

            if book_in_cart.quantity == 0:
                book_in_cart.delete()
            else:
                book_in_cart.save()

    def total(self):
        total = 0
        books_in_cart = BookInCart.objects.filter(cart=self)
        for book_in_cart in books_in_cart:
            total += book_in_cart.book.price * book_in_cart.quantity
        return total


class BookInCart(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
