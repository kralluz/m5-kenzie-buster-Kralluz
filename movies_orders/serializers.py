from rest_framework import serializers
from movies.models import Movie
from movies_orders.models import MovieOrder


class Movies_orderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source="movie.title")
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    purchased_at = serializers.DateTimeField(read_only=True)
    purchased_by = serializers.CharField(read_only=True, source="user.email")

    def get_purchased_by(self, obj):
        return obj.user.email if obj.user else None

    def create(self, validated_data):
        user = self.context["request"].user
        movie = Movie.objects.get(id=self.context["movie_id"])
        movies_order = MovieOrder.objects.create(
            movie=movie, user=user, **validated_data
        )
        return movies_order
