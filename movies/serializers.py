from rest_framework import serializers
from movies.models import Movie, Rating


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=127)
    duration = serializers.CharField(max_length=10, default="")
    rating = serializers.ChoiceField(choices=Rating.choices, default=Rating.G)
    synopsis = serializers.CharField(max_length=255, default="")
    added_by = serializers.CharField(
        max_length=127, read_only=True, source="user.email"
    )

    def get_added_by(self, obj):
        return obj.user.email if obj.user else None

    def create(self, validated_data):
        user = self.context["request"].user
        movie = Movie.objects.create(user=user, **validated_data)
        return movie
