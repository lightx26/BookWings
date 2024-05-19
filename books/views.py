from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.core import serializers
from books.models import Book
import books.services as books_services

from django.http import JsonResponse


# Create your views here.

# def addBook(request):
#     if request.method == 'POST':
#         form = AddBookForm(request.POST)
#         if form.is_valid():
#             book = form.save(commit=False)
#             book.be_sold = 0
#             book.save()
#             return redirect('home')
#     else:
#         form = AddBookForm()
#     context = {'form': form}
#     return render(request, 'add_book.html', context)


def view_books(request):
    books = books_services.get_all_books()
    paginator = Paginator(books, 15)
    page = request.GET.get('page', 1)
    # books_json = serializers.serialize("json", books)
    return render(request, 'books.html', {'books': paginator.page(page)})


def view_books_by_filter(request):
    input_title = request.GET.get('search', '').strip()
    category_id = int(request.GET.get('category', 0))
    category = books_services.get_category_by_id(category_id)

    books = books_services.get_books_by_filter(input_title, category)
    categories = books_services.get_all_categories()

    paginator = Paginator(books, 15)
    page = request.GET.get('page', 1)

    return render(request, 'books/books.html',
                  {
                      'books': paginator.page(page),
                      'categories': categories,
                      'input_title': input_title,
                      'category_id': category_id,
                  })


def view_books_by_category(request):
    input_title = request.GET.get('search', '').strip()
    category_id = int(request.GET.get('category', 0))
    category = books_services.get_category_by_id(category_id)

    books = books_services.get_books_by_filter(input_title, category)
    categories = books_services.get_all_categories()

    paginator = Paginator(books, 15)
    page = request.GET.get('page', 1)

    return JsonResponse({
        'books': serializers.serialize("json", paginator.page(page)),
        'categories': serializers.serialize("json", categories),
        'category_id': category
    })


def view_book_details(request, book_id, book_slug):
    book = books_services.get_book_by_id(book_id)
    if book_slug != book.slug:
        return redirect('view_book_details', book_id=book_id, book_slug=book.slug, APPEND_SLASH=False)
    return render(request, 'books/book_details.html', {'book': book})
