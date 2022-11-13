import random

from django.core.management.base import BaseCommand

from hm12.models import Book, Author


class Command(BaseCommand):


    def handle(self, *args, **options):
        a = ['Леся Украинка', 'Михаил Булгаков', 'Николай Гоголь', 'Тарас Шевченко', 'Александр Пушкин', 'Оскар Уайльд',
             'Лев Толстой', 'Иван Франко', 'Дэниел Киз', 'Виктор Гюго', 'Эрих Мария Ремарк', 'Олена Пчелка',
             'Грегори Дэвид Робертс', 'Джордж Оруэлл', 'Всеволод Нестайко']
        authors = []
        for i in range(1, 16):
            authors.append(Author(name=random.choice(a), age=random.randint(30, 80)))
        Author.objects.bulk_create(authors)
