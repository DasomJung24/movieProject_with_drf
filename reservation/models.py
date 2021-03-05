from django.db import models
from user.models import TimeStampedModel


class Theater(models.Model):
    name = models.CharField(max_length=30)
    city = models.ForeignKey('City', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)


class TheaterScreen(TimeStampedModel):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE)
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    is_screened = models.BooleanField()


class Screen(models.Model):
    number = models.PositiveIntegerField()


class Reservation(TimeStampedModel):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    theater_screen = models.ForeignKey(TheaterScreen, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7, decimal_places=1)


class ReservationItem(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    ticket_type = models.ForeignKey('TicketType', on_delete=models.CASCADE)
    seat = models.IntegerField()


class TicketType(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=1)
