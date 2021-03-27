from rest_framework import viewsets, permissions
from django.utils import timezone
from rest_framework.response import Response

from movie.models import Movie
from .models import City, TheaterScreen
from .serializers import ReservationMainSerializer


class ReservationMainViewSet(viewsets.ModelViewSet):
    serializer_class = ReservationMainSerializer
    permission_classes = [permissions.AllowAny]
    model = City

    def list(self, request, *args, **kwargs):
        cities = City.objects.all()
        screening_movie = TheaterScreen.objects.filter(start_datetime__gte=timezone.now()).values('movie').distinct()
        movie_list = [Movie.objects.get(id=m['movie']).title for m in screening_movie]
        city = ReservationMainSerializer(cities, many=True)
        return Response({'movie': movie_list, 'city': city.data})