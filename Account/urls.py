from django.urls import path
from .views import *

urlpatterns = [
    path('register/', accountRegister, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', accountLogout, name='logout'),
    path('Account/change-password/', accountChangePassword, name='change-password'),
    # path('Account/', accountProfile, name='profile'),
    path('Account/update-address/', accountUpdateAddress, name='update-address'),
    # path('Account/remove-address/', accountRemoveAddress, name='remove-address'),
]