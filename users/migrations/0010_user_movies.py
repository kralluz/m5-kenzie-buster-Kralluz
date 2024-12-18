# Generated by Django 5.0 on 2023-12-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_user'),
        ('movies_orders', '0001_initial'),
        ('users', '0009_alter_user_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='movies',
            field=models.ManyToManyField(related_name='users_orders', through='movies_orders.MovieOrder', to='movies.movie'),
        ),
    ]
