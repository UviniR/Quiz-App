from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    # path('tlogin', views.tlogin, name='tlogin'),
    path('tlogin', LoginView.as_view(template_name='tlogin.html'),name='tlogin'),
    # path('slogin',views.slogin, name='slogin')
]