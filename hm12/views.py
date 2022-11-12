from django.shortcuts import render, get_object_or_404
from .models import Book, Author, Publisher, Store


def main_page(request):
    return render(request, 'main_page.html')


def get_books(request):
    book = Book.objects.prefetch_related('authors').all()
    return render(request, 'get_books.html', {'book': book})


def book(request, pk):
    book = get_object_or_404(Book, id=pk)
    books = book.authors.all()
    return render(request, 'book.html', {'book': book,
                                         'books': books})


def get_author(request):
    authors = Author.objects.prefetch_related('book_set').all()
    return render(request, 'get_author.html', {'authors': authors})


def author(request, pk):
    authors = get_object_or_404(Author, id=pk)
    author = authors.book_set.all()
    return render(request, 'author.html', {'authors': authors,
                                           'author': author})


def get_publisher(request):
    publishers = Publisher.objects.prefetch_related('book_set').all()
    return render(request, 'get_publisher.html', {'publishers': publishers})


def publisher(request, pk):
    publisher = get_object_or_404(Publisher, id=pk)
    publishers = publisher.book_set.all()
    return render(request, 'publisher.html', {'publisher': publisher, 'publishers': publishers})


def get_store(request):
    store = Store.objects.prefetch_related('books').all()
    return render(request, 'get_store.html', {'store': store})


def stores(request, pk):
    store = get_object_or_404(Store, pk=pk)
    books = store.books.all()
    return render(request, 'store.html', {'store': store, 'books': books})
