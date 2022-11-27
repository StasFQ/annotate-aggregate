from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Avg, FloatField, IntegerField, Count, Max, Min
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.cache import cache_page

from .models import Book, Author, Publisher, Store


def main_page(request):
    return render(request, 'main_page.html')


@cache_page(15)
def get_books(request):
    book_authors = Book.objects.annotate(auth=Count('authors')).all()
    price = Book.objects.aggregate(Avg('price', output_field=IntegerField()), Max('price', output_field=IntegerField()),
                                   Min('price', output_field=IntegerField()))
    paginator = Paginator(book_authors, 150)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'get_books.html', {
                                              'average_price': price['price__avg'],
                                              'Max_price': price['price__max'],
                                              'Min_price': price['price__min'],
                                              'page_obj': page_obj,
                                              'page_number': page_number,
                                              'book_authors': book_authors})


def book(request, pk):
    book = get_object_or_404(Book, id=pk)
    books = book.authors.all()
    return render(request, 'book.html', {'book': book,
                                         'books': books})


def get_author(request):
    authors = Author.objects.prefetch_related('book_set').all()
    all_authors = Author.objects.aggregate(Count('id'))
    return render(request, 'get_author.html', {'authors': authors,
                                               'all_authors': all_authors['id__count']})


def author(request, pk):
    authors = get_object_or_404(Author, id=pk)
    author = authors.book_set.all()
    return render(request, 'author.html', {'authors': authors,
                                           'author': author})


@cache_page(15)  # решил закешировать эту вью,так как из всех тут наибольшее количество запросов в базу.
def get_store(request):
    all_books = Store.objects.annotate(num_books=Count('books'))
    return render(request, 'get_store.html', {'all_books': all_books})


def stores(request, pk):
    store = get_object_or_404(Store, pk=pk)
    books = store.books.all()
    return render(request, 'store.html', {'store': store, 'books': books})


class ListPublisher(generic.ListView):
    template_name = 'list_publisher.html'
    model = Publisher
    queryset = Publisher.objects.all()
    paginate_by = 5


class CreatePublisher(LoginRequiredMixin, generic.CreateView):
    template_name = 'publisher_form.html'
    model = Publisher
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('hm12:ListPublisher')


class UpdatePublisher(LoginRequiredMixin, generic.UpdateView):
    template_name = 'update_publisher.html'
    model = Publisher
    fields = ['name']

    def get_success_url(self):
        return reverse_lazy('hm12:ListPublisher')


class DeletePublisher(LoginRequiredMixin, generic.DeleteView):
    template_name = 'delete_publisher.html'
    model = Publisher
    success_url = reverse_lazy('hm12:ListPublisher')


class DetailPublisher(generic.DetailView):
    template_name = 'detail_publisher.html'
    model = Publisher
    context_object_name = 'publisher'
