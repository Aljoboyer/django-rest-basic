
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.Allbook.as_view()),
    path('book-create/', views.Create_Book.as_view()),
    path('book-update/<int:pk>', views.Update_Book.as_view()),
    path('book-patch/<int:pk>', views.Patch_Book.as_view()),

]
