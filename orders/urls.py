from django.urls import path
from .views import *

urlpatterns = [
    path('', view_orders, name='view_orders'),
    path('delivered/', view_delivered_orders, name='view_delivered_orders'),
    path('delivering/', view_delivering_orders, name='view_delivering_orders'),
    path('prepare-order/', prepare_order, name='prepare_order'),
    path('make-order/', make_order, name='make_order'),
]
