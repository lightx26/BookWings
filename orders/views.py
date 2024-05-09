from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Order, DeliveryInformation, BookInOrder, Shipping


# Create your views here.
@login_required
def prepare_order(request):
    if request.method == 'POST':
        books = request.POST.get('books')
        quantities = request.POST.get('quantity')
        tmp_total = 0
        for book, quantity in zip(books, quantities):
            tmp_total += book.price * quantity

        request.session['prepared_order'] = {
            'books': books,
            'quantities': quantities,
            'total': tmp_total
        }
        return redirect('make_order')

    return render(request, 'prepare_order.html')


@login_required
def make_order(request):
    prepared_order = request.session.pop('prepared_order')
    if request.method == 'POST':
        order = Order.objects.create(
            customer=request.user,
            status=False
        )

        for coupon in request.POST.get('coupon'):
            order.coupon.add(coupon)

        delivery_info = DeliveryInformation.objects.create(
            order=order,
            address=request.POST.get('address'),
            shipping_company=Shipping.objects.get(pk=request.POST.get('shipping_company')),
        )

        delivery_info.delivery_fee = delivery_info.shipping_company.shipping_fee
        delivery_info.save()

        books = prepared_order.get('books')
        quantities = prepared_order.get('quantities')
        for book, quantity in zip(books, quantities):
            BookInOrder.objects.create(
                order=order,
                book=book,
                quantity=quantity
            )

        tmp_total = prepared_order.get('total')
        for coupon in order.coupon.all():
            if coupon.type == 'percentage':
                tmp_total -= tmp_total * coupon.discount / 100
            else:
                tmp_total -= coupon.discount
        order.total = tmp_total + delivery_info.delivery_fee
        order.save()
        return render(request, 'order_success.html')

    return render(request, 'make_order.html')
