from django.db import models

# Create your models here.
class games_data(models.Model):
    title = models.CharField(max_length=50)
    thumbnail = models.URLField()
    description = models.TextField()
    game_url = models.URLField()
    genre = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    release_date = models.DateField()
    storepage_url = models.URLField(null= True)

    def __str__(self) -> str:
        return f'{self.title}'


class Reviews(models.Model):
    game = models.ForeignKey(games_data, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    review_description = models.TextField()

    def __str__(self) -> str:
        return f'{self.name}'