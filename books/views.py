from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from books.models import Book
from books.pagination import LibraryPagination
from books.serializers import BookSerializer
from rest_framework.permissions import IsAdminUser, AllowAny
from users.permissions import IsModer


class BookCreateApiView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [IsModer | IsAdminUser,]


class BookListApiView(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("title",  "genre", "author__last_name",)
    pagination_class = LibraryPagination
    permission_classes = [AllowAny,]


class BookRetrieveApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsModer | IsAdminUser,]


class BookDestroyApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    permission_classes = [IsModer | IsAdminUser,]
