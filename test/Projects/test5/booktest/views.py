from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import os
from django.conf import settings
from .models import *
from django.core.paginator import *

def index(request):
    return render(request,'booktest/index.html')

def Exce(request):
    a =int('ddd')
    return HttpResponse('a')


def uploadPic(request):
    return render(request,'booktest/uploadPic.html')

def uploadPic_handle(request):
    pic1 = request.FILES['pic1']
    pic1Name=os.path.join(settings.MEDIA_ROOT,pic1.name)
    with open(pic1Name,'wb') as pic:
        for chunk in pic1.chunks():
            pic.write(chunk)
    return HttpResponse('<img src="/static/media/%s/">'%pic1.name)

def herolist(request,pindex):
    if pindex=='':
        pindex=1
    list = HeroInfo.objects.all()
    paginator = Paginator(list,4)
    page = paginator.page(int(pindex))
    context = {'page':page}
    return render(request,'booktest/herolist.html',context)

def area(request):
    return render(request,'booktest/area.html')

def area2(request,id):
    id1 = int(id)
    if id1==0:
        data=AreasInfo.objects.filter(parea__isnull=True)
    else:
        data=[{ }]
    list=[]
    for area in data:
        list.append([area.id,area.title])
    return JsonResponse({'data':list})