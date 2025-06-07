from rest_framework import status
from rest_framework.test import APITestCase

from authors.models import Author
from users.models import User


class AuthorForAdminAPITestCase(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="SU", email="su@example.com", password="testpass123"
        )
        self.user = User.objects.create(
            username="User", email="user@example.com", password="testpass123"
        )

        self.client.force_authenticate(user=self.user)
        self.authors = Author.objects.create(
            first_name="Александр",
            last_name="Пушкин",
            country="Россия",
        )

    def test_super_user(self):
        """Права суперпользователя"""
        self.client.force_authenticate(user=self.superuser)
        update_data = {
            "first_name": "Николай",
            "last_name": "Гоголь",
            "country": "Россия",
        }

        """Создание автора"""
        data = {
            "first_name": "Лев",
            "last_name": "Толстой",
            "country": "Россия",
        }
        response = self.client.post("/authors/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        """Просмотр авторов"""
        response = self.client.get("/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Просмотр автора"""
        response = self.client.get(f"/authors/{self.authors.last_name}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Обновление автора"""
        response = self.client.put(
            f"/authors/{self.authors.last_name}/update/", data=update_data
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__delete_superuser(self):
        """Удаление автора"""
        self.client.force_authenticate(user=self.superuser)
        response = self.client.delete(f"/authors/{self.authors.last_name}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user(self):
        """Права пользователя"""
        self.client.force_authenticate(user=self.user)
        update_data = {
            "first_name": "Александр",
            "last_name": "Пушкин",
            "country": "Россия1",
        }

        """Создание автора"""
        data = {
            "first_name": "Александр",
            "last_name": "Пушкин",
            "country": "Россия",
        }
        response = self.client.post("/authors/create/", data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        """Просмотр авторов"""
        response = self.client.get("/authors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Просмотр автора"""
        response = self.client.get(f"/authors/{self.authors.last_name}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Обновление автора"""
        response = self.client.put(
            f"/authors/{self.authors.last_name}/update/", data=update_data
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_user(self):
        """Удаление автора"""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(f"/authors/{self.authors.last_name}/delete/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
