import datetime
import random

from django.core.management.base import BaseCommand

from hm12.models import Book, Publisher, Author


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('number',  type=int, choices=range(1, 11))

    def handle(self, *args, **options):
        b = ['Перлини української класики', 'Пятьдесят оттенков', 'Маленький принц', 'Повести Белкина',
             'Сказка о царе Салтане', 'Лесна песня', 'Евгений Онегин', 'Украдене щастя', 'Скарбниця української класик',
             'Изучаем Пайтон', 'Кобзар', 'Незримая жизнь Адди Ларю', 'Сфинкс', 'Телени', 'Стрела', 'Вино з одуванчиков',
             'Барышня-крестьянка', 'Козетта', 'Анна Каренина', 'Harry Potter', 'Над пропастью во ржи', 'Шантарам',
             'Мастер и Маргарита', 'Сиротки', 'Та', 'Служба доставки книг', 'Из крови и пепла', 'Что скрывает прилив',
             'Перехресні стежки', 'Бояриня', 'Финист  Ясный сокол', 'Пятая Салли', 'Цвет для Элджернона', 'Отверженные',
             'Немного ненависти', 'Викинуті українці', 'Три товарища', 'Человек', 'Книжный на левом берегу Сены',
             'Оккульттрегер', 'Прикосновение', 'Война и мир', 'Пророк. Поеми. Поезії', 'Дневник книготорговца',
             'Империя вампиров', 'Воскресение', 'Книжная лавка', 'Собор Парижской Богоматери', 'Захар Беркут',
             'Книжная лавка под дождём', 'Книжный магазинчик счастья']
        books = []
        P = Publisher.objects.all().values_list('id', flat=True)
        for i in range(options['number']):
            books.append(Book(name=random.choice(b), pages=random.randint(200, 400), price=random.randint(200, 350),
                              rating=random.randint(1, 10), pubdate=datetime.datetime.now(), publisher_id=random.choice(P))),
        Book.objects.bulk_create(books)
        author_ids = Author.objects.values_list('id', flat=True)
        for i in range(len(author_ids)):
            a = random.randint(1, 5)
            book = Book.objects.get(id=a)
            book.authors.add(random.choice(author_ids))
