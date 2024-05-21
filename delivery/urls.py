from django.urls import path
# TODO: Import the views from delivery app
from .views import *

urlpatterns = [
    path('', view_arrived_shipment, name='view_arrived_shipments'),
    path('success', view_success_shipment, name='history_shipments'),
    path('delivering', view_delivering_shipment, name='history_shipments'),
    path('take/<int:shipment_id>', take_shipment, name='take_shipment'),
    path('return/<int:shipment_id>', return_shipment, name='return_shipment'),
    path('complete/<int:shipment_id>', complete_shipment, name='complete_shipment'),
]