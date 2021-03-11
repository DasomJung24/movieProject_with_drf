import re
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if attrs['is_user']:
            if not attrs['account'] or not attrs['email']:
                raise serializers.ValidationError('account와 email을 입력해주세요.')
            elif not re.match(r'^.*(?=^.{8,12}$)(?=.*\d)(?=.*[a-zA-Z]).*$', attrs['account']):
                raise serializers.ValidationError('account 형식을 지켜주세요.')

        if not re.match(r'^.*(?=^.{8,15}$)(?=.*\d)(?=.*[a-zA-Z])(?=.*[!@#$%^&+=]).*$', attrs['password']):
            raise serializers.ValidationError('password 형식을 지켜주세요.')
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