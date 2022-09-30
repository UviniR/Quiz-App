from django.urls import path
from . import views

urlpatterns = [
    path('create', views.create, name='create'),
    path('qna',views.qna),
    path('summary',views.summary),
    path('review',views.review)

]