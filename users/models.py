from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from megabox_clone_project.models import BaseModel


class UserManager(BaseUserManager):
    def create_user(self, email, name, password=None, **kwargs):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email), name=name, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        user = self.create_user(email=email, password=password, name=name, )
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=32)
    birth = models.DateField(null=True)
    is_unmanned_ticket = models.BooleanField(default=True)
    is_marketing = models.BooleanField(default=False)
    receive_settings = models.JSONField(default=dict)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'name',
    ]

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.name


class FavoriteTheater(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    theater = models.ForeignKey('theaters.Theater', on_delete=models.CASCADE, related_name='favorites')

    class Meta:
        db_table = 'favorite_theaters'
        unique_together = ('theater', 'user')