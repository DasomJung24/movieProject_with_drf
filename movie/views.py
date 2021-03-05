from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import MovieSerializer
from .models import *


class MovieViewSet(viewsets.GenericViewSet):
    serializer_class = MovieSerializer

    def list(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response({'result': serializer.data})

