from rest_framework import serializers

from .models import Movie, Image, Actor, Genre, Tag, Type, AudienceRating, Director


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('url', )


class MovieSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_images')

    def get_images(self, movie):
        if Image.objects.filter(type=1, movie=movie):
            image = Image.objects.get(type=1, movie=movie)
        else:
            image = None
        serializers = ImageSerializer(image, many=False)
        return serializers.data

    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience_rating', 'opening_date', 'images']


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