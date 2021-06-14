from django.utils import timezone
from rest_framework import permissions, generics, status
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from .serializers import MovieSerializer, MovieDetailSerializer, LikeSerializer
from .models import *


class MovieListView(generics.ListAPIView):
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.DjangoFilterBackend]
    filterset_fields = ['tag']
    queryset = Movie.objects.prefetch_related('images', 'audience_rating', 'tag')

    def get_queryset(self):
        main = self.request.query_params.get('main', None)
        title = self.request.query_params.get('title', None)
        is_open = self.request.query_params.get('is_open', None)
        active_type = self.request.query_params.get('active_type', None)

        if main:
            return self.queryset.exclude(tag__name='특별상영')[0:4]

        if active_type == 'not_open':
            order_type = self.request.query_params.get('active_order', None)
            queryset = self.queryset.filter(opening_date__gt=timezone.now().date())
            queryset = queryset.order_by('opening_date') if order_type == 'date' else queryset.order_by('title')
        elif active_type == 'special':
            queryset = self.queryset.filter(tag__name='특별상영')
        else:
            queryset = self.queryset.exclude(tag__name='특별상영')

        if title:
            return queryset.filter(title__contains=title)
        elif is_open == 'true':
            return queryset.filter(opening_date__lte=timezone.now().date())
        else:
            return queryset

    def get(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.get_queryset())
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)


class MovieDetailView(generics.RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
    lookup_url_kwarg = 'movie_id'
    queryset = Movie.objects.all()


class LikeView(CreateModelMixin, DestroyModelMixin, generics.GenericAPIView):
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
