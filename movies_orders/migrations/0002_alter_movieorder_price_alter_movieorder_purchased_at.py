# Generated by Django 5.0 on 2023-12-06 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieorder',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='movieorder',
            name='purchased_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
