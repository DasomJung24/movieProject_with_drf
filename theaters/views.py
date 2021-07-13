from collections import defaultdict

from django.db.models import Q
from django.utils import timezone
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from megabox_clone_project.utils import str_to_int, date_to_timezone
from theaters.models import Theater, Screening
from theaters.serializers import TheaterSerializer, ScreeningSerializer, ScreeningMovieSerializer


class TheaterListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = TheaterSerializer
    queryset = Theater.objects.select_related('city')

    def get(self, request, *args, **kwargs):
        original = self.request.query_params.get('original', False)
        queryset = self.get_queryset().all()
        if original:
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        else:
            default = defaultdict(list)
            for theater in queryset:
                default[theater.city.name].append({'id': theater.id, 'name': theater.name})
            return Response(default)


class ScreeningListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ScreeningSerializer
    queryset = Screening.objects.select_related(
        'theater_screen',
        'movie',
        'theater_screen__theater'
    )

    def get_queryset(self):
        movie_ids = str_to_int(self.request.query_params.getlist('movie_ids[]', []))
        theater_ids = str_to_int(self.request.query_params.getlist('theater_ids[]', []))

        date = date_to_timezone(self.request.query_params.get('date', None)) - timezone.timedelta(hours=9)
        now = timezone.now() - timezone.timedelta(hours=9)
        next_date = date + timezone.timedelta(days=1)
        q = Q(started_at__lt=next_date)

        if len(movie_ids) > 0 and len(theater_ids) == 0:
            q.add(Q(movie_id__in=movie_ids), q.AND)
        elif len(movie_ids) == 0 and len(theater_ids) > 0:
            q.add(Q(theater_screen__theater_id__in=theater_ids), q.AND)
        else:
            q.add(Q(movie_id__in=movie_ids), q.AND)
            q.add(Q(theater_screen__theater_id__in=theater_ids), q.AND)

        if date and date.date() == now.date():
            q.add(Q(started_at__gte=now), q.AND)
        elif date and date.date() != now.date():
            q.add(Q(started_at__gte=date), q.AND)

        return self.queryset.filter(q)

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_movies_for_day(request):
    date = date_to_timezone(request.GET.get('date', None)) - timezone.timedelta(hours=9)
    now = timezone.now() - timezone.timedelta(hours=9)
    next_date = date + timezone.timedelta(days=1)

    if date.date() == now.date():
        return Response(Screening.objects.filter(
            Q(started_at__gte=now) &
            Q(started_at__lt=next_date)
        ).values('movie_id').distinct().order_by('movie_id'))
    else:
        return Response(Screening.objects.filter(
            Q(started_at__gte=date) &
            Q(started_at__lt=next_date)
        ).values('movie_id').distinct().order_by('movie_id'))
