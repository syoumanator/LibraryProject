from django.urls import path

from books.apps import BooksConfig
from books.views import BookCreateApiView, BookListApiView, BookRetrieveApiView, BookUpdateApiView, BookDestroyApiView, \
    TakeBookCreateApiView, TakeBookRetrieveApiView, TakeBookDestroyApiView, TakeBookListApiView, TakeBookUpdateApiView

app_name = BooksConfig.name

urlpatterns = [
    path("", BookListApiView.as_view(), name="books-list"),
    path("create/", BookCreateApiView.as_view(), name="book-create"),
    path("<str:title>/", BookRetrieveApiView.as_view(lookup_field="title"), name="book-detail"),
    path("<str:title>/update/", BookUpdateApiView.as_view(lookup_field="title"), name="book-update"),
    path("<str:title>/delete/", BookDestroyApiView.as_view(lookup_field="title"), name="book-delete"),

    path("rent/", TakeBookListApiView.as_view(), name="books-list"),
    path("rent/create/", TakeBookCreateApiView.as_view(), name="rent-book-create"),
    path("rent/<str:book>/", TakeBookRetrieveApiView.as_view(lookup_field="book"), name="rent-book-detail"),
    path("rent/<str:book>/update/", TakeBookUpdateApiView.as_view(lookup_field="book"), name="rent-book-update"),
    path("rent/<str:book>/delete/", TakeBookDestroyApiView.as_view(lookup_field="book"), name="rent-book-delete"),
]
