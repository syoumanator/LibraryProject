from rest_framework import generics

from authors.models import Author
from authors.serializers import AuthorSerializers


class AuthorCreateApiView(generics.CreateAPIView):
    serializer_class = AuthorSerializers
    pass


class AuthorRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()

    pass


class AuthorListApiView(generics.ListAPIView):
    serializer_class = AuthorSerializers
    queryset = Author.objects.all()

    pass


class AuthorUpdateApiView(generics.UpdateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    pass


class AuthorDestroyApiView(generics.DestroyAPIView):
    queryset = Author.objects.all()
    pass
