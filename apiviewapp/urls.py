
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.Allmovies),
    path('movie-create/', views.Create_Movie),
]
