from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cart, BookInCart
import cart.services as cart_services


# Create your views here.
@login_required
def add_to_cart(request, book_id):
    cart = cart_services.get_cart(request.user)
    quantity = request.POST.get('quantity', 1)
    cart.add(book_id, quantity)
    return redirect('view_cart')


@login_required
def view_cart(request):
    cart = cart_services.get_cart(request.user)
    books_in_cart = BookInCart.objects.filter(cart=cart)
    return render(request, 'cart.html', {'books': books_in_cart})
