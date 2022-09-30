from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('qna',views.qna, name='qna'),
    path('summary',views.summary, name='summary'),
    path('review',views.review, name='review'),
    path('dashboard', views.dashboard, name='teacher-dashboard')

]