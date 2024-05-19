from django.urls import path
from .views import *

urlpatterns = [
    # path('add-book/', addBook, name='addbook'),
    path('', view_cart, name='view_cart'),
    path('add-to-cart/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/', remove_from_cart, name='remove_from_cart'),
    path('update-quantity/', update_quantity, name='update_quantity'),
    path('get-cart-size/', get_cart_size, name='get_cart_size'),
]
