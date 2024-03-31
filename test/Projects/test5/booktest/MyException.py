from django.http import HttpResponse
#方法1
# class MyException(object):
#     def __init__(self,get_response):
#         self.get_response = get_response
#     def __call__(self,request):
#         return self.get_response(request)
#
#     def process_exception(self,request,exception):
#         return HttpResponse(exception)

#方法2：
from django.utils.deprecation import MiddlewareMixin
class MyException(MiddlewareMixin):
    def process_exception(self, request, exception):
        return HttpResponse(exception)



