from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=50,
        unique=True
        )
    email = models.EmailField(
        max_length=127,
        unique=True
        )
    birthdate = models.DateField(
        null=True,
        blank=True
        )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    password = models.CharField(max_length=127)
    is_employee = models.BooleanField(default=False)
    movies = models.ManyToManyField(
        'movies.Movie',
        through='movies_orders.MovieOrder',
        related_name='users_orders'
        )
