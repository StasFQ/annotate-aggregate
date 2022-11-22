from django.urls import path

from hm12.views import main_page, get_books, get_author, book, author, get_publisher, get_store, stores, publisher, \
    CreatePublisher, UpdatePublisher, DeletePublisher, DetailPublisher, ListPublisher

app_name = 'hm12'
urlpatterns = [
    path('', main_page, name='main_page'),
    path('books/', get_books, name='get_books'),
    path('authors/', get_author, name='get_author'),
    path('book/<int:pk>/', book, name='book'),
    path('author/<int:pk>/', author, name='author'),
    path('publisher/', get_publisher, name='get_publisher'),
    path('publisher/<int:pk>/', publisher, name='publisher'),
    path('store/', get_store, name='get_store'),
    path('store/<int:pk>/', stores, name='store'),
    path('publishers/', CreatePublisher.as_view(), name='CreatePublisher'),
    path('update_publisher/<int:pk>', UpdatePublisher.as_view(), name='UpdatePublisher'),
    path('delete_publisher/<int:pk>', DeletePublisher.as_view(), name='DeletePublisher'),
    path('detail_publisher/<int:pk>', DetailPublisher.as_view(), name='DetailPublisher'),
    path('list_publisher/', ListPublisher.as_view(), name='ListPublisher')
]
