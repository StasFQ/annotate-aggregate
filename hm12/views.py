from django.shortcuts import render, get_object_or_404
from .models import Book, Author


def main_page(request):
    return render(request, 'main_page.html')


def get_books(request):
    book = Book.objects.prefetch_related('authors').all()
    return render(request, 'get_books.html', {'book': book})


def book(request, pk):
    book = get_object_or_404(Book, id=pk)
    return render(request, 'book.html', {'book': book})


def get_author(request):
    authors = Author.objects.prefetch_related('book_set').all()
    return render(request, 'get_author.html', {'authors': authors})


def author(request, pk):
    authors = get_object_or_404(Author, id=pk)
    author = Author.objects.prefetch_related('book_set').get(id=pk)
    return render(request, 'author.html', {'authors': authors,
                                           'author': author})
