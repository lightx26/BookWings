from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from accounts.models import Address
from coupons.models import CouponType
from delivery.models import Shipping

import orders.services as order_services
import coupons.services as coupon_services
import accounts.services as accounts_services
import books.services as books_services
import cart.services as cart_services


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
        try:
            shipping_company = order_services.get_shipping_company_by_id(request.POST.get('shipping_company'))
        except Shipping.DoesNotExist:
            # TODO: Redirect to error page
            return redirect('home')

        try:
            address = accounts_services.get_address_by_id(request.POST.get('address'))
        except Address.DoesNotExist:
            return redirect('update-address')

        delivery_info = order.set_delivery_info(address, shipping_company, shipping_company.shipping_fee)

        # Add products to order
        book_ids = prepared_order.get('books')
        quantities = prepared_order.get('quantities')
        for book_id, quantity in zip(book_ids, quantities):
            book = books_services.get_book_by_id(book_id)
            order.add_product(book, quantity)

        # Calculate total price
        tmp_total = Decimal(prepared_order.get('total'))
        for coupon in order.coupon.all():
            if coupon.type == CouponType.PERCENTAGE:
                tmp_total -= min(tmp_total * coupon.discount / 100, coupon.max_discount)
            elif coupon.type == CouponType.FIXED:
                tmp_total -= coupon.discount
        order.total = delivery_info.delivery_fee + tmp_total

        # Save order
        order_services.save_order(order)
        # return render(request, 'order_success.html')

        # Remove books from cart
        cart_services.get_cart(request.user).remove(book_ids)

        # Check for rank promotion
        accounts_services.rank_up(request.user)

        # Clear unused session after processing
        request.session.pop('prepared_order')

        return redirect('home')

    addresses = accounts_services.get_addresses_by_user(request.user)
    shipping_companies = order_services.get_all_shipping_companies()
    o_coupons, d_coupons = coupon_services.get_coupon_for_order(request.user, prepared_order.get('total'))

    return render(request, 'make_order.html',
                  {'prepared_order': prepared_order,
                   'addresses': addresses,
                   'shipping_companies': shipping_companies,
                   'order_coupons': o_coupons,
                   'delivery_coupons': d_coupons,})

# @login_required
# def payment(request, order_id):
#     order = order_services.get_order_by_id(order_id)
#     if request.method == 'POST':
#         order.status = 'PAID'
#         order.save()
#         return redirect('home')
#     return render(request, 'payment.html', {'order': order})
