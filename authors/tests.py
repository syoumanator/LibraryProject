from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from users.models import User


class AuthorForAdminAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(username="Test", email="test@example.com", password="testpass123")
        self.client.force_authenticate(user=self.user)
        self.authors = Author.objects.create(
            first_name="Лев",
            last_name="Толстой",
            country="Россия",
        )

    def test_author_create(self):
        """Создание Автора"""
        data = {
            "first_name": "Александр",
            "last_name": "Пушкин",
            "country": "Россия",
        }
        response = self.client.post("/authors/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_author_detail(self):
        """Просмотр Автора"""
        response = self.client.get(f"/authors/{self.authors.last_name}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_list(self):
        """Просмотр Автора"""
        response = self.client.get(f"/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_update(self):
        """Обновление Автора"""
        update_data = {
            "first_name": "Александр",
            "last_name": "Пушкин",
            "country": "Россия1",
        }
        response = self.client.put(f"/authors/{self.authors.last_name}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_delete(self):
        """Удаление Автора"""
        response = self.client.delete(f"/authors/{self.authors.last_name}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class AuthorForUserAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(username="Test", email="test@example.com", password="testpass123")
        self.client.force_authenticate(user=self.user)
        self.authors = Author.objects.create(
            first_name="place",
            last_name="00:00",
            country="act",
        )

    def test_author_create(self):
        """Создание Автора"""
        data = {
            "first_name": "Александр",
            "last_name": "Пушкин",
            "country": "Россия",
        }
        response = self.client.post("/authors/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_detail(self):
        """Просмотр Автора"""
        response = self.client.get(f"/authors/{self.authors.last_name}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_list(self):
        """Просмотр Автора"""
        response = self.client.get(f"/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_author_update(self):
        """Обновление Автора"""
        update_data = {
            "first_name": "Александр",
            "last_name": "Пушкин",
            "country": "Россия1",
        }
        response = self.client.put(f"/authors/{self.authors.last_name}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_author_delete(self):
        """Удаление Автора"""
        response = self.client.delete(f"/authors/{self.authors.last_name}/delete/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
