from rest_framework import serializers

from authors.serializers import AuthorSerializers
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializers(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
