from django.urls import re_path
from . import views
urlpatterns =[
    re_path(r'^$',views.index,name='index'),
    re_path(r'^Exce/$',views.Exce,name='Exce'),
    re_path(r'^uploadPic/$', views.uploadPic, name='uploadPic'),
    re_path(r'^uploadPic_handle/$', views.uploadPic_handle, name='uploadPic_handle'),
    re_path(r'^herolist/(\d*)$', views.herolist, name='herolist'),
    re_path(r'^area/$', views.area, name='area'),
    re_path(r'^area/(\d+)/$', views.area2, name='area2')
]