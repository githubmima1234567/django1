import time

HTML_ROOT_DIR = "./html"

class Aplication(object):
    """框架的核心部分，也就是框架的主题程序，框架是通用的"""
    def __init__(self,urls):
        # 设置路由信息
        self.urls = urls
    #__call__魔法方法使类可以当函数使用
    def __call__(self, environ, start_response):
        #字典中使用get取值，没有的话返回None或默认值，使用中括号没有的话会出错
        path = environ.get("PATH_INFO", "/")
        #静态文件
        if path.startswith("/static"):
            #要访问静态文件
            file_name = path[7:]
            try:
                # 打开文件
                file = open(HTML_ROOT_DIR + file_name, "rb")
            except IOError:
                status ="404 Not Found"
                headers = [ ]
                start_response(status,headers)
                return "the file is not found"
            else:
                contentdata = file.read()
                file.close()
                # 构造响应数据
                status = "200 OK"
                headers = [ ]
                start_response(status, headers)
                return contentdata.decode("utf-8")
        #py文件
        for url,handler in self.urls:
            if path == url :
                return handler(environ,start_response)
        # 代表未找到路由信息，404错误
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "the file is not found"


def ctime(environ, start_response):
    status = "200 OK"
    headers = [
        ("Content-Type", 'text/plain')
    ]
    start_response(status, headers)
    return time.ctime()

def sayhallo(environ, start_response):
    status = "200 OK"
    response_headers = [("Content-Type", 'text/plain')]
    start_response(status, response_headers)
    content = "hallo!"
    return content

def say_you(environ, start_response):
    status = "200 OK"
    response_headers = [("Content-Type", 'text/plain')]
    start_response(status, response_headers)
    content = "I love you!"
    return content

urls = [
    ("/",ctime),
    ("/ctime",ctime),
    ("/sayhallo",sayhallo),
    ("/sayyou",say_you)
]

app = Aplication(urls)





