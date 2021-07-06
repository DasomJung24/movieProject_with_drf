import random

from django.core.management.base import BaseCommand
from django.utils import timezone

from movies.models import Movie
from theaters.models import Screening, TheaterScreen


class Command(BaseCommand):

    def handle(self, *args, **options):
        theaters = [t.id for t in TheaterScreen.objects.all()]
        movies = [{'id': m.id, 'date': m.opening_date} for m in Movie.objects.all()]

        for i in range(5):
            for t in theaters:
                movie = random.choice(movies)
                movie_id, opening_date = movie['id'], movie['date']
                times = [
                    opening_date + timezone.timedelta(hours=3),
                    opening_date + timezone.timedelta(hours=6),
                    opening_date + timezone.timedelta(hours=9),
                    opening_date + timezone.timedelta(hours=12),
                    opening_date + timezone.timedelta(hours=15),
                    opening_date + timezone.timedelta(hours=18),
                    opening_date + timezone.timedelta(hours=21),
                    opening_date + timezone.timedelta(days=1),
                    opening_date + timezone.timedelta(days=1, hours=3),
                    opening_date + timezone.timedelta(days=1, hours=6),
                    opening_date + timezone.timedelta(days=1, hours=9),
                    opening_date + timezone.timedelta(days=1, hours=12),
                    opening_date + timezone.timedelta(days=1, hours=15),
                    opening_date + timezone.timedelta(days=1, hours=18),
                    opening_date + timezone.timedelta(days=1, hours=21),
                    opening_date + timezone.timedelta(days=2),
                    opening_date + timezone.timedelta(days=2, hours=3),
                    opening_date + timezone.timedelta(days=2, hours=6),
                    opening_date + timezone.timedelta(days=2, hours=9),
                    opening_date + timezone.timedelta(days=2, hours=12),
                    opening_date + timezone.timedelta(days=2, hours=15),
                    opening_date + timezone.timedelta(days=2, hours=18),
                    opening_date + timezone.timedelta(days=2, hours=21),
                    opening_date + timezone.timedelta(days=3),
                    opening_date + timezone.timedelta(days=3, hours=3)
                ]
                time = random.choice(times)
                if not Screening.objects.filter(started_at=time, theater_screen_id=t):
                    Screening.objects.create(
                        theater_screen_id=t,
                        movie_id=movie_id,
                        started_at=time
                    )