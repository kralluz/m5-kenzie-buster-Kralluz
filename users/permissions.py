from rest_framework import permissions
from .models import User
from rest_framework.views import Request, View


class UserRoutesPermissions(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return request.user == obj or request.user.is_employee


class TokenPresentPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET', 'PATCH']:
            return 'Authorization' in request.headers
        return True
