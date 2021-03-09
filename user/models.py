from django.db import models


class TimeStampedModel(models.Model):
    created_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
        ordering = ('-created_datetime',)


class User(TimeStampedModel):
    name = models.CharField(max_length=50)
    birth = models.DateField()
    phone_number = models.CharField(max_length=20, unique=True)
    account = models.CharField(max_length=50, null=True, blank=True, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True, unique=True)
    is_user = models.BooleanField(default=True)

    def __str__(self):
        return self.account


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    movie = models.ForeignKey('movie.Movie', on_delete=models.CASCADE, related_name='likes')