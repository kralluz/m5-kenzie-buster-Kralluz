# Generated by Django 5.0 on 2023-12-05 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_is_superuser_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(null=True),
        ),
    ]
