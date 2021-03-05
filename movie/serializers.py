from rest_framework import serializers

from .models import Movie, Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('url', )


class MovieSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField('get_images')

    def get_images(self, movie):
        image = Image.objects.filter(type=1, movie=movie)
        serializers = ImageSerializer(image, many=True)
        return serializers.data

    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience_rating', 'opening_date', 'images']


