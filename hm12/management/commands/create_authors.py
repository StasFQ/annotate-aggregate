import random

from django.core.management.base import BaseCommand

from hm12.models import Book, Author


class Command(BaseCommand):

    def handle(self, *args, **options):
        authors = []
        for i in range(1, 31):
            authors.append(Author(name=f'author_{i}', age=random.randint(30, 80)))
        Author.objects.bulk_create(authors)
