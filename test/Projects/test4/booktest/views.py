from django.shortcuts import render
from .models import *
from django.http import HttpResponse
def index(request):
    # hero = HeroInfo.objects.get(pk=1)
    # context = {'hero':hero}

    list = HeroInfo.objects.filter(isDelete=True)
    context = {'list':list}
    return render(request,'booktest/index.html',context)

def show(request,id,id1):
    context = {'id':id,'id1':id1}
    return render(request,'booktest/show.html', context)


#用于模板继承

def index2(request):
    return render(request,'booktest/index2.html')
def user1(request):
    return render(request,'booktest/user1.html')

def user2(request):
    hero = HeroInfo.objects.get(pk=1)
    context = {'hero':hero}
    return render(request,'booktest/user2.html',context)

#html转义
def htmlTest(request):
    context = {'t1':'<h1>很好！</h1>'}
    return render(request,'booktest/htmlTest.html',context)

#csrf跨域访问
def csrfTest1(request):
    return render(request,'booktest/csrfTest1.html')

def csrfTest2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)
# render(request,'booktest/csrfTest2.html',{'uname':uname})