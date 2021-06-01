from rest_framework import viewsets, permissions, generics, status
from django_filters import rest_framework as filters
from rest_framework.response import Response

from .serializers import MovieSerializer, MovieDetailSerializer, LikeSerializer
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


class LikeViewSet(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = Like

    def post(self, request, *args, **kwargs):
        data = {'user_id': request.user.id, 'movie_id': kwargs['movie_id']}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
