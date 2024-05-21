from books.models import Book, Category
import orders.services as orders_services


def get_all_books():
    return Book.objects.all().order_by('-id')

def get_book_by_id(book_id):
    return Book.objects.get(pk=book_id)


def get_books_by_title(title):
    return Book.objects.filter(title__icontains=title).order_by('-id')


def get_books_by_filter(input_title="", category=None):
    books = get_books_by_title(input_title).order_by('-id')
    if category is not None:
        books = books.filter(tags=category).order_by('-id')
    return books


def get_trendy_books():
    tmp_orders = orders_services.get_recent_order_by_time(delta_month=3)    # Get orders in the last 3 months
    book_sold = {}
    for order in tmp_orders:
        for book_in_order in order.bookinorder_set.all():
            if book_in_order.book.id in book_sold:
                book_sold[book_in_order.book.id] += book_in_order.quantity
            else:
                book_sold[book_in_order.book.id] = book_in_order.quantity

    trendy_book_ids = sorted(book_sold.items(), key=lambda x: -x[1])[:10]    # Top 10 best-selling books
    return Book.objects.filter(pk__in=[book_id for book_id, _ in trendy_book_ids]).order_by('-id')


def get_all_categories():
    return Category.objects.all().order_by('name')


def get_category_by_id(category_id):
    if category_id is None or category_id == 0:
        return None
    return Category.objects.get(pk=category_id)
