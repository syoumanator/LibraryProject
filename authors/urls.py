from django.urls import path

from authors.apps import AuthorsConfig
from authors.views import (
    AuthorCreateApiView,
    AuthorDestroyApiView,
    AuthorListApiView,
    AuthorRetrieveApiView,
    AuthorUpdateApiView,
)

app_name = AuthorsConfig.name

urlpatterns = [
    path("", AuthorListApiView.as_view(), name="authors-list"),
    path("create/", AuthorCreateApiView.as_view(), name="author-create"),
    path(
        "<str:last_name>/",
        AuthorRetrieveApiView.as_view(lookup_field="last_name"),
        name="author-detail",
    ),
    path(
        "<str:last_name>/update/",
        AuthorUpdateApiView.as_view(lookup_field="last_name"),
        name="author-update",
    ),
    path(
        "<str:last_name>/delete/",
        AuthorDestroyApiView.as_view(lookup_field="last_name"),
        name="author-delete",
    ),
]
