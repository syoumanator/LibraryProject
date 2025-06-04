from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from books.models import Book, TakeBook
from books.pagination import LibraryPagination
from books.serializers import BookSerializer, TakeBookSerializers
from rest_framework.permissions import IsAdminUser, AllowAny

from books.services import take_book, return_book
from users.permissions import IsModer, IsOwner


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


class TakeBookCreateApiView(generics.CreateAPIView):
    queryset = TakeBook.objects.all()
    serializer_class = TakeBookSerializers
    permission_classes = [IsModer | IsAdminUser,]

    def perform_create(self, serializer):
        data = serializer.save(user=self.request.user)
        take_book(data.book)
        data.save()


class TakeBookListApiView(generics.ListAPIView):
    serializer_class = TakeBookSerializers
    queryset = TakeBook.objects.all()
    pagination_class = LibraryPagination
    permission_classes = [IsModer | IsAdminUser,]


class TakeBookRetrieveApiView(generics.RetrieveAPIView):
    queryset = TakeBook.objects.all()
    serializer_class = TakeBookSerializers

    def get_queryset(self):
        if IsAdminUser().has_permission(self.request, self) or IsModer().has_permission(self.request, self):
            return TakeBook.objects.all()
        else:
            return TakeBook.objects.filter(user=self.request.user)


class TakeBookUpdateApiView(generics.UpdateAPIView):
    queryset = TakeBook.objects.all()
    serializer_class = TakeBookSerializers
    permission_classes = [IsModer | IsAdminUser,]

    def perform_update(self, serializer):
        data = serializer.save()
        book = data.book
        return_book(data, book)
        data.save()


class TakeBookDestroyApiView(generics.DestroyAPIView):
    queryset = TakeBook.objects.all()
    permission_classes = [IsModer | IsAdminUser,]
