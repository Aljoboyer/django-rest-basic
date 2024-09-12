
from django.urls import path
from . import views

urlpatterns = [
    path('userList/', views.UserList.as_view()),
    path('createUser/', views.CreateUser.as_view()),

]
