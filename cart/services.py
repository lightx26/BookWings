from cart.models import Cart


def get_cart(user):
    return Cart.objects.get(customer=user)


def books_in_cart(cart):
    return cart.bookincart_set.all()
