from rest_framework.serializers import ModelSerializer

from users.models import User
from users.validators import PhoneNumberValidator


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        validators = [
            PhoneNumberValidator(field1="phone_number"),
        ]