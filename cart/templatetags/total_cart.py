from django import template

register = template.Library()


@register.filter
def subtotal_cart(cart_items):
    total = 0
    for item in cart_items:
        total += item.book.price * item.quantity
    return total
