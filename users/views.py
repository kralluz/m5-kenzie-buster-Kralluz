from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from users.serializers import UserSerializer


class UserView(APIView, PageNumberPagination):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if serializer.validated_data.get('is_employee'):
                user.is_superuser = True
                user.save()
            return Response(serializer.data, status=201)

    def get(self, request, pet_id=None):
        ...

    def patch(self, request, pet_id):
        ...

    def delete(self, request, pet_id):
        ...


class LoginJWTView(TokenObtainPairView):
    ...
