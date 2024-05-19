from cart.models import Cart


def get_cart(user):
    return Cart.objects.get(customer=user)


