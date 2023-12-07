from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .models import User
from .permissions import UserRoutesPermissions


class UserView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, UserRoutesPermissions]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request, user_id=None):
        if user_id:
            user = get_object_or_404(User, id=user_id)
            self.check_object_permissions(request, user)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=200)
        users = User.objects.all()
        result_page = self.paginate_queryset(users, request)
        if result_page is not None:
            serializer = UserSerializer(result_page, many=True)
            return self.get_paginated_response(serializer.data, status=200)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=200)

    def patch(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)

    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        user.delete()
        return Response(status=204)


class LoginJWTView(TokenObtainPairView):
    ...
