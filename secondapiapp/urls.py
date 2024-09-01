
from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.shop_create),
]
