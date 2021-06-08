from django.contrib import admin

from theaters.models import Theater, City, TheaterScreen, Screening

admin.site.register(Theater)
admin.site.register(City)
admin.site.register(TheaterScreen)
admin.site.register(Screening)
