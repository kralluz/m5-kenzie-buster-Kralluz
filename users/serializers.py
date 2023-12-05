from rest_framework import (serializers, )
from users.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    email = serializers.EmailField(max_length=127)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    birthdate = serializers.CharField(required=False, allow_null=True)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        errors = {}
        if User.objects.filter(email=validated_data.get('email')).exists():
            errors['email'] = ["email already registered."]
        if User.objects.filter(username=validated_data.get('username')).exists():
            errors['username'] = ["username already taken."]
        if errors:
            raise serializers.ValidationError(errors)
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            birthdate=validated_data.get('birthdate'),
            is_employee=validated_data.get('is_employee', False),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
