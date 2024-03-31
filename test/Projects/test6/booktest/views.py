from django.shortcuts import render
from .models import *
from django.http import JsonResponse

def index(request):
    return render(request,'booktest/index.html')

def areahandle(request):
    list = AreaInfo.objects.filter(parea__isnull=True)
    data =[]
    # [(12000, '河北省', None), (110000, '北京市', None)]
    for area in list:
        data.append([area.id,area.title])
    return JsonResponse({'data':data})

def cityhandle(request,id):
    list = AreaInfo.objects.filter(parea_id=id)
    data = []
    for area in list:
        data.append([area.id,area.title])
    return JsonResponse({'data':data})


