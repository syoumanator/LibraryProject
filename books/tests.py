# from rest_framework import status
# from rest_framework.test import APITestCase
#
# from books.models import Book
# from users.models import User
# from authors.models import Author
#
# class BookForAdminAPITestCase(APITestCase):
#
#     def setUp(self):
#         self.user = User.objects.create_superuser(username="Test", email="test@example.com", password="testpass123")
#         self.client.force_authenticate(user=self.user)
#         self.authors = Author.objects.create(
#             first_name="Лев",
#             last_name="Толстой",
#             country="Россия"
#         )
#         self.book = Book.objects.create(
#             title="Утро помещика",
#             author="",
#             quantity="",
#             in_stock_quantity="",
#             is_available=""
#         )
#
#     def test_book_create(self):
#         """Создание Книги"""
#         data = {
#             "title",
#             "author",
#             "quantity",
#             "in_stock_quantity",
#             "is_available",
#         }
#         response = self.client.post("/books/create/", data=data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#
#     def test_book_detail(self):
#         """Просмотр Книги"""
#         response = self.client.get(f"/books/{self.book.title}/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_book_list(self):
#         """Просмотр Книги"""
#         response = self.client.get(f"/books/")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_book_update(self):
#         """Обновление Книги"""
#         update_data = {
#             "first_name": "Александр",
#             "last_name": "Пушкин",
#             "country": "Россия1",
#         }
#         response = self.client.put(f"/books/{self.book.title}/update/", data=update_data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_book_delete(self):
#         """Удаление Книги"""
#         response = self.client.delete(f"/books/{self.book.title}/delete/")
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#
#
# # class AuthorForUserAPITestCase(APITestCase):
# #
# #     def setUp(self):
# #         self.user = User.objects.create(username="Test", email="test@example.com", password="testpass123")
# #         self.client.force_authenticate(user=self.user)
# #         self.authors = Author.objects.create(
# #             first_name="place",
# #             last_name="00:00",
# #             country="act",
# #         )
# #
# #     def test_author_create(self):
# #         """Создание Автора"""
# #         data = {
# #             "first_name": "Александр",
# #             "last_name": "Пушкин",
# #             "country": "Россия",
# #         }
# #         response = self.client.post("/authors/create/", data=data)
# #         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
# #
# #     def test_author_detail(self):
# #         """Просмотр Автора"""
# #         response = self.client.get(f"/authors/{self.authors.last_name}/")
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #
# #     def test_author_list(self):
# #         """Просмотр Автора"""
# #         response = self.client.get(f"/authors/")
# #         self.assertEqual(response.status_code, status.HTTP_200_OK)
# #
# #     def test_author_update(self):
# #         """Обновление Автора"""
# #         update_data = {
# #             "first_name": "Александр",
# #             "last_name": "Пушкин",
# #             "country": "Россия1",
# #         }
# #         response = self.client.put(f"/authors/{self.authors.last_name}/update/", data=update_data)
# #         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
# #
# #     def test_author_delete(self):
# #         """Удаление Автора"""
# #         response = self.client.delete(f"/authors/{self.authors.last_name}/delete/")
# #         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
#
