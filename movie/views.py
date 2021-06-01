from rest_framework import permissions, generics, status
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from .serializers import MovieSerializer, MovieDetailSerializer, LikeSerializer
from .models import *


class MovieViewSet(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['tag']
    queryset = Movie.objects.all().prefetch_related('images', 'audience_ratings')


class MovieDetailViewSet(generics.RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
    lookup_url_kwarg = 'movie_id'
    queryset = Movie.objects.all()


class LikeViewSet(CreateModelMixin, DestroyModelMixin, generics.GenericAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
    model = Like
    queryset = Like.objects

    def get_object(self, user_id=None, movie_id=None):
        try:
            return self.queryset.get(user_id=user_id, movie_id=movie_id)
        except Like.DoesNotExist:
            raise NotFound()

    def post(self, request, *args, **kwargs):
        data = {'user_id': request.user.id, 'movie_id': kwargs['movie_id']}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        like = self.get_object(request.user.id, kwargs['movie_id'])
        movie = Movie.objects.get(id=like.movie_id)
        movie.like_count -= 1
        movie.save()
        like.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
