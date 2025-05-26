from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150, verbose_name="First name", help_text="Введите имя автора")
    last_name = models.CharField(max_length=150, verbose_name="Last name", help_text="Введите фамилию автора")
    date_of_birth = models.DateField(verbose_name="Date of birth", help_text="Введите дату рождения (YYYY-MM-DD)", blank=True, null=True)
    date_of_death = models.DateField(verbose_name="Date of death", help_text="Введите дату смерти (YYYY-MM-DD)", blank=True, null=True,)
    image = models.ImageField(upload_to="author/image", verbose_name="Image", help_text="Загрузите изображение автора", blank=True,null=True,)
    country = models.CharField(max_length=30, verbose_name="Country", help_text="Укажите страну проживания автора", blank=True, null=True,)
    biography = models.TextField(verbose_name="Biography", help_text="Укажите биографию автора", blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

