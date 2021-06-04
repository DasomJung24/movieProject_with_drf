from django.contrib import admin
from .models import Reservation, ReservationItem, TicketType

admin.site.register(Reservation)
admin.site.register(ReservationItem)
admin.site.register(TicketType)
