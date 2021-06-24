from django.utils import timezone
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.utils.translation import ugettext as _

from .models import User, FavoriteTheater


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    theaters = serializers.SerializerMethodField(required=False)
    is_unmanned_ticket = serializers.BooleanField(required=False)
    is_marketing = serializers.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'name',
            'birth',
            'phone_number',
            'password',
            'is_unmanned_ticket',
            'is_marketing',
            'receive_settings',
            'theaters',
        )

    def create(self, validated_data):
        data = self.context.get('data', {})
        user = User.objects.create_user(**validated_data)
        theaters = [FavoriteTheater(theater_id=i['id'], user_id=user.id) for i in data['theaters']]

        if len(theaters) > 0:
            user.favorites.all().delete()
            FavoriteTheater.objects.bulk_create(theaters)

        return user

    def get_theaters(self, obj):
        theaters = obj.favorites.all()
        return [{'id': t.id, 'user': t.user_id, 'theater': t.theater_id} for t in theaters]


class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    name = serializers.CharField(max_length=32, read_only=True)
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)
    theaters = serializers.ListField(read_only=True, default=[])
    phone_number = serializers.CharField(read_only=True)
    birth = serializers.DateField(read_only=True)
    is_unmanned_ticket = serializers.BooleanField(read_only=True, default=True)
    is_marketing = serializers.BooleanField(read_only=True, default=False)
    receive_settings = serializers.JSONField(read_only=True, default={})
    movies = serializers.ListField(read_only=True, default=[])

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

        favorites = user.favorites.all()
        user.theaters = [{'id': i.id, 'theater_id': i.theater_id, 'name': i.theater.name} for i in favorites] \
            if favorites else []

        likes = user.likes.all()
        user.movies = [{'id': i.id, 'movie_id': i.movie_id, 'title': i.movie.title} for i in likes] \
            if likes else []

        return user


class UserSerializer(serializers.ModelSerializer):
    favorites = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'birth',
            'phone_number',
            'email',
            'name',
            'is_unmanned_ticket',
            'is_marketing',
            'receive_settings',
            'favorites',
            'likes',
        )

    def get_favorites(self, obj):
        favorites = obj.favorites.all()
        return [{'id': i.id, 'theater_id': i.theater_id, 'name': i.theater.name} for i in favorites] \
            if favorites else []

    def get_likes(self, obj):
        likes = obj.likes.all()
        return [{'id': i.id, 'movie_id': i.movie_id, 'title': i.movie.title} for i in likes] \
            if likes else []
