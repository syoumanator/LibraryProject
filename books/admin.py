from django.contrib import admin

from books.models import Book, TakeBook


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


@admin.register(TakeBook)
class RentBooksAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "user",
        "take_date",
        "return_date",
        "is_returned",
        "deadline",
    )