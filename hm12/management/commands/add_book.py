from django.core.management.base import BaseCommand

from hm12.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number',  type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        ans = []
        books = []
        for i in range(options['number']):
            ans.append(Book(name='Harry Potter', pages='436', price='416', rating=8, pubdate='2000-06-09', publisher_id=1))
        Book.objects.bulk_create(ans)
