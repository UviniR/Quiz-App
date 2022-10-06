from django.urls import path
from . import views

urlpatterns = [
    path('tsignup', views.tsignup, name='tsignup'),
    path('ssignup',views.ssignup, name='ssignup')
]