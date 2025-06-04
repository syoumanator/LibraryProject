from rest_framework import serializers

from authors.models import Author
from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Author.objects.all(),
        slug_field='last_name'
    )

    class Meta:
        model = Book
        fields = '__all__'
