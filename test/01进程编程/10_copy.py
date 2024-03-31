
from multiprocessing import Pool,Manager
import os

#该程序在ubantu上可以运行成功，在windows上运行不成功，没有完成复制功能
def copyfile(name,oldfilename,newname,q):
    "完成复制功能"
    # 从旧文件中读取数据
    fr = open(oldfilename+"/"+name)
    content = fr.readlines()
    # 把数据保存在新文件中
    fw = open(newname+"/"+name,"w")
    fw.write(content)

    fw.close()
    fr.close()
    q.put(name)
def main():
    #1.取文件夹名字
    oldfilename = input("请输入要复制的文件夹名字：")
    #2.取文件夹里面的所有文件名
    oldname = os.listdir(oldfilename)
    print(oldname)
    #3.创建一个新文件夹
    newname = oldfilename+"复制"
    os.mkdir(newname)
    #4.用多进程进行复制文件
    pool =  Pool(5 )
    q = Manager().Queue()

    for name in oldname:
        # print(name)
        pool.apply_async(copyfile, args=(name, oldfilename, newname,q))

    num = 0
    all_num = len(oldname)
    while num <all_num:
        q.get()
        num += 1
        rate = num/all_num
        print("\r进度：%.2f%%"%(rate*100),end = "")

main()
