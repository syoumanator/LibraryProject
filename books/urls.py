from django.urls import path

from books.apps import BooksConfig
from books.views import BookCreateApiView, BookListApiView, BookRetrieveApiView, BookUpdateApiView, BookDestroyApiView

app_name = BooksConfig.name

urlpatterns = [
    path("", BookListApiView.as_view(), name="books-list"),
    path("create/", BookCreateApiView.as_view(), name="book-create"),
    path("<str:title>/", BookRetrieveApiView.as_view(lookup_field="title"), name="book-detail"),
    path("<str:title>/update/", BookUpdateApiView.as_view(lookup_field="title"), name="title-update"),
    path("<str:title>/delete/", BookDestroyApiView.as_view(lookup_field="title"), name="title-delete"),
]
