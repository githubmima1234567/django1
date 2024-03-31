from multiprocessing import Pool
import os

def copyfile(name,oldfilename,newname):
    "完成复制功能"
    # 从旧文件中读取数据
    fr = open(oldfilename+"/"+name)
    content = fr.readlines()
    # 把数据保存在新文件中
    fw = open(newname+"/"+name,"w")
    fw.write(content)
    fw.close()
    fr.close()

#1.取文件夹名字
oldfilename = input("请输入要复制的文件夹名字：")
#2.取文件夹里面的所有文件名
oldname = os.listdir(oldfilename)
print(oldname)
#3.创建一个新文件夹
newname = oldfilename+"复制"
os.mkdir(newname)
#4.用多进程进行复制文件
pool =  Pool( )
for name in oldname:
    # print(name)
    pool.apply_async(copyfile,args=(name,oldfilename,newname))

pool.close()  # 关闭进程池
pool.join()  #

