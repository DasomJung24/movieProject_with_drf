from rest_framework import serializers

from movies.serializers import MovieDetailSerializer
from theaters.models import Theater, Screening, TheaterScreen


class TheaterSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Theater
        fields = ['id', 'city', 'name']


class TheaterScreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheaterScreen
        fields = ['id', 'theater_id', 'screen']


class ScreeningSerializer(serializers.ModelSerializer):
    movie = MovieDetailSerializer(many=False)
    theater_screen = TheaterScreenSerializer(many=False)

    class Meta:
        model = Screening
        fields = ['id', 'theater_screen', 'movie', 'started_at']

    # def get_theater_screen(self, obj):
    #     return TheaterScreen.objects.get(id=obj.theater_screen_id)


class ScreeningMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = ['movie_id']