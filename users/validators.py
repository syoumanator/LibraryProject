from rest_framework.exceptions import ValidationError


class PhoneNumberValidator:
    """Проверка номера телефона"""

    def __init__(self, field1):
        self.field1 = field1

    def __call__(self, instance):
        if not instance.isdigit() or len(instance) != 11:
            raise ValidationError("Номер должен состоять из 11 цифр")
