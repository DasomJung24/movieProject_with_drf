from rest_framework import serializers

from theaters.models import Theater, Screening


class TheaterSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Theater
        fields = ['id', 'city', 'name']


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = '__all__'