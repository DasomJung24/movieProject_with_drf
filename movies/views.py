from django.db.models import Q
from django.utils import timezone
from rest_framework import permissions, generics, status
from django_filters import rest_framework as filters
from rest_framework.exceptions import NotFound
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin
from rest_framework.response import Response

from megabox_clone_project.utils import date_to_timezone
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
        elif is_open != 'false' and is_open != 'true':
            is_open_date = date_to_timezone(is_open) - timezone.timedelta(hours=9)
            now = timezone.now() - timezone.timedelta(hours=9)
            if is_open_date.date() == now.date():
                return queryset.filter(opening_date__lte=timezone.now().date())
            next_date = is_open_date + timezone.timedelta(hours=15)
            return self.queryset.filter(
                    Q(opening_date__gte=now) &
                    Q(opening_date__lt=next_date)
                )
        elif is_open == 'true':
            return queryset.filter(opening_date__lte=timezone.now().date())
        else:
            return queryset.all()

    def get(self, request, *args, **kwargs):
        movie_list = self.request.query_params.get('list', None)
        if not movie_list:
            page = self.paginate_queryset(self.get_queryset())
            serializer = self.get_serializer(page, many=True, context={'user': request.user})
            return self.get_paginated_response(serializer.data)
        else:
            serializer = self.serializer_class(self.get_queryset(), many=True, context={'user': request.user})
            return Response(serializer.data)


class MovieDetailView(generics.RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
    lookup_url_kwarg = 'movie_id'
    queryset = Movie.objects.prefetch_related('tag', 'genre', 'type', 'images', 'actor', 'director').all()


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
        data = {'user': request.user.id, 'movie': kwargs['movie_id']}
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
