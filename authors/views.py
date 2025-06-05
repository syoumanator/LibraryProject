from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from authors.models import Author
from authors.pagination import AuthorsPagination
from authors.serializers import AuthorSerializers


class AuthorCreateApiView(generics.CreateAPIView):
    """Эндпоинт создания"""
    serializer_class = AuthorSerializers
    permission_classes = [
        IsAdminUser,
    ]


class AuthorListApiView(generics.ListAPIView):
    """Эндпоинт просмотра списка"""
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()
    pagination_class = AuthorsPagination
    permission_classes = [
        AllowAny,
    ]


class AuthorRetrieveApiView(generics.RetrieveAPIView):
    """Эндпоинт просмотра"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [AllowAny]


class AuthorUpdateApiView(generics.UpdateAPIView):
    """Эндпоинт изменения"""
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    permission_classes = [
        IsAdminUser,
    ]


class AuthorDestroyApiView(generics.DestroyAPIView):
    """Эндпоинт удаления"""
    queryset = Author.objects.all()
    permission_classes = [
        IsAdminUser,
    ]
