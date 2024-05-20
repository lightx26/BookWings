import cart.services as cart_services


def cart_custom_processor(request):
    if not request.user.is_authenticated:
        return {}

    cart = cart_services.get_cart(request.user)
    books_in_cart = cart_services.books_in_cart(cart)
    return {
        'cart': cart,
        'books_in_cart': books_in_cart,
    }
