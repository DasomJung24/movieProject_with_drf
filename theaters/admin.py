from django.contrib import admin

from theaters.models import Theater, City, TheaterScreen, Screen

admin.site.register(Theater)
admin.site.register(City)
admin.site.register(TheaterScreen)
admin.site.register(Screen)