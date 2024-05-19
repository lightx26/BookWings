from datetime import datetime

from coupons.models import Coupon


def get_coupon_by_id(coupon_id):
    return Coupon.objects.get(pk=coupon_id)


def get_coupon_for_order(customer, order_value):
    for_order_coupons = Coupon.objects.filter(min_order_value__lte=order_value, min_customer_rank__lte=customer.rank)
    o_coupons = for_order_coupons.filter(usage_type='ORDER')
    d_coupons = for_order_coupons.filter(usage_type='DELIVERY')
    return filter_valid_coupons(o_coupons), filter_valid_coupons(d_coupons)


def get_coupon_for_customer(customer):
    for_customer_coupons = Coupon.objects.filter(min_customer_rank__lte=customer.rank)
    return filter_valid_coupons(for_customer_coupons)


# def get_hot_coupons():
#     hot_coupons = Coupon.objects.filter()
#     return filter_valid_coupons(hot_coupons)


def get_new_coupons():
    new_coupons = Coupon.objects.all().order_by('-id')
    return filter_valid_coupons(new_coupons)[:10]


def filter_valid_coupons(coupons):
    valid_coupons = []
    for coupon in coupons.filter(expiration_date__gte=datetime.now()):
        if count_coupon_usage(coupon) < coupon.usage_limit:
            valid_coupons.append(coupon)
    return valid_coupons


def count_coupon_usage(coupon):
    return coupon.order_set.count()
