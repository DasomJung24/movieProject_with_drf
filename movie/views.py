from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import MovieSerializer, MovieDetailSerializer
from .models import *


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        queryset = Movie.objects.all()
        t = self.request.query_params.get('type', None)
        if t:
            queryset = queryset.filter(type=t)
        return queryset


class MovieDetailViewSet(viewsets.ModelViewSet):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
    lookup_url_kwarg = 'movie_id'
    queryset = Movie.objects.all()
