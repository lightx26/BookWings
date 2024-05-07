from django.shortcuts import render, redirect

from books.forms import AddBookForm


# Create your views here.

def addBook(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.be_sold = 0
            book.save()
            return redirect('home')
    else:
        form = AddBookForm()
    context = {'form': form}
    return render(request, 'add_book.html', context)
