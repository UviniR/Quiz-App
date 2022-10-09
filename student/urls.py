from django.urls import path
from . import views

urlpatterns = [
   path('sdashboard', views.student_d, name='sdashboard'),
   path('attempt/<int:pk>', views.attempt, name='attempt'),
   path('grades', views.grades, name='grades'),
   path('logout', views.stud_logout_view, name='logout'),
   path('calculate-marks', views.calculate_marks,name='calculate-marks')
]