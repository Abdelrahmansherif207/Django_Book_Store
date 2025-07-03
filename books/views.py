from django.shortcuts import render, redirect, get_object_or_404
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('description')
        rate = request.POST.get('rate') or 0
        book = Book.objects.create(title=title, desc=desc, rate=rate)
        return redirect('book_list')
    return render(request, 'books/book_form.html')

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.views += 1
    book.save()
    return render(request, 'books/book_detail.html', {'book': book})

def book_edit(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.desc = request.POST.get('description')
        book.rate = request.POST.get('rate') or 0
        book.save()
        return redirect('book_detail', book_id=book.id)
    return render(request, 'books/book_form.html', {'book': book})

def book_delete(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})
