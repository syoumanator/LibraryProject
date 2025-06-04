from django.db import models
from authors.models import Author
from users.models import User


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name="Book Title", help_text="Укажите название книги")
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name="authors", verbose_name="Author", help_text="Укажите автора книги")
    genre = models.CharField(verbose_name="Book Genre", help_text="Укажите жанр книги", blank=True, null=True)
    description = models.TextField(verbose_name="Description", help_text="Напишите описание книги", blank=True, null=True)
    pages = models.PositiveSmallIntegerField(verbose_name="Количество страниц", help_text="Укажите количество страниц", blank=True, null=True)
    publication_date = models.DateField(verbose_name="Publication Date", help_text="Укажите дату публикации книги (YYYY-MM-DD)", blank=True, null=True)
    translator = models.CharField(max_length=100, verbose_name="Translator", help_text="Укажите переводчика", blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(verbose_name="Общее количество книг")
    in_stock_quantity = models.PositiveSmallIntegerField(verbose_name="Доступное количество книг")
    is_available = models.BooleanField(default=True, verbose_name="Is Available", help_text="Имеется ли книга для выдачи")
    image = models.ImageField(upload_to="books/image", help_text="Загрузите изображение книги", verbose_name="Image", blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ["author"]


class TakeBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book", related_name="book", help_text="Укажите отданную книгу",)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Читатель", help_text="Читатель, взявший книгу")
    take_date = models.DateField(auto_now_add=True, verbose_name="Дата выдачи книги")
    return_date = models.DateField(verbose_name="Дата возврата книги", blank=True, null=True)
    is_returned = models.BooleanField(default=False, verbose_name="Возврат книги")
    deadline = models.DateField(verbose_name="Когда книга должна быть возвращена", help_text="Укажите, когда книга должна быть возвращена (YYYY-MM-DD)")

    def __str__(self):
        return f"Читатель: {self.user}\nКнига: {self.book}\nСрок возврата: {self.deadline}"

    class Meta:
        verbose_name = "Аренда книги"
        verbose_name_plural = "Аренды книг"
        ordering = ["deadline"]
