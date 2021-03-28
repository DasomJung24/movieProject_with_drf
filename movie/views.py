from rest_framework import viewsets, permissions

from .serializers import MovieSerializer, MovieDetailSerializer
from .models import *


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Movie.objects.all().prefetch_related('images')
        t = self.request.query_params.get('tag', None)
        if t:
            queryset = queryset.filter(tag=t)
        return queryset


class MovieDetailViewSet(viewsets.ModelViewSet):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
    lookup_url_kwarg = 'movie_id'
    queryset = Movie.objects.all()
