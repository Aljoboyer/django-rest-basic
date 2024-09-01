from django.contrib import admin
from . models import Aiquest
from . models import Students


# Register your models here.
@admin.register(Aiquest)
class AiquestAdmin(admin.ModelAdmin):
    list_display = ['id', 'teacher_name', 'course_name', 'course_duration', 'seat']


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'st_name', 'roll', 'section', 'classname']