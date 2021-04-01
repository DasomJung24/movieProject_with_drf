from rest_framework import viewsets, permissions
from django_filters import rest_framework as filters

from .serializers import MovieSerializer, MovieDetailSerializer
from .models import *


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['tag']
    queryset = Movie.objects.all().prefetch_related('images')


class MovieDetailViewSet(viewsets.ModelViewSet):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
    lookup_url_kwarg = 'movie_id'
    queryset = Movie.objects.all()
