from django import forms
from .models import Book


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publisher', 'edition', 'be_sold', 'status']