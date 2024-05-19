from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cart, BookInCart
import cart.services as cart_services
from django.http import JsonResponse

# Create your views here.
@login_required
def add_to_cart(request):
    book_id = request.POST.get('book_id')
    cart = cart_services.get_cart(request.user)
    cart.add(book_id, 1)
    # return HttpResponse("Book added to cart")
    return JsonResponse({'status': 'success'})


@login_required
def view_cart(request):
    cart = cart_services.get_cart(request.user)
    books_in_cart = BookInCart.objects.filter(cart=cart)
    return render(request, 'cart.html', {'books': books_in_cart})

@login_required
def remove_from_cart(request):
    if request.method != 'POST':
        return redirect('view_cart')
    
    book_id = request.POST.get('book_id')
    cart = cart_services.get_cart(request.user)
    cart.remove(book_id)
    return redirect('view_cart')

@login_required
def update_quantity(request):
    if request.method != 'POST':
        return JsonResponse({'status': 'error'})
    
    book_id = request.POST.get('book_id')
    quantity = request.POST.get('quantity')
    cart = cart_services.get_cart(request.user)
    cart.update_quantity(book_id, quantity)
    return JsonResponse({'status': 'success'})

@login_required
def get_cart_size(request):
    cart = cart_services.get_cart(request.user)
    books_in_cart = BookInCart.objects.filter(cart=cart)
    count = 0
    for book in books_in_cart:
        count += book.quantity
        
    return HttpResponse(count)