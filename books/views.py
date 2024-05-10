from django.shortcuts import render, redirect

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
    return render(request, 'books.html',
                  {
                      'books': books,
                      'count': books.count()
                  })


def view_book_details(request, book_id):
    book = books_services.get_book_by_id(book_id)
    return render(request, 'book_details.html', {'book': book})
