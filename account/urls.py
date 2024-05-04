from django.urls import path
from .views import *

urlpatterns = [
    path('register/', accountRegister, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', accountLogout, name='logout'),
    path('account/change-password/', accountChangePassword, name='change-password'),
    # path('account/', accountProfile, name='profile'),
    path('account/update-address/', accountUpdateAddress, name='update-address'),
    # path('account/remove-address/', accountRemoveAddress, name='remove-address'),
]