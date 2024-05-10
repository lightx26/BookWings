from django.urls import path
from .views import *

urlpatterns = [
    # path('add-book/', addBook, name='addbook'),
    path('prepare-order/', prepare_order, name='prepare_order'),
    path('make-order/', make_order, name='make_order'),
]
