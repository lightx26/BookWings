from books.models import Book


def get_all_books():
    return Book.objects.all()


def get_book_by_id(book_id):
    return Book.objects.get(pk=book_id)
