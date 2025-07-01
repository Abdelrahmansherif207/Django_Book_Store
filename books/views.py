from django.shortcuts import render, redirect
from django.http import Http404


BOOKS = []
BOOK_ID_COUNTER = 1

class Book:
    def __init__(self, title, author, description):
        global BOOK_ID_COUNTER
        self.id = BOOK_ID_COUNTER
        BOOK_ID_COUNTER += 1
        self.title = title
        self.author = author
        self.description = description

def book_list(request):
    return render(request, 'books/book_list.html', {'books': BOOKS})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        book = Book(title, author, description)
        BOOKS.append(book)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

def book_detail(request, book_id):
    book = next((b for b in BOOKS if b.id == book_id), None)
    if not book:
        raise Http404('Book not found')
    return render(request, 'books/book_detail.html', {'book': book})

def book_edit(request, book_id):
    book = next((b for b in BOOKS if b.id == book_id), None)
    if not book:
        raise Http404('Book not found')
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        return redirect('book_detail', book_id=book.id)
    return render(request, 'books/book_form.html', {'book': book})

def book_delete(request, book_id):
    global BOOKS
    book = next((b for b in BOOKS if b.id == book_id), None)
    if not book:
        raise Http404('Book not found')
    if request.method == 'POST':
        BOOKS = [b for b in BOOKS if b.id != book_id]
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
