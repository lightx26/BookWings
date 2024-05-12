from orders.models import Shipping, Order, OrderStatus


def get_all_shipping_companies():
    return Shipping.objects.all()


def get_shipping_company_by_id(shipping_id):
    return Shipping.objects.get(pk=shipping_id)


def get_order_by_id(order_id):
    return Order.objects.get(pk=order_id)


def get_orders_by_customer(customer):
    return Order.objects.filter(customer=customer)


def create_order(customer, total):
    return Order.objects.create(customer=customer,
                                total=total,
                                status=OrderStatus.PREPARING)


def save_order(order):
    order.save()
    return order
