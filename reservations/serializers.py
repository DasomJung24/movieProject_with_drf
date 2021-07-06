from rest_framework import serializers

from theaters.models import Theater, TheaterScreen, City


class TheaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theater
        fields = ['id', 'name', ]


class ReservationMainSerializer(serializers.ModelSerializer):
    theater = serializers.SerializerMethodField('get_theaters')

    def get_theaters(self, city):
        theaters = Theater.objects.filter(city=city)
        serializer = TheaterSerializer(theaters, many=True)
        return serializer.data

    class Meta:
        model = City
        fields = ['id', 'name', 'theater', ]


class TheaterTodaySerializer(serializers.ModelSerializer):
    screen = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='number'
    )
    theater = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )
    movie = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='title'
    )

    class Meta:
        model = TheaterScreen
        fields = ['id', 'screen', 'theater', 'movies', 'start_datetime', ]