from rest_framework import permissions


class IsModer(permissions.BasePermission):
    """Проверяет, является ли пользователь модератором."""

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moders").exists()


class IsOwner(permissions.BasePermission):
    """Проверяет, является ли пользователь владельцем."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


    # def get_permissions(self):
    #     if self.action == "create":
    #         self.permission_classes = (~IsModer,)
    #     elif self.action in ["update", "retrieve"]:
    #         self.permission_classes = (IsModer | IsOwner,)
    #     elif self.action == "destroy":
    #         self.permission_classes = (~IsModer | IsOwner,)
    #     return super().get_permissions()