from django.db import models

from megabox_clone_project.models import BaseModel
from megabox_clone_project.settings import AUTH_USER_MODEL


class Theater(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )
        db_table = 'theaters'

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'cities'


class TheaterScreen(BaseModel):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    is_screened = models.BooleanField()

    class Meta:
        db_table = 'theater_screens'


class Screen(models.Model):
    number = models.PositiveIntegerField()

    class Meta:
        db_table = 'screens'


class Reservation(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    theater_screen = models.ForeignKey(TheaterScreen, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7, decimal_places=1)
    name = models.CharField(max_length=50)
    birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    password = models.CharField(max_length=16)

    class Meta:
        db_table = 'reservations'


class ReservationItem(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey('TicketType', on_delete=models.CASCADE)
    seat = models.IntegerField()

    class Meta:
        db_table = 'reservation_items'


class TicketType(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=1)

    class Meta:
        db_table = 'ticket_types'
