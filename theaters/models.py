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


class TheaterScreen(BaseModel):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    screen = models.ForeignKey('Screen', on_delete=models.CASCADE)
    movie = models.ForeignKey('movies.Movie', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    is_screened = models.BooleanField()

    class Meta:
        db_table = 'theater_screens'


class Screen(models.Model):
    number = models.PositiveIntegerField()

    class Meta:
        db_table = 'screens'
