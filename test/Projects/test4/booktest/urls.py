from django.urls import re_path
from . import views

urlpatterns =[
    re_path(r'^index/$',views.index,name='index'),
    re_path(r'^(\d+)/(\d+)$',views.show,name='show'),
    re_path(r'^user1/$',views.user1,name='user1'),
    re_path(r'^user2/$',views.user2,name='user2'),
    re_path(r'^index2/$',views.index2,name='index2'),
    re_path(r'^htmlTest/$',views.htmlTest,name='htmlTest'),
    re_path(r'^csrfTest1/$',views.csrfTest1,name='csrfTest1'),
    re_path(r'^csrfTest2/$',views.csrfTest2,name='csrfTest2'),

]