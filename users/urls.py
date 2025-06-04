from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import (
    UserCreateAPIView,
    UserDestroyAPIView,
    UserListApiView,
    UserRetrieveAPIView,
    UserUpdateAPIView,
)

app_name = UsersConfig.name

urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("", UserListApiView.as_view(), name="authors-list"),
    path(
        "<str:username>/",
        UserRetrieveAPIView.as_view(lookup_field="username"),
        name="user-detail",
    ),
    path(
        "<str:username>/update/",
        UserUpdateAPIView.as_view(lookup_field="username"),
        name="user-update",
    ),
    path(
        "<str:username>/delete/",
        UserDestroyAPIView.as_view(lookup_field="username"),
        name="delete",
    ),
]
