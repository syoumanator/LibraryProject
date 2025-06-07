import os

from django.core.management import BaseCommand
from dotenv import load_dotenv

from users.models import User

load_dotenv()


class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            username=os.getenv("SU_username"),
            email=os.getenv("SU_email"),
            first_name=os.getenv("SU_first_name"),
            last_name=os.getenv("SU_last_name"),
            phone_number=os.getenv("phone_number"),
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password(os.getenv("SU_password"))
        user.save()
        self.stdout.write(
            self.style.SUCCESS(
                f"Admin user created: {user.username}, {user.email}, "
                f"{user.first_name}, {user.last_name}, {user.phone_number}"
            )
        )
