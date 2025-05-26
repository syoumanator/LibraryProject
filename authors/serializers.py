from rest_framework import serializers

from authors.models import Author


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
