# Generated by Django 2.0 on 2020-04-21 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_auto_20200421_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_id',
            field=models.IntegerField(),
        ),
    ]
