from django.db import models

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=35)
    genre = models.CharField(max_length=50)
    writer = models.CharField(max_length=50)
    language = models.CharField(max_length=50)