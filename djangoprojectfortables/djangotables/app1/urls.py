from django.urls import path
from . import views

urlpatterns = [
    path('', views.app1homepage, name='app1homepage'),
]