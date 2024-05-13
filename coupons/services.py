from datetime import datetime

from coupons.models import Coupon


def get_coupon_by_id(coupon_id):
    return Coupon.objects.get(pk=coupon_id)


def count_coupon_usage(coupon):
    # coupon = get_coupon_by_id(coupon_id)
    return coupon.order_set.count()


def get_coupon_for_order(customer, order_value):
    coupons = Coupon.objects.filter(min_order_value__lte=order_value, min_customer_rank__lte=customer.rank,
                                    expiration_date__gte=datetime.now(),
                                    usage_type='ORDER')
    valid_coupons = []
    for coupon in coupons:
        if count_coupon_usage(coupon) < coupon.usage_limit:
            valid_coupons.append(coupon)
    return valid_coupons


def get_available_coupons():
    for_value_coupons = Coupon.objects.filter(is_expired=False)

    valid_coupons = []
    for coupon in for_value_coupons:
        if count_coupon_usage(coupon) < coupon.usage_limit:
            valid_coupons.append(coupon)
    return valid_coupons
