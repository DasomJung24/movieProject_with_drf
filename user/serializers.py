from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

from .models import User


class UserSignUpSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField('get_token')

    def get_token(self, user):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validate_data):
        user = self.Meta.model(**validate_data)
        user.set_password(validate_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('token', 'username', 'birth', 'phone_number', 'password', 'email', 'name', )