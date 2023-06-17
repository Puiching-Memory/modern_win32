import asyncio
import winsdk.windows.ui.windowmanagement as wm

async def create_window():
    # 在异步上下文中创建AppWindow对象
    window = await asyncio.to_thread(wm.AppWindow.try_create_async)

    # 在异步上下文中设置窗口的标题和大小
    await asyncio.to_thread(window.put_title, "My Window")
    await asyncio.to_thread(window.request_size, (800, 600))

    # 在异步上下文中显示窗口
    await asyncio.to_thread(window.try_show)

# 运行事件循环
asyncio.run(create_window())
