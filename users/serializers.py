from django.utils import timezone
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.utils.translation import ugettext as _

from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'birth', 'phone_number', 'password', )

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=32, read_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, attrs):
        email = attrs.get('email', None)
        password = attrs.get('password', None)

        if email is None:
            raise serializers.ValidationError(
                'email is required to login.'
            )

        if password is None:
            raise serializers.ValidationError(
                'password is required to login.'
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError(_('LOGIN_EMAIL_PASSWORD_WRONG'))

        if user is None:
            raise serializers.ValidationError(_('LOGIN_EMAIL_PASSWORD_WRONG'))

        if not user.check_password(password):
            raise serializers.ValidationError(_('LOGIN_EMAIL_PASSWORD_WRONG'))

        if not user.is_active:
            raise serializers.ValidationError(_('LOGIN_USER_DEACTIVATED'))

        user.last_login = timezone.now()
        user.save()

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        return user


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'name', 'birth', 'phone_number', 'email', 'name', )
