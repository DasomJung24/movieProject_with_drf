from rest_framework import serializers

from .models import City, Theater


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