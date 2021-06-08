import random
from django.core.management.base import BaseCommand
from theaters.models import TheaterScreen, Theater


class Command(BaseCommand):

    help = 'this command hello'

    def add_arguments(self, parser):
        parser.add_argument('--count', default=1, type=int, help='how many time show message')

    def handle(self, *args, **options):
        theaters = [t.id for t in Theater.objects.all()]
        number = [4, 6, 8, 10]

        for t in theaters:
            n = random.choice(number)
            for i in range(1, n+1):
                TheaterScreen.objects.create(
                    theater_id=t,
                    screen=i
                )

        # {seat: [{seat: A1, status: normal, option: premium}, {seat: A2, status: normal, option: premium...

        seat_li = list()

        row = [chr(i) for i in range(65, 79)]
        number = [i for i in range(1, 23)]

        for r in row:
            for n in number:
                if n != 7 and n != 8:
                    seat = dict()
                    seat['seat'] = r + str(n)
                    seat['status'] = 'normal'
                    seat['option'] = 'normal'
                    seat_li.append(seat)

        TheaterScreen.objects.all().update(meta={'SEAT': seat_li})
