import random
from django.core.management.base import BaseCommand

from hm12.models import Book, Publisher


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number',  type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        p = ['Украина', 'Картография', 'Морион', 'Фолио', 'Грамота', 'Иглмосс Эдишинз', 'Освита', 'Учебники и пособия',
             'Генеза', 'Ранок']
        publisher = []
        for i in range(options['number']):
            publisher.append(Publisher(name=random.choice(p)))
        Publisher.objects.bulk_create(publisher)
