from django.db import models
from django.utils.translation import gettext as _

from megabox_clone_project.models import BaseModel
from megabox_clone_project.settings import AUTH_USER_MODEL

IMAGE_MAIN = 1
IMAGE_SUB = 2
IMAGES = 3

IMAGE_CHOICES = (
    (IMAGE_MAIN, (_('메인이미지'))),
    (IMAGE_SUB, (_('서브이미지'))),
    (IMAGES, (_('나머지이미지'))),
)


class Movie(BaseModel):
    title = models.CharField(max_length=100)
    english_title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    opening_date = models.DateField(null=True, blank=True)
    running_time = models.PositiveIntegerField(null=True, blank=True)
    ticketing_rate = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, null=True, blank=True)
    audience_rating = models.ForeignKey('AudienceRating', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag')
    actor = models.ManyToManyField('Actor')
    director = models.ManyToManyField('Director')
    genre = models.ManyToManyField('Genre')
    type = models.ManyToManyField('Type')
    like_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('-ticketing_rate', 'title', '-id', )
        db_table = 'movies'

    def __str__(self):
        return self.title


class Image(BaseModel):
    movie = models.ForeignKey(Movie, related_name='images', on_delete=models.CASCADE)
    url = models.URLField()
    type = models.PositiveSmallIntegerField(choices=IMAGE_CHOICES)

    class Meta:
        db_table = 'images'


class Rating(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()

    class Meta:
        db_table = 'ratings'


class AudienceRating(models.Model):
    grade = models.CharField(max_length=20)

    class Meta:
        db_table = 'audience_ratings'


class Tag(models.Model):
    name = models.CharField(max_length=40)

    class Meta:
        db_table = 'tags'


class Actor(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'actors'


class Director(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'directors'


class Genre(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'genres'


class Type(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'types'


class Like(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='likes')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='likes')

    class Meta:
        db_table = 'likes'
        unique_together = ('movie', 'user', )
