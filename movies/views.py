from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from movies.models import Movie
from movies.serializers import MovieSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.permissions import MoviesRoutesPermissions


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviesRoutesPermissions]

    def post(self, request):
        serializer = MovieSerializer(
            data=request.data, context={'request': request}
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

    def get(self, request, movie_id=None):
        if movie_id:
            try:
                movie = Movie.objects.get(id=movie_id)
                serializer = MovieSerializer(movie)
                return Response(serializer.data, status=200)
            except Movie.DoesNotExist:
                return Response({'detail': 'Not found.'}, status=404)
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=200)

    def delete(self, request, movie_id):
        try:
            movie = Movie.objects.get(id=movie_id)
            movie.delete()
            return Response(status=204)
        except Movie.DoesNotExist:
            return Response({'detail': 'Not found.'}, status=404)
