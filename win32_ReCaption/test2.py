import wx
from win32ui import CreateBitmapf

# 创建一个PyCBitmap对象
bitmap = CreateBitmap((16, 16), 1, 24, [0]*16*16*3)
print(bitmap)

# 将PyCBitmap对象转换为wx.Bitmap对象
wx_bitmap = wx.BitmapFromBuffer(16, 16, bitmap.GetBitmapBits(True))