from django.shortcuts import render, redirect

from books.forms import AddBookForm
from books.models import Book


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
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def view_book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    return render(request, 'book_details.html', {'book': book})
