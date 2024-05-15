from django.urls import path
from .views import *

urlpatterns = [
    path('register/', accountRegister, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('accounts/profile', view_profile, name='profile'),
    path('accounts/change-password/', change_password, name='change-password'),
    path('accounts/address', view_addresses, name='address'),
    path('accounts/update-address/', update_address, name='update-address'),
    path('accounts/remove-address/', remove_address, name='remove-address'),
]