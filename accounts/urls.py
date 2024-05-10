from django.urls import path
from .views import *

urlpatterns = [
    path('register/', accountRegister, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
    path('accounts/change-password/', change_password, name='change-password'),
    # path('accounts/', accountProfile, name='profile'),
    path('accounts/update-address/', update_address, name='update-address'),
    path('accounts/remove-address/', remove_address, name='remove-address'),
    # path('accounts/remove-address/', accountRemoveAddress, name='remove-address'),
]