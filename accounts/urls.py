from django.urls import path
from .views import *

urlpatterns = [
    path('register/', accountRegister, name='register'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('accounts/profile', view_profile, name='profile'),
    path('accounts/change-password/', change_password, name='change-password'),
    path('accounts/address', view_addresses, name='address'),
    path('accounts/update-address/', update_address, name='update-address'),
    path('accounts/remove-address/<int:addr_id>', remove_address, name='remove-address'),
]