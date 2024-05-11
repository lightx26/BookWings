from django.core.paginator import Paginator
from django.shortcuts import render
from django.core import serializers
from books.models import Book
import books.services as books_services


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
    # category = books_services.get_category_by_id(request.GET.get('category', None))
    books = books_services.get_books_by_filter(input_title)
    paginator = Paginator(books, 15)
    page = request.GET.get('page', 1)

    return render(request, 'books.html',
                  {
                      'books': paginator.page(page),
                      'input_title': input_title,
                  })


def view_book_details(request, book_id):
    book = books_services.get_book_by_id(book_id)
    return render(request, 'book_details.html', {'book': book})
