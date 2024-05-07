from django.urls import path
from .views import *

urlpatterns = [
    path('add-book/', addBook, name='addbook'),
]