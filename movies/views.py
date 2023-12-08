from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.serializers import MovieSerializer
from movies.permissions import MoviesRoutesPermissions
from movies.models import Movie


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [MoviesRoutesPermissions]

    def post(self, request):
        serializer = MovieSerializer(
            data=request.data, context={'request': request}
            )
        user = request.user
        self.check_object_permissions(request, user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

    def get(self, request, movie_id=None):
        if movie_id:
            movie = get_object_or_404(Movie, id=movie_id)
            serializer = MovieSerializer(movie)
            return Response(serializer.data, status=200)
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        if result_page is not None:
            serializer = MovieSerializer(result_page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=200)

    def update(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        self.check_object_permissions(request, movie)
        serializer = MovieSerializer(
            movie, data=request.data, context={'request': request}
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)

    def delete(self, request, movie_id):
        movie = get_object_or_404(Movie, id=movie_id)
        self.check_object_permissions(request, movie)
        movie.delete()
        return Response(status=204)
