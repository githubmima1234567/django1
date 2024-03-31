from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^areahandle/$',views.areahandle,name='areahandle'),
    re_path(r'^cityhandle(\d+)$',views.cityhandle,name='cityhandle'),
]