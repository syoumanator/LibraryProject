from rest_framework import status
from rest_framework.test import APITestCase

from books.models import Book
from users.models import User
from authors.models import Author


class BookForAdminAPITestCase(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(username="SU", email="su@example.com", password="testpass123")
        self.user = User.objects.create(username="User", email="user@example.com", password="testpass123")
        self.authors = Author.objects.create(
            first_name="Лев",
            last_name="Толстой",
            country="Россия"
        )
        self.book = Book.objects.create(
            title="Война и мир",
            author=self.authors,
            quantity="10",
            in_stock_quantity="5",
        )

    def test_super_user(self):
        """Права суперпользователя"""
        self.client.force_authenticate(user=self.superuser)
        update_data = {
            "title": "Война и мир",
            "author": self.authors.last_name,
            "quantity": "10",
            "in_stock_quantity": "5",
            "pages": "1200"
        }

        """Создание книги"""
        data = {
            "title": "Исповедь",
            "author": self.authors.last_name,
            "quantity": "10",
            "in_stock_quantity": "5",
            "pages": "1000"
        }
        response = self.client.post("/books/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        """Просмотр Книг"""
        response = self.client.get(f"/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Просмотр книги"""
        response = self.client.get(f"/books/{self.book.title}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Обновление книги"""
        response = self.client.put(f"/books/{self.book.title}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Удаление книги"""
        response = self.client.delete(f"/books/{self.book.title}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user(self):
        """Права обычного пользователя"""
        self.client.force_authenticate(user=self.user)
        update_data = {
            "title": "Война и мир",
            "author": self.authors.last_name,
            "quantity": "10",
            "in_stock_quantity": "5",
            "pages": "1200"
        }

        """Создание книги"""
        data = {
            "title": "Исповедь",
            "author": self.authors.last_name,
            "quantity": "10",
            "in_stock_quantity": "5",
            "pages": "1000"
        }
        response = self.client.post("/books/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        """Просмотр книг"""
        response = self.client.get(f"/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Просмотр книги"""
        response = self.client.get(f"/books/{self.book.title}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Обновление книги"""
        response = self.client.put(f"/books/{self.book.title}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        """Удаление книги"""
        response = self.client.delete(f"/books/{self.book.title}/delete/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
