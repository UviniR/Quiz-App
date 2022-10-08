from django.urls import path
from . import views

urlpatterns = [
   path('sdashboard', views.student_d, name='sdashboard'),
   path('attempt', views.attempt, name='attempt'),
   path('grades', views.grades, name='grades')
]

