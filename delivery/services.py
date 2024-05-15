from .models import DeliveryInformation, DeliveryStatus, Shipping


def get_shipment_by_id(shipment_id):
    return DeliveryInformation.objects.get(id=shipment_id)


def get_shipments(deliverer=None, status=None):
    if deliverer is None:
        return DeliveryInformation.objects.filter(status=status)
    if status is None:
        return DeliveryInformation.objects.filter(delivery_by=deliverer)

    return DeliveryInformation.objects.filter(delivery_by=deliverer, status=status)
