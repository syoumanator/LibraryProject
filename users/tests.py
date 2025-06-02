from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserAPITestCase(APITestCase):

    def setUp(self):
        self.superuser = User.objects.create_superuser(
            username="SU",
            email="su@example.com",
            password="testpass123",
            first_name="Super",
            last_name="User",
            phone_number="+79991111111"
        )
        self.normal_user = User.objects.create_user(
            username="Normal",
            email="user@example.com",
            password="testpass123",
            first_name="Normal",
            last_name="User",
            phone_number="+79991111111"
        )

    def test_user_register(self):
        """Создание пользователя"""
        data = {"email": "test@mail.com",
                "username": "Test_1",
                "password": "123456789",
                "first_name": "Гриша",
                "last_name": "Гришков",
                "phone_number": "+79991111111",

                }
        response = self.client.post("/users/register/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_superuser_permissions(self):
        """Проверка суперпользователя"""
        self.client.force_authenticate(user=self.superuser)
        update_data = {"phone_number": "+79991111122"}

        """Просмотр всех пользователей"""
        response = self.client.get(f"/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Просмотр другого пользователя"""
        response = self.client.get(f"/users/{self.superuser.username}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        """Просмотр себя"""
        response = self.client.get(f"/users/{self.normal_user.username}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        "Обновление другого пользователя"
        response = self.client.patch(f"/users/{self.superuser.username}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        "Обновление другого пользователя"
        response = self.client.patch(f"/users/{self.normal_user.username}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        "Удаление себя"
        response = self.client.delete(f"/users/{self.superuser.username}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        "Удаление другого пользователя"
        response = self.client.delete(f"/users/{self.normal_user.username}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user(self):
        """Права обычного пользователя"""
        self.client.force_authenticate(user=self.normal_user)
        update_data = {"phone_number": "+79991111122"}

        """Просмотр всех пользователей"""
        response = self.client.get(f"/users/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        """Просмотр другого пользователя"""
        response = self.client.get(f"/users/{self.superuser.username}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        """Просмотр себя"""
        response = self.client.get(f"/users/{self.normal_user.username}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        "Обновление другого пользователя"
        response = self.client.patch(f"/users/{self.superuser.username}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        "Обновление другого пользователя"
        response = self.client.patch(f"/users/{self.normal_user.username}/update/", data=update_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        "Удаление другого пользователя"
        response = self.client.delete(f"/users/{self.superuser.username}/delete/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        "Удаление себя"
        response = self.client.delete(f"/users/{self.normal_user.username}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
