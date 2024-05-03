from django.urls import path
from .views import register, UserLoginView
from .views import register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]