from accounts.models import Address


def get_addresses_by_user(user):
    return Address.objects.filter(user=user)


def get_address_by_id(address_id):
    return Address.objects.get(pk=address_id)