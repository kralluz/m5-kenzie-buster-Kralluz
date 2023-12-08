from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User


class CustomJWTSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["is_superuser"] = user.is_superuser
        return token


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
        if User.objects.filter(email=validated_data.get("email")).exists():
            errors["email"] = ["email already registered."]
        if User.objects.filter(username=validated_data.get("username")).exists():
            errors["username"] = ["username already taken."]
        if errors:
            raise serializers.ValidationError(errors)
        is_employee = validated_data.get("is_employee", False)
        if is_employee:
            user = User.objects.create_superuser(**validated_data)
        else:
            user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        errors = {}
        email = validated_data.get("email")
        if email and User.objects.filter(email=email).exclude(id=instance.id).exists():
            errors["email"] = ["Email already registered."]
        username = validated_data.get("username")
        if (
            username
            and User.objects.filter(username=username).exclude(id=instance.id).exists()
        ):
            errors["username"] = ["Username already taken."]
        if errors:
            raise serializers.ValidationError(errors)
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
