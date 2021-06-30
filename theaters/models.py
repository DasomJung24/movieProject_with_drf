from django.db import models

from megabox_clone_project.models import BaseModel


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


class TheaterScreen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    screen = models.PositiveIntegerField()
    meta = models.JSONField(default=dict)

    class Meta:
        db_table = 'theater_screens'


class Screening(BaseModel):
    theater_screen = models.ForeignKey(TheaterScreen, on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    started_at = models.DateTimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        db_table = 'screenings'
