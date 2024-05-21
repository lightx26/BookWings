from delivery.models import Shipping, DeliveryStatus
from orders.models import Order
from datetime import date
from dateutil.relativedelta import relativedelta


def get_all_shipping_companies():
    return Shipping.objects.all()


def get_shipping_company_by_id(shipping_id):
    return Shipping.objects.get(pk=shipping_id)


def get_order_by_id(order_id):
    return Order.objects.get(pk=order_id)


def get_orders_by_customer(customer, status=None):
    if status:
        return Order.objects.filter(customer=customer, status=status)
    return Order.objects.filter(customer=customer)


def get_delivered_orders(customer):
    orders = get_orders_by_customer(customer).order_by('-date_ordered')
    delivered_orders = []
    for order in orders:
        if order.delivery_info == DeliveryStatus.DELIVERED:
            delivered_orders.append(order)
    return delivered_orders


def get_not_delivered_orders(customer):
    orders = get_orders_by_customer(customer).order_by('-date_ordered')
    delivering_orders = []
    for order in orders:
        if order.delivery_info != DeliveryStatus.DELIVERED:
            delivering_orders.append(order)
    return delivering_orders


def get_recent_orders(num_orders):
    return Order.objects.order_by('-date_ordered')[:num_orders]


def get_orders_in_time(from_date, to_date):
    return Order.objects.filter(date_ordered__range=[from_date, to_date])


def get_recent_order_by_time(delta_month):
    return get_orders_in_time(date.today() - relativedelta(months=delta_month), date.today())


def create_order(customer, total):
    return Order.objects.create(customer=customer, total=total)


def save_order(order):
    order.save()
    return order
