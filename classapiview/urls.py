
from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.Allbook),
    path('book-create/', views.Create_Book),
    path('book-update/<int:pk>', views.Update_Book),
    path('book-patch/<int:pk>', views.Patch_Book),

]
