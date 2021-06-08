import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from movies.models import Movie
from theaters.models import Screening, TheaterScreen


class Command(BaseCommand):

    def handle(self, *args, **options):
        theaters = [t.id for t in TheaterScreen.objects.all()]
        movies = [m.id for m in Movie.objects.all()]
        times = [
            timezone.now(),
            timezone.now() + timezone.timedelta(hours=3),
            timezone.now() + timezone.timedelta(hours=6),
            timezone.now() + timezone.timedelta(hours=9),
            timezone.now() + timezone.timedelta(hours=12),
            timezone.now() + timezone.timedelta(hours=15),
            timezone.now() + timezone.timedelta(hours=18),
            timezone.now() + timezone.timedelta(hours=21),
            timezone.now() + timezone.timedelta(days=1),
            timezone.now() + timezone.timedelta(days=1, hours=3),
            timezone.now() + timezone.timedelta(days=1, hours=6),
            timezone.now() + timezone.timedelta(days=1, hours=9),
            timezone.now() + timezone.timedelta(days=1, hours=12),
            timezone.now() + timezone.timedelta(days=1, hours=15),
            timezone.now() + timezone.timedelta(days=1, hours=18),
            timezone.now() + timezone.timedelta(days=1, hours=21),
            timezone.now() + timezone.timedelta(days=2),
            timezone.now() + timezone.timedelta(days=2, hours=3),
            timezone.now() + timezone.timedelta(days=2, hours=6),
            timezone.now() + timezone.timedelta(days=2, hours=9),
            timezone.now() + timezone.timedelta(days=2, hours=12),
            timezone.now() + timezone.timedelta(days=2, hours=15),
            timezone.now() + timezone.timedelta(days=2, hours=18),
            timezone.now() + timezone.timedelta(days=2, hours=21),
            timezone.now() + timezone.timedelta(days=3),
            timezone.now() + timezone.timedelta(days=3, hours=3)
        ]
        for i in range(5):
            for t in theaters:
                movie_id = random.choice(movies)
                time = random.choice(times)
                if not Screening.objects.filter(started_at=time, theater_screen_id=t):
                    Screening.objects.create(
                        theater_screen_id=t,
                        movie_id=movie_id,
                        started_at=time
                    )