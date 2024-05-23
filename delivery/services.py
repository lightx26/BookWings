from .models import Shipment, DeliveryStatus, Shipping


def get_shipment_by_id(shipment_id):
    return Shipment.objects.get(id=shipment_id)


def get_shipments(deliverer=None, status=None):
    if deliverer is None:
        return Shipment.objects.filter(status=status)
    if status is None:
        return Shipment.objects.filter(delivery_by=deliverer)

    return Shipment.objects.filter(delivery_by=deliverer, status=status)
