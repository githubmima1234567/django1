from django.urls import re_path
# from . import views1
from . import views

urlpatterns = [

    re_path(r'^$',views.index,name='index'),
    # # re_path(r'^(\d+)/(\d+)/(\d+)$',views.detail,name='detail'),#位置参数
    re_path(r'^(?P<p3>\d+)/(?P<p2>\d+)/(?P<p1>\d+)$',views.detail,name='detail'),  #关键字参数
    # re_path(r'^$',views1.index,name='index'),
    # # re_path(r'^(\d+)/(\d+)/(\d+)$',views.detail,name='detail'),#位置参数
    # re_path(r'^(?P<p3>\d+)/(?P<p2>\d+)/(?P<p1>\d+)$',views1.detail,name='detail')  #关键字参数
    re_path(r'^getTest1/$',views.getTest1,name='getTest1'),
    re_path(r'^getTest2/$',views.getTest2,name='getTest2'),
    re_path(r'^getTest3/$',views.getTest3,name='getTest3'),
    re_path(r'^postTest1/$',views.postTest1,name='postTest1'),
    re_path(r'^postTest2/$',views.postTest2,name='postTest2'),
    re_path(r'^cookieTest/$',views.cookieTest,name='cookieTest'),
    re_path(r'^redirectTest1/$',views.redirectTest1,name='redirectTest1'),
    re_path(r'^redirectTest2/$',views.redirectTest2,name='redirectTest2'),
    re_path(r'^session1/$',views.session1,name='session1'),
    re_path(r'^session2/$',views.session2,name='session2'),
    re_path(r'^session2_handle/$',views.session2_handle,name='session2_handle'),
    re_path(r'^session3/$',views.session3,name='session3'),

]


# handler500 = 'views.server_error'