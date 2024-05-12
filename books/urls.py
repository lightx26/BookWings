from django.urls import path
from .views import *

urlpatterns = [
    # path('add-book/', addBook, name='addbook'),
    path('', view_books_by_filter, name='view_books'),
    path('<int:book_id>/<slug:book_slug>/', view_book_details, name='view_book_details'),
]
