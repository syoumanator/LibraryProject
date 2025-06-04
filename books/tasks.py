from celery import shared_task

from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


@shared_task
def send_information(name):
    """Уведомляет о взятии книги в аренду"""
    send_mail(f"Вы взяли книгу {name.book}", f"Поздравляем с взятием книги, не забудьте вернуть до {name.deadline}", EMAIL_HOST_USER, [name.user.email])
