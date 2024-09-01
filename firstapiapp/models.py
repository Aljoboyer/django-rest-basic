from django.db import models

# Create your models here.
class Aiquest(models.Model):
    teacher_name = models.CharField(max_length=25)
    course_name = models.CharField(max_length=25)
    course_duration = models.IntegerField()
    seat = models.IntegerField()

class Students(models.Model):
    st_name = models.CharField(max_length=25)
    roll = models.IntegerField()
    section = models.CharField(max_length=2)
    classname = models.CharField(max_length=24)