from django.contrib import admin

from hm12.models import Author, Publisher, Store, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_filter = ['age']
    search_fields = ['name']
    ordering = ['age']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'get_rating', 'publisher', 'pubdate']
    list_filter = ['pages', 'price']
    search_fields = ['name', 'rating']
    ordering = ['price']


class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_books']
    search_fields = ['name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Store, StoreAdmin)
