from rest_framework import generics

from authors.models import Author
from authors.serializers import AuthorSerializers


class AuthorCreateApiView(generics.CreateAPIView):
    pass


class AuthorRetrieveApiView(generics.RetrieveAPIView):
    pass


class AuthorListApiView(generics.ListAPIView):
    pass


class AuthorUpdateApiView(generics.UpdateAPIView):
    pass


class AuthorDestroyApiView(generics.DestroyAPIView):
    pass
