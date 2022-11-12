from django.urls import path

from hm12.views import main_page, get_books, get_author, book, author, get_publisher, get_store, stores

app_name = 'hm12'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('books/', get_books, name='get_books'),
    path('authors/', get_author, name='get_author'),
    path('book/<int:pk>/', book, name='book'),
    path('author/<int:pk>/', author, name='author'),
    path('publisher/', get_publisher, name='get_publisher'),
    path('store/', get_store, name='get_store'),
    path('store/<int:pk>/', stores, name='store')

]
