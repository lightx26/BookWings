from .models import Book

from django import forms
import django_filters
from django_filters.filters import RangeFilter


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'publisher', 'edition', 'be_sold', 'status']


class BookFilterForm(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.ModelChoiceFilter(queryset=Book.tags.all())

    class Meta:
        model = Book
        fields = ['title', 'tags']
