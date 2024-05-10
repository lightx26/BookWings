from orders.models import Shipping, Order


def get_all_shipping_companies():
    return Shipping.objects.all()


def get_shipping_company_by_id(shipping_id):
    return Shipping.objects.get(pk=shipping_id)


def create_order(customer, total):
    return Order.objects.create(customer=customer,
                                total=total,
                                status=False)


def save_order(order):
    order.save()
    return order
