import random

from django.core.management.base import BaseCommand

from hm12.models import Book, Store


class Command(BaseCommand):


    def handle(self, *args, **options):
        s = ['Книжный рай', 'Читай', 'Books-store', 'Книги бу', 'Мир Книг']
        stores = []
        for i in range(1, 6):
            name = random.choice(s)
            stores.append(Store(name=name))
        Store.objects.bulk_create(stores)
        book_ids = Book.objects.values_list('id', flat=True)
        for i in range(len(book_ids)):
            a = random.randint(1, 5)
            store = Store.objects.get(id=a)
            store.books.add(random.choice(book_ids))
