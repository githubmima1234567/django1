from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
def index(request):

    return HttpResponse('hello world')
    # return render(request,'booktest/index.html')

def detail(request,p1,p2,p3):
    return HttpResponse(p1+p2+p3)
# def show(*args,**kwargs),第一个是位置参数，第二个是

#展示链接页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')
#展示一键一值
def getTest2(request):
    a1=request.GET['a']
    b1=request.GET['b']
    c1=request.GET['c']
    context={'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html',context)
#展示一键多值
def getTest3(request):
    a1=request.GET.getlist('a')
    context={'a':a1}
    return render(request,'booktest/getTest3.html',context)

def postTest1(request):

    return render(request,'booktest/postTest1.html')

def postTest2(request):
    name1 = request.POST['name']
    pwd1 = request.POST['pwd']
    ugender1 = request.POST['ugender']
    uhobby1 = request.POST.getlist('uhobby')
    context = {'name': name1, 'pwd': pwd1, 'ugender': ugender1, 'uhobby': uhobby1}
    return render(request,'booktest/postTest2.html',context)

#cookie练习
def cookieTest(request):
    response=HttpResponse() #获取HttpResponse
    cookie=request.COOKIES  #获取cookie
    if 'h1'in cookie:
        response.write(cookie['h1'])
    # response.set_cookie('h1','123')  #设置cookie添加到HttpResponse中
    return response  #返回HttpResponse
# 从Python3.x开始，has_key() 函数被 contains(key) 函数替代。dict1.__contains__('name'))

#重定向
def redirectTest1(request):
    # return HttpResponseRedirect('/booktest/redirectTest2/')
    return redirect('/booktest/redirectTest2/')

def redirectTest2(request):
    return HttpResponse('跳转过来的页面')

def session1(request):
    # uname=None
    uname=request.session.get('myname','未登录')
    context = {'uname':uname}
    return render(request,'booktest/session1.html',context)

def session2(request):
    return render(request,'booktest/session2.html')

def session2_handle(request):
    uname = request.POST['uname']
    request.session['myname']=uname
    request.session.set_expiry(2) #设置session过期时间，整数，多少秒过期
    request.session.set_expiry(0)#关闭浏览器就过期
    request.session.set_expiry(None)#永不过期
    return redirect('/booktest/session1/')

def session3(request):
    del request.session['myname'] #删除session
    return redirect('/booktest/session1/')