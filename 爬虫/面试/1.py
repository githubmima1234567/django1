import asyncio

async def my_task():
    try:
        # 模拟任务执行
        await asyncio.sleep(30)
        return True  # 任务执行完成
    except asyncio.CancelledError:
        return False  # 任务被取消

async def main():
    task = asyncio.create_task(my_task())  # 创建协程任务
    try:
        result = await asyncio.wait_for(task, timeout=30)  # 设置超时时间为30秒
    except asyncio.TimeoutError:
        task.cancel()  # 超时时取消任务
        result = False
    print("任务执行完成:", result)

asyncio.run(main())

"""
在这个示例中，my_task是一个协程任务，它模拟了一个耗时长达30秒的任务。
在main函数中，我们使用asyncio.create_task来创建这个协程任务，
并使用asyncio.wait_for设置了超时时间为30秒。如果任务在30秒内执行完成，
那么就会打印出"任务执行完成: True"；如果任务超时被强制结束，那么就会打印出"任务执行完成: False"。

这里使用asyncio.CancelledError"""
