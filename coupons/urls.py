from django.urls import path
from .views import view_my_coupons

urlpatterns = [
    path('', view_my_coupons, name='view_my_coupons'),
]