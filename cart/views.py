from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cart, BookInCart
import cart.services as cart_services


# Create your views here.
@login_required
def add_to_cart(request, book_id):
    cart = cart_services.get_cart(request.user)
    cart.add(book_id, 1)
    return HttpResponse("Book added to cart")


@login_required
def view_cart(request):
    cart = cart_services.get_cart(request.user)
    books_in_cart = BookInCart.objects.filter(cart=cart)
    return render(request, 'cart.html', {'books': books_in_cart})
