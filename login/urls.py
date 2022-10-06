from django.urls import path
from . import views

urlpatterns = [
    path('tlogin', views.tlogin, name='tlogin'),
    path('slogin',views.slogin, name='slogin')
]