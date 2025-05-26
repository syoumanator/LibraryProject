from django.urls import path

from authors.apps import AuthorsConfig
from authors.views import AuthorCreateApiView, AuthorRetrieveApiView, AuthorUpdateApiView, AuthorListApiView, AuthorDestroyApiView

app_name = AuthorsConfig.name

urlpatterns = [
    path("", AuthorListApiView.as_view(), name="authors-list"),
    path("create/", AuthorCreateApiView.as_view(), name="author-create"),
    path("<int:pk>/", AuthorRetrieveApiView.as_view(), name="author-detail"),
    path("<int:pk>/update", AuthorUpdateApiView.as_view(), name="author-update"),
    path("<int:pk>/delete", AuthorDestroyApiView.as_view(), name="author-delete"),
]
