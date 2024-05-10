from django.urls import path
from .views import *

urlpatterns = [
    path('register/', accountRegister, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', accountLogout, name='logout'),
    path('accounts/change-password/', accountChangePassword, name='change-password'),
    # path('accounts/', accountProfile, name='profile'),
    path('accounts/update-address/', accountUpdateAddress, name='update-address'),
    path('accounts/remove-address/', remove_address, name='remove-address'),
    # path('accounts/remove-address/', accountRemoveAddress, name='remove-address'),
]