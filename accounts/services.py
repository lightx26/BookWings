from accounts.models import Address, User, CustomerRank, CustomerRankConditions
import orders.services as order_services


def get_addresses_by_user(user):
    return Address.objects.filter(user=user)


def get_address_by_id(address_id):
    return Address.objects.get(pk=address_id)


def check_rank_up(customer):
    """
    Check if the customer is eligible for a rank up
    :param customer
    :return: the rank that the customer should be promoted to
    """
    if customer.rank == CustomerRank.DIAMOND:
        return CustomerRank.DIAMOND

    orders = order_services.get_orders_by_customer(customer)

    total_spent = 0
    for order in orders:
        if order.deliveryinformation.status == 'COMPLETED':
            total_spent += order.total

    for rank in range(CustomerRank.DIAMOND, customer.rank, -1):
        if (total_spent >= CustomerRankConditions.RANK_SPENT_CONDITIONS[rank]
                and orders.count() >= CustomerRankConditions.RANK_ORDER_CONDITIONS[rank]):
            return rank

    return customer.rank


def rank_up(customer):
    if customer.rank < CustomerRank.DIAMOND:
        customer.rank = check_rank_up(customer)
    customer.save()
    return customer.rank

# def rank_up(customer):
#     if customer.rank < CustomerRank.DIAMOND:
#         customer.rank += 1
#     customer.save()
#     return customer.rank
#
#
# def rank_down(customer):
#     if customer.rank > CustomerRank.BRONZE:
#         customer.rank -= 1
#     customer.save()
#     return customer.rank
