from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import coupons.services as coupon_services


# Create your views here.
@login_required
def view_my_coupons(request):
    available_coupons = coupon_services.get_available_coupons()
    return render(request, 'coupons/my_coupons.html', {'coupons': available_coupons})
