from django.db.models import Q
from django.utils import timezone
from rest_framework import generics, permissions

from theaters.models import Theater, Screening
from theaters.serializers import TheaterSerializer, ScreeningSerializer


class TheaterListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TheaterSerializer
    queryset = Theater.objects.select_related('city')


class ScreeningListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ScreeningSerializer
    queryset = Screening.objects.select_related('theater_screen', 'movie')

    def get_queryset(self):
        date = self.request.query_params.get('date', None)
        if date:
            if date == timezone.now().
            date += ' 00:00:00'
            return self.queryset.filter(Q(started_at__gte=timezone.now()) & Q(started_at=date))