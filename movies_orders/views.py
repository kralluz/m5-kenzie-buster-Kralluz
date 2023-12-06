from rest_framework.views import APIView
from rest_framework.response import Response
from movies.models import Movie
from movies_orders.serializers import Movies_orderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth.models import AnonymousUser


class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, movie_id=None):
        if movie_id:
            try:
                if isinstance(request.user, AnonymousUser):
                    return Response(status=401)
                serializer = Movies_orderSerializer(
                    data=request.data,
                    context={"request": request, "movie_id": movie_id},
                )
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=201)
            except Movie.DoesNotExist:
                return Response({"detail": "Not found."}, status=404)
