from django.urls import path,re_path
from . import views

app_name = 'drums1'

urlpatterns = [
    re_path(r'drumsclasses', views.drumsclassespage, name='drumsclassespage'),
    re_path(r'drumsselect', views.drumsselectpage, name='drumsselectpage'),
    re_path(r'drumstables', views.drumstablespage, name='drumstablespage'),
    re_path(r'drumsform', views.drumsformspage, name='drumsformspage'),
    re_path(r'drumssearch', views.drumssearchpage, name='drumssearchpage'),
    re_path(r'drumsresult', views.drumsresultspage, name='drumsresultspage'),
    re_path(r'^relative/$', views.drumsrelativeurl,name='drumsrelativeurl'),
    re_path(r'^drumsregister/$', views.drumsregisterationpage, name='drumsregisterationpage'),
    re_path(r'^logout/$', views.drumsuserlogoutpage, name='drumsuserlogoutpage'),
    re_path(r'^login/$', views.drumsuserloginpage, name='drumsuserloginpage'),
    re_path(r'^home$', views.drumshomepage, name='drumshomepage'),
    re_path(r'', views.drumshomepage, name='drumshomepage'),
]