import asyncio
import time
"""
请编写程序实现协程的动态伸缩：当活跃协程数量⼩于5时，⾃动创建新的协程来处理任务，其他要求：
1. 每⼀个协程任务需要返回任务是否执⾏完成，且运⾏指定时间（30秒）后都会强制结束退出；
2. 程序需要动态监测协程数量，⼩于⼀定数量时需要及时补充新的协程
"""

async def task():
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
        active_tasks = len(asyncio.all_tasks())
        if active_tasks < 5:
            asyncio.create_task(task())
        await asyncio.sleep(5)  # 每5秒检测一次


async def main():
    asyncio.create_task(monitor())  # 创建监控协程
    await asyncio.sleep(300)  # 程序运行5分钟


if __name__ == "__main__":
    asyncio.run(main())

