from datetime import datetime

from django.db.models import Q
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.response import Response

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
            if datetime.strptime(date, '%Y-%m-%d').date() == timezone.now().date():
                return self.queryset.filter(
                    Q(started_at__gte=timezone.now()) &
                    Q(started_at__lte=timezone.now().date() + timezone.timedelta(days=1))
                )
            else:
                return self.queryset.filter(started_at=datetime.strptime(date, '%Y-%m-%d').date())
        return self.queryset.all()

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)