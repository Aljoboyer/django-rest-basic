from django.contrib import admin
from . models import Book
# Register your models here.
@admin.register(Book)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'genre', 'writer', 'language']