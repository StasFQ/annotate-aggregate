from django.urls import path

from hm12.views import *

app_name = 'hm12'
urlpatterns =[
    path('', main_page, name='main_page'),
    path('books/', get_books, name='get_books'),
    path('authors/', get_author, name='get_author'),
    path('book/<int:pk>/', book, name='book'),
    path('author/<int:pk>/', author, name='author')

]