from rest_framework import serializers

from .models import Movie, Image, Like


class MovieSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    audience_rating = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='grade'
    )

    def get_image(self, movie):
        if Image.objects.filter(type=1, movie=movie):
            image = Image.objects.get(type=1, movie=movie).url
        else:
            image = None
        return image

    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience_rating', 'opening_date', 'image', 'ticketing_rate', 'like_count']


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
        many=True,
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
                  'audience_rating', 'tag', 'actor', 'director', 'genre', 'type', 'images', 'like_count']


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('user_id', 'movie_id', )

    def create(self, validated_data):
        like = Like.objects.create(**validated_data)
        movie = Movie.objects.get(id=like.movie_id)
        movie.like_count += 1
        movie.save()
        return like
