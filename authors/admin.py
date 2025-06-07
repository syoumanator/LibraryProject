from django.contrib import admin

from .models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "date_of_birth",
        "date_of_death",
        "image",
        "country",
        "biography",
    )
    list_filter = ("last_name", "country")
