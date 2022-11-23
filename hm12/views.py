from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

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



def get_store(request):
    store = Store.objects.prefetch_related('books').all()
    return render(request, 'get_store.html', {'store': store})

def stores(request, pk):
    store = get_object_or_404(Store, pk=pk)
    books = store.books.all()
    return render(request, 'store.html', {'store': store, 'books': books})




class CreatePublisher(LoginRequiredMixin, generic.CreateView):
    template_name = 'publisher_form.html'
    model = Publisher
    fields = ['name']


class UpdatePublisher(LoginRequiredMixin, generic.UpdateView):
    template_name = 'update_publisher.html'
    model = Publisher
    fields = ['name']


class DeletePublisher(LoginRequiredMixin, generic.DeleteView):
    template_name = 'delete_publisher.html'
    model = Publisher
    success_url = reverse_lazy('hm12:get_publisher')


class DetailPublisher(generic.DetailView):
    template_name = 'detail_publisher.html'
    model = Publisher
    context_object_name = 'publisher'


class ListPublisher(generic.ListView):
    template_name = 'list_publisher.html'
    model = Publisher
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


