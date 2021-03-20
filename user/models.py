from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    phone_number = models.CharField(max_length=20, unique=True)

    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        db_table = 'user'


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='likes')

    class Meta:
        db_table = 'like'
