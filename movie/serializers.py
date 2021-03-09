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


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ('name', )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', )


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name', )


class AudienceRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudienceRating
        fields = ('grade', )


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('name', )


class MovieDetailSerializer(serializers.ModelSerializer):
    actor = serializers.SerializerMethodField('get_actors')
    genre = serializers.SerializerMethodField('get_genres')
    tag = serializers.SerializerMethodField('get_tags')
    type = serializers.SerializerMethodField('get_type')
    audience_rating = serializers.SerializerMethodField('get_audience_rating')
    director = serializers.SerializerMethodField('get_directors')
    images = serializers.SerializerMethodField('get_images')

    def get_images(self, movie):
        image = Image.objects.filter(movie=movie)
        serializers = ImageSerializer(image, many=True)
        return serializers.data

    def get_actors(self, movie):
        actors = Actor.objects.filter(movie=movie)
        serializers = ActorSerializer(actors, many=True)
        return serializers.data

    def get_genres(self, movie):
        genres = Genre.objects.filter(movie=movie)
        serializers = GenreSerializer(genres, many=True)
        return serializers.data

    def get_tags(self, movie):
        tags = Tag.objects.filter(movie=movie)
        serializers = TagSerializer(tags, many=True)
        return serializers.data

    def get_type(self, movie):
        types = Type.objects.filter(movie=movie)
        serializers = TypeSerializer(types, many=True)
        return serializers.data

    def get_audience_rating(self, movie):
        audience_rating = AudienceRating.objects.get(movie=movie)
        serializers = AudienceRatingSerializer(audience_rating, many=False)
        return serializers.data

    def get_directors(self, movie):
        directors = Director.objects.filter(movie=movie)
        serializers = DirectorSerializer(directors, many=True)
        return serializers.data

    class Meta:
        model = Movie
        fields = ['id', 'title', 'english_title', 'content', 'opening_date', 'running_time', 'ticketing_rate',
                  'audience_rating', 'tag', 'actor', 'director', 'genre', 'type', 'images']