from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import MovieSerializer, MovieDetailSerializer
from .models import *


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer

    def list(self, request):
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response({'result': serializer.data})


class MovieDetailViewSet(viewsets.ModelViewSet):
    serializer_class = MovieDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=kwargs['movie_id'])
        serializer = MovieDetailSerializer(movie)
        return Response({'result': serializer.data})