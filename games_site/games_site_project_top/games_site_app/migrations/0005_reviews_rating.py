# Generated by Django 4.2 on 2023-04-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_site_app', '0004_rename_game_id_reviews_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]