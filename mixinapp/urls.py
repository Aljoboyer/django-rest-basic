
from django.urls import path
from . import views

urlpatterns = [
    path('userList/', views.UserList.as_view()),
    path('createUser/', views.CreateUser.as_view()),
    path('userretrive/<int:pk>', views.UserRetrive.as_view()),
    path('userUpdate/<int:pk>', views.UserUpdate.as_view()),
    path('userpatch/<int:pk>', views.UserPartialUpdate.as_view()),

]
