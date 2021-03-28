from rest_framework import serializers

from .models import Movie, Image, Actor, Genre, Tag, Type, AudienceRating, Director


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, movie):
        if Image.objects.filter(type=1, movie=movie):
            image = Image.objects.get(type=1, movie=movie).url
        else:
            image = None
        return image

    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience_rating', 'opening_date', 'image']


class MovieDetailSerializer(serializers.ModelSerializer):
    actor = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    genre = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    type = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    audience_rating = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='grade'
    )
    director = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    images = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='url'
    )

    class Meta:
        model = Movie
        fields = ['id', 'title', 'english_title', 'content', 'opening_date', 'running_time', 'ticketing_rate',
                  'audience_rating', 'tag', 'actor', 'director', 'genre', 'type', 'images']