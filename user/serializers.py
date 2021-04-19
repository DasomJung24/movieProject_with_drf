from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import User, Like


class UserSignUpSerializer(serializers.ModelSerializer):
    def create(self, validate_data):
        user = self.Meta.model(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'birth', 'phone_number', 'password', 'email', )


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        username = attrs.get('username', None)
        password = attrs.get('password', None)

        if username is None:
            raise serializers.ValidationError(
                'username is required to login.'
            )

        if password is None:
            raise serializers.ValidationError(
                'password is required to login.'
            )

        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError(
                'user is not found.'
            )

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return {'token': token}


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'birth', 'phone_number', 'password', 'email', 'name', )


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('user_id', 'movie_id', )