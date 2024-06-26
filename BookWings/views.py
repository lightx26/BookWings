from django.core.paginator import Paginator
from django.shortcuts import render, redirect
import books.services as books_services
import coupons.services as coupons_services
import delivery.services as delivery_services
from accounts.models import UserRole
from delivery.models import DeliveryStatus


def index(request):
    books = books_services.get_trendy_books()
    coupons = coupons_services.get_new_coupons()
    categories = books_services.get_all_categories()

    paginator = Paginator(books, 8)
    page = request.GET.get('page', 1)

    return render(request, 'home/index.html',
                  {'books': paginator.page(page), 'coupons': coupons, 'categories': categories})


def about(request):
    return render(request, 'home/about.html')
