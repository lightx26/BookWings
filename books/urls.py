from django.urls import path
from .views import *

urlpatterns = [
    # path('add-book/', addBook, name='addbook'),
    path('', view_books, name='books'),
    path('<int:book_id>/', view_book_details, name='view_book_details')
]
