from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls", namespace="users")),
    path("authors/", include("authors.urls", namespace="authors")),
]
