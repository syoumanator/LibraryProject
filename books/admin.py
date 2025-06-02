from django.contrib import admin

from books.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "genre",
        "description",
        "pages",
        "publication_date",
        "translator",
        "quantity",
        "in_stock_quantity",
        "is_available",
        "image",
    )
