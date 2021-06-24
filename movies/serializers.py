from rest_framework import serializers

from .models import Movie, Image, Like


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'movie', 'url', 'type', )


class MovieSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    audience_rating = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='grade'
    )
    user_like = serializers.SerializerMethodField(read_only=True)

    def get_user_like(self, movie):
        user = self.context.get('user', None)
        if not user.is_authenticated:
            return False

        if user.likes.filter(movie_id=movie.id):
            return True
        return False

    class Meta:
        model = Movie
        fields = [
            'id',
            'title',
            'audience_rating',
            'opening_date',
            'images',
            'ticketing_rate',
            'like_count',
            'content',
            'user_like',
        ]


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
        fields = ('user', 'movie', )

    def create(self, validated_data):
        like = Like.objects.create(**validated_data)
        movie = Movie.objects.get(id=like.movie_id)
        movie.like_count += 1
        movie.save()
        return like
