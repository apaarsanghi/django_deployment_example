from django.urls import re_path, path
from . import views

urlpatterns = [
    re_path(r'guitarclasses', views.guitarclassespage, name='guitarclassesspage'),
    re_path(r'guitarselect', views.guitarselectpage, name='guitarselectpage'),
    re_path(r'', views.guitarindexpage, name='guitarhomepage'),
]