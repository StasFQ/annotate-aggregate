import datetime
import random
import radar

from django.core.management.base import BaseCommand

from hm12.models import Book, Publisher, Author
from random import randrange
from datetime import timedelta



class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number',  type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        books = []
        P = Publisher.objects.all().values_list('id', flat=True)
        for i in range(options['number']):
            books.append(Book(name=f'Book_{i}', pages=random.randint(200, 400), price=random.randint(200, 350),
                              rating=random.randint(1, 10),
                              pubdate=radar.random_date(start='2000-05-24', stop='2013-05-24'),
                              publisher_id=random.choice(P))),
        Book.objects.bulk_create(books)
        author_ids = Author.objects.values_list('id', flat=True)
        for i in range(len(author_ids)):
            a = random.randint(1, 5)
            book = Book.objects.get(id=a)
            book.authors.add(random.choice(author_ids))
