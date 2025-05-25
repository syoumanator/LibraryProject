import os

from django.core.management import BaseCommand

from users.models import User

from dotenv import load_dotenv
load_dotenv()


class Command(BaseCommand):
    help = "Создание суперпользователя"

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            username=os.getenv("SU_username"),
            email=os.getenv("SU_email"),
            first_name=os.getenv("SU_first_name"),
            last_name=os.getenv("SU_last_name"),
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.set_password(os.getenv("SU_password"))
        user.save()
        self.stdout.write(self.style.SUCCESS(f"Admin user created: {user.username}, {user.email}, {user.first_name}, {user.last_name},"))
