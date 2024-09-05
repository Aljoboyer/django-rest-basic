
from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.Allmovies),
    path('movie-create/', views.Create_Movie),
    path('movie-update/<int:pk>', views.Update_Movie),
    path('movie-patch/<int:pk>', views.Patch_Movie),

]
