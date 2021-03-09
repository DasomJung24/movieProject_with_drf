import re
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if not re.match(r'^.*(?=^.{8,12}$)(?=.*\d)(?=.*[a-zA-Z]).*$', attrs['account']):
            raise serializers.ValidationError('account is not available')
        elif not re.match(r'^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$', attrs['password']):
            raise serializers.ValidationError('password is not available')
        else:
            return attrs

    def create(self, validate_data):
        user = super(UserSerializer, self).create(self.validated_data)
        user.password = make_password(self.validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('name', 'birth', 'phone_number', 'account', 'password', 'email', 'is_user', )