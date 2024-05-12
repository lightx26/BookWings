from books.models import Book, Category


def get_all_books():
    return Book.objects.all()


def get_book_by_id(book_id):
    return Book.objects.get(pk=book_id)


def get_books_by_title(title):
    return Book.objects.filter(title__icontains=title)


def get_books_by_filter(input_title="", category=None):
    books = get_books_by_title(input_title)
    if category is not None:
        books = books.filter(tags=category)
    return books


def get_all_categories():
    return Category.objects.all()


def get_category_by_id(category_id):
    if category_id is None or category_id == 0:
        return None
    return Category.objects.get(pk=category_id)
