from django.db import models

# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=25)
    shop_no = models.IntegerField()
    category = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
