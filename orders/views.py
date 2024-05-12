from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.models import Address
from books.models import Book
from coupons.models import Coupon
from .models import Order, DeliveryInformation, BookInOrder, Shipping

import orders.services as order_services
import coupons.services as coupon_services
import accounts.services as accounts_services
import books.services as books_services


# Create your views here.
@login_required
def prepare_order(request):
    if request.method == 'POST':
        books = request.POST.getlist('books[]')
        quantities = request.POST.getlist('quantities[]')

        tmp_total = 0
        for book_id, quantity in zip(books, quantities):
            book = books_services.get_book_by_id(book_id)
            tmp_total += book.price * int(quantity)

        request.session['prepared_order'] = {
            'books': books,
            'quantities': quantities,
            'total': float(tmp_total)
        }
        return redirect('make_order')
    return redirect('view_cart')


@login_required
def make_order(request):
    prepared_order = request.session.get('prepared_order')
    if request.method == 'POST':
        # Create initial order
        order = order_services.create_order(request.user, prepared_order.get('total'))

        # Add applied coupons to order
        for coupon_id in request.POST.getlist('coupons[]'):
            order.coupon.add(coupon_services.get_coupon_by_id(coupon_id))

        # Set delivery information
        shipping_company = order_services.get_shipping_company_by_id(request.POST.get('shipping_company'))
        delivery_info = order.set_delivery_info(Address.objects.get(pk=request.POST.get('address')),
                                                shipping_company,
                                                shipping_company.shipping_fee)

        # Add products to order
        books = prepared_order.get('books')
        quantities = prepared_order.get('quantities')
        for book_id, quantity in zip(books, quantities):
            book = books_services.get_book_by_id(book_id)
            order.add_product(book, quantity)

        # Calculate total price
        tmp_total = Decimal(prepared_order.get('total'))
        for coupon in order.coupon.all():
            if coupon.type == 'PERCENTAGE':
                tmp_total -= tmp_total * coupon.discount / 100
            else:
                tmp_total -= coupon.discount
        order.total = delivery_info.delivery_fee + tmp_total

        # Save order
        order_services.save_order(order)
        # return render(request, 'order_success.html')
        request.session.pop('prepared_order')
        return redirect('home')

    addresses = accounts_services.get_addresses_by_user(request.user)
    shipping_companies = order_services.get_all_shipping_companies()
    coupons = coupon_services.get_coupon_for_order(prepared_order.get('total'))

    return render(request, 'make_order.html',
                  {'prepared_order': prepared_order,
                   'addresses': addresses,
                   'shipping_companies': shipping_companies,
                   'coupons': coupons})


# @login_required
# def payment(request, order_id):
#     order = order_services.get_order_by_id(order_id)
#     if request.method == 'POST':
#         order.status = 'PAID'
#         order.save()
#         return redirect('home')
#     return render(request, 'payment.html', {'order': order})
