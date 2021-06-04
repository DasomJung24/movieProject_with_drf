from django.db import models

from megabox_clone_project.models import BaseModel
from megabox_clone_project.settings import AUTH_USER_MODEL


class Reservation(BaseModel):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    theater_screen = models.ForeignKey('theaters.TheaterScreen', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=7, decimal_places=1)
    name = models.CharField(max_length=50)
    date_time = models.DateTimeField()
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
