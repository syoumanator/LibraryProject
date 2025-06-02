from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView, UpdateAPIView

from rest_framework.permissions import AllowAny, IsAdminUser

from users.pagination import UserPagination
from users.permissions import IsOwner, IsModer

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwner | IsModer | IsAdminUser,)


class UserListApiView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = UserPagination
    permission_classes = (IsModer | IsAdminUser,)


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsOwner | IsModer | IsAdminUser,)


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    permission_classes = (IsOwner | IsAdminUser,)
