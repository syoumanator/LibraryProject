from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User
from users.pagination import UserPagination
from users.permissions import IsModer, IsOwner
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Эндпоинт создания"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    """Эндпоинт просмотра"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwner | IsModer | IsAdminUser,)


class UserListApiView(ListAPIView):
    """Эндпоинт просмотра списка"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination
    permission_classes = (IsModer | IsAdminUser,)


class UserUpdateAPIView(UpdateAPIView):
    """Эндпоинт изменения"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwner | IsModer | IsAdminUser,)


class UserDestroyAPIView(DestroyAPIView):
    """Эндпоинт удаления"""
    queryset = User.objects.all()
    permission_classes = (IsOwner | IsAdminUser,)
