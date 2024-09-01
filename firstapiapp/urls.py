
from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.aiquest_info),
    path('single/<int:pk>', views.aiquest_individual),
    path('student/', views.get_all_students),
    path('aicreate/', views.aiquest_create),
    path('stcreate/', views.student_create),

]
