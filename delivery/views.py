from datetime import datetime

from django.shortcuts import render, redirect
from accounts.models import UserRole
from accounts.decorators import role_required
from .models import DeliveryInformation, DeliveryStatus
import delivery.services as delivery_services


# Create your views here.
@role_required([UserRole.ADMIN, UserRole.DELIVERER])
def view_arrived_shipment(request):
    shipments = delivery_services.get_shipments(status=DeliveryStatus.ARRIVED)
    return render(request, 'arrived_deliveries.html', context={'shipments': shipments})


@role_required([UserRole.DELIVERER])
def view_success_shipment(request):
    shipments = delivery_services.get_shipments(deliverer=request.user, status=DeliveryStatus.DELIVERED)
    return render(request, 'shipments/delivered.html', context={'shipments': shipments})


@role_required([UserRole.DELIVERER])
def view_delivering_shipment(request):
    shipments = delivery_services.get_shipments(deliverer=request.user, status=DeliveryStatus.DELIVERING)
    return render(request, 'shipment/delivering.html', context={'shipments': shipments})


@role_required([UserRole.DELIVERER])
def take_shipment(request, shipment_id):
    shipment = delivery_services.get_shipment_by_id(shipment_id)
    if shipment.status == DeliveryStatus.ARRIVED:
        shipment.status = DeliveryStatus.DELIVERING
        shipment.delivery_by = request.user
        shipment.save()

    return redirect('view_arrived_shipments')
    # return render(request, 'shipment_taken.html', context={'shipment': shipment})


def return_shipment(request, shipment_id):
    shipment = DeliveryInformation.objects.get(id=shipment_id)
    if shipment.status == DeliveryStatus.DELIVERING:
        shipment.status = DeliveryStatus.ARRIVED
        shipment.delivery_by = None
        shipment.save()

    return redirect('history_shipments')
    # return render(request, 'shipment_returned.html', context={'shipment': shipment}


@role_required([UserRole.DELIVERER])
def complete_shipment(request, shipment_id):
    shipment = DeliveryInformation.objects.get(id=shipment_id)
    if shipment.status == DeliveryStatus.DELIVERING:
        shipment.status = DeliveryStatus.DELIVERED
        shipment.finish_delivery_date = datetime.now()
        shipment.save()

    return redirect('history_shipments')
    # return render(request, 'shipment_delivered.html', context={'shipment': shipment})
