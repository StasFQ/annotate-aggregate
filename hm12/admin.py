from django.contrib import admin

from hm12.models import Author, Publisher, Store, Book


class BookInline(admin.TabularInline):
    model = Book
    extra = 3


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']
    list_filter = ['age']
    search_fields = ['name']
    ordering = ['age']


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    inlines = [BookInline]


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'price', 'rating', 'authora', 'publisher', 'pubdate']
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
