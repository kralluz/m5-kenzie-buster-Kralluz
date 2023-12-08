from rest_framework import permissions
from .models import User
from rest_framework.views import Request, View


class MoviesRoutesPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser
