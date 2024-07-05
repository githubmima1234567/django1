'''实现第一题功能，可以使用工厂模式
创建StudentsData类，findStudent方法寻找该学生是否存在students.csv中，studentMajors方法对应专业的老师信息等
创建ProfessionalClass类，有一个creater方法，方便后续有其他专业添加，可以不修改原有代码，方便后续扩展。
'''
import csv
import random
import string

class Computer():
    """
    计算机专业的老师是张四，教室在A楼，上课时会随机⽣成2个10以内的数字m，n，并计算 m
    * 2 ^ n 的结果，打印出来
    """
    def teacher(self):
        print("老师是:张四")
    def classroomLocation(self):
        print("教室在A楼")
    def make(self):
        m = random.randint(1, 10)
        n = random.randint(1, 10)
        # print(m)
        # print(n)
        result = m * (2 ** n)
        print("上课操作的结果是：%d" % result)

class English():
    """
        英语专业的老师是李五，教室在B楼，上课时会随机⼀个⼩于26的数字m，并随机输出m个不重复
        的小写英文字⺟组成的字符串
     """
    def teacher(self):
        print("老师是:李五")
    def classroomLocation(self):
        print("教室在B楼")
    def make(self):
        m = random.randint(1, 25)
        letters = string.ascii_lowercase
        random_letters = random.sample(letters, m)
        random_string = ''.join(random_letters)
        print("上课操作的结果是：%d %s" %(m,random_string))

class Math():
    """
    数学专业的老师是王六，教室在C楼，上课时会随机⼀个3位的正整数m，并反转输出
    """
    def teacher(self):
        print("老师是:王六")
    def classroomLocation(self):
        print("教室在C楼")
    def make(self):
        m = random.randint(100, 999)
        m_str = str(m)
        m_reverse = m_str[::-1]
        print("上课操作的结果是：%s" % m_reverse)
class Literature():
    """文学专业的老师是赵七，教室在D楼，上课时会随机输出3个汉字"""
    def teacher(self):
        print("老师是:赵七")
    def classroomLocation(self):
        print("教室在D楼")
    def make(self):
        list = []
        val1 = random.randint(0x4e00, 0x9fbf)
        val2 = random.randint(0x4e00, 0x9fbf)
        val3 = random.randint(0x4e00, 0x9fbf)
        list.append(chr(val1))
        list.append(chr(val2))
        list.append(chr(val3))
        print("上课操作的结果是：%s" %str(list))
class ProfessionalClass(object):
    """
    typename:专业名称
    """
    def creater(self,typename):
        self.typename = typename
        if self.typename == "英语":
            self.major = English()
        elif self.typename == "计算机":
            self.major = Computer()
        elif self.typename == "数学":
            self.major = Math()
        elif self.typename == "文学":
            self.major = Literature()
        return self.major
class StudentsData(object):
    def __init__(self):
        self.special = ProfessionalClass()
    def studentMajors(self,typename):
        self.major=self.special.creater(typename)
        self.major.teacher()
        self.major.classroomLocation()
        self.major.make()
    def findStudent(self,name):
        with open('./students.csv', 'r') as file:    # 从csv中读取文件
            data = csv.reader(file)
            for row in data:
                if name in row:
                    special = row[1]
                    print("专业是："+special)
                    return special

if __name__ == "__main__":
    while True:
        name = input("请输入学生名字：")
        studentsdata = StudentsData()
        specialname = studentsdata.findStudent(name)
        if specialname == None:
            print("名字错误，请重新输入！")
        else:
            studentsdata.studentMajors(specialname)







