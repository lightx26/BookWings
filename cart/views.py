from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Cart, BookInCart
from books.models import Book


# Create your views here.
@login_required
def add_to_cart(request, book_id):
    cart = Cart.objects.get(customer=request.user)
    quantity = request.POST.get('quantity', 1)
    cart.add(book_id, quantity)


@login_required
def view_cart(request):
    cart = Cart.objects.get(customer=request.user)
    books_in_cart = BookInCart.objects.filter(cart=cart)
    return render(request, 'cart.html', {'books': books_in_cart})