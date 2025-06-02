from rest_framework.exceptions import ValidationError
from django.core.validators import RegexValidator


class PhoneNumberValidator:
    """Проверка номера телефона"""

    def __init__(self, field1):
        self.field1 = field1
        self.international_regex = RegexValidator(
            regex=r"^\+?7?\d{10}$",
            message="Формат номера телефона: '89991111111' или '+79991111111'"
        )

    def __call__(self, instance):
        phone_number = instance.get(self.field1)
        try:
            self.international_regex(phone_number)
        except ValidationError as e:
            raise ValidationError({self.field1: str(e)})
