import random

from django.core.management.base import BaseCommand

from hm12.models import Book, Store


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number', type=int, choices=range(1, 50))

    def handle(self, *args, **options):
        s = ['Книжный рай', 'Читай', 'Books-store', 'Книги бу', 'Мир Книг']
        stores = []
        for i in range(options['number']):
            name = random.choice(s)
            if name not in Store.objects.name:
                stores.append(Store(name=name))
        Store.objects.bulk_create(stores)
        book_ids = Book.objects.values_list('id', flat=True)
        for i in range(len(book_ids)):
            a = random.randint(1, 5)
            store = Store.objects.get(id=a)
            store.books.add(random.choice(book_ids))
