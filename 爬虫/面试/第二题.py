
"""
请编写程序实现协程的动态伸缩：当活跃协程数量⼩于5时，⾃动创建新的协程来处理任务，其他要求：
1. 每⼀个协程任务需要返回任务是否执⾏完成，且运⾏指定时间（30秒）后都会强制结束退出；
2. 程序需要动态监测协程数量，⼩于⼀定数量时需要及时补充新的协程

第二题功能设计，
在main函数中，我们使用asyncio.create_task来创建这个协程任务，
monitor是创建监控协程，如果协程数量小于5时，自动创建新的协程来处理任务，
my_task是一个协程任务，它模拟了一个耗时长达30秒的任务。
并使用await asyncio.sleep(30)设置30秒内执行完成，
那么就会打印出"任务执行完成: Task done"；如果任务超时被强制结束，那么就会打印出"任务执行完成: Task cancelled"。

"""

import asyncio
async def my_task():
    """
    my_task是一个协程任务,模拟了一个耗时长达30秒的任务
    """
    try:
        print("Start task")
        await asyncio.sleep(30)  # 模拟任务执行30秒
        print("Task done")
        return True
    except asyncio.CancelledError:
        print("Task cancelled")
        return False

async def monitor():
    while True:
        active_tasks = len(asyncio.all_tasks()) #获取协程数量
        if active_tasks < 5: #当活跃协程数量⼩于5时，⾃动创建新的协程来处理任务
            asyncio.create_task(my_task())  #创建新的协程
        await asyncio.sleep(5)  # 程序需要动态监测协程数量，如：每5秒检测一次

async def main():
    asyncio.create_task(monitor())  # 创建监控协程
    await asyncio.sleep(300)  # 程序运行5分钟

if __name__ == "__main__":
    asyncio.run(main())