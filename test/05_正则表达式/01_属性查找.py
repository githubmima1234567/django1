class Foo(object):
    def __init__(self):
        pass
    #获取属性，没有该方法，没有的类属性会报错，有就不会报错
    def __getattr__(self, item):
        print (item,end=" ")
        return self
    #打印输出
    def __str__(self):
        return ""
    #自定义查找属性，等级最高，容易造成递归无穷尽问题
    # def __getattribute__(self, item):
    #     self.itcast = 10
    #       self.__getattribute__("itcast") #于上一句等同

print(Foo().think.different.itcast)