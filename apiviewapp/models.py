from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=35)
    genre = models.CharField(max_length=50)
    imdb = models.IntegerField()
    director = models.CharField(max_length=50)