import win32api
import win32gui,win32ui
import wx


icon_path = "imageres.dll"
icon_index = 0   # 图标在文件中的索引
large_icons, small_icons = win32gui.ExtractIconEx(icon_path, icon_index)
for icon in large_icons:
    bmp = win32ui.CreateBitmapFromHandle(icon)

    wx_bitmap = wx.BitmapFromBuffer(16, 16, bmp.GetBitmapBits(False))

    print(wx_bitmap)
    # 处理位图数据