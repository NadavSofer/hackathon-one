# Generated by Django 4.2 on 2023-04-29 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('games_site_app', '0002_games_data_storepage_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('review_description', models.TextField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_site_app.games_data')),
            ],
        ),
    ]
