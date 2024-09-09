
from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.Allbook.as_view()),
    # path('book-update/<int:pk>', views.Update_Book.as_view()),

]
