from django.shortcuts import render
from django.http import HttpResponse
def index(request):

    return HttpResponse('hello world views1')
    # return render(request,'booktest/index.html')


def detail(request,p1,p2,p3):
    return HttpResponse(p1+p2+p3)
# def show(*args,**kwargs),第一个是位置参数，第二个是