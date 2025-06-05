from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from books.models import Book, TakeBook
from books.pagination import LibraryPagination
from books.serializers import BookSerializer, TakeBookSerializers
from books.services import return_book, take_book
from users.permissions import IsModer


class BookCreateApiView(generics.CreateAPIView):
    """Эндпоинт создания книги"""
    serializer_class = BookSerializer
    permission_classes = [
        IsModer | IsAdminUser,
    ]


class BookListApiView(generics.ListAPIView):
    """Эндпоинт просмотра списка книг"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        "title",
        "genre",
        "author__last_name",
    )
    pagination_class = LibraryPagination
    permission_classes = [
        AllowAny,
    ]


class BookRetrieveApiView(generics.RetrieveAPIView):
    """Эндпоинт просмотра книги"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class BookUpdateApiView(generics.UpdateAPIView):
    """Эндпоинт изменения книги"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [
        IsModer | IsAdminUser,
    ]


class BookDestroyApiView(generics.DestroyAPIView):
    """Эндпоинт удаления книги"""
    queryset = Book.objects.all()
    permission_classes = [
        IsModer | IsAdminUser,
    ]


class TakeBookCreateApiView(generics.CreateAPIView):
    """Эндпоинт создания арендованной книги"""
    queryset = TakeBook.objects.all()
    serializer_class = TakeBookSerializers
    permission_classes = [
        IsModer | IsAdminUser,
    ]

    def perform_create(self, serializer):
        data = serializer.save(user=self.request.user)
        take_book(data.book)
        data.save()


class TakeBookListApiView(generics.ListAPIView):
    """Эндпоинт просмотра списка арендованных книг"""
    serializer_class = TakeBookSerializers
    queryset = TakeBook.objects.all()
    pagination_class = LibraryPagination
    permission_classes = [
        IsModer | IsAdminUser,
    ]

    def get_queryset(self):
        if IsAdminUser().has_permission(self.request, self) or IsModer().has_permission(
            self.request, self
        ):
            print(TakeBook.objects.all())
            return TakeBook.objects.all()
        else:
            print(TakeBook.objects.all())
            return TakeBook.objects.filter(user=self.request.user)


class TakeBookRetrieveApiView(generics.RetrieveAPIView):
    """Эндпоинт просмотра арендованной книги"""
    queryset = TakeBook.objects.all()
    serializer_class = TakeBookSerializers
    permission_classes = [
        IsModer | IsAdminUser,
    ]


class TakeBookUpdateApiView(generics.UpdateAPIView):
    """Эндпоинт изменения арендованной книги"""
    queryset = TakeBook.objects.all()
    serializer_class = TakeBookSerializers
    permission_classes = [
        IsModer | IsAdminUser,
    ]

    def perform_update(self, serializer):
        data = serializer.save()
        book = data.book
        return_book(data, book)
        data.save()


class TakeBookDestroyApiView(generics.DestroyAPIView):
    """Эндпоинт удаления арендованной книги"""
    queryset = TakeBook.objects.all()
    permission_classes = [
        IsModer | IsAdminUser,
    ]
