##############################
# import
##############################
import wx
import win32api,win32gui,win32con

from ctypes import OleDLL
OleDLL('shcore').SetProcessDpiAwareness(1) #high DPI support


import GUI_Win32

##############################
# GUI的函数桥接
##############################


class CalcFrame(GUI_Win32.Main):
	def __init__(self, parent):
		# 定义主函数
		GUI_Win32.Main.__init__(self, parent)

		self.SetDoubleBuffered(True)

		##close_bmp = wx.Bitmap(icon)

		##self.Close_Button.SetBitmap(close_bmp)


	def OnMaximizeWindow(self, *event):
		hWnd = self.GetHandle()

		win32gui.ReleaseCapture()
		win32api.SendMessage(hWnd, win32con.WM_SYSCOMMAND,
					win32con.SC_MAXIMIZE + win32con.HTCAPTION, 0)		

	def OnMinimizeWindow(self, *event):
		hWnd = self.GetHandle()

		win32gui.ReleaseCapture()
		win32api.SendMessage(hWnd, win32con.WM_SYSCOMMAND,
					win32con.SC_MINIMIZE + win32con.HTCAPTION, 0)
	
	def OnCloseWindow(self, *event):
		hWnd = self.GetHandle()

		win32gui.ReleaseCapture()
		re =  win32api.SendMessage(hWnd, win32con.WM_SYSCOMMAND, win32con.WM_DESTROY, 0)
		print(re)

	def OnMoveWindow(self, *event):
		""" 
		移动窗口
		----------
		hWnd: int or `sip.voidptr`
		(窗口句柄)
		"""
		hWnd = self.GetHandle()

		win32gui.ReleaseCapture()
		win32api.SendMessage(hWnd, win32con.WM_SYSCOMMAND,
					win32con.SC_MOVE + win32con.HTCAPTION, 0)

	def MainOnRightDown(self, event):
		self.Destroy()
		return super().MainOnRightDown(event)
		
##############################
# 主函数
##############################


def main():
	app = wx.App(False)
	frame = CalcFrame(None)
	frame.Show(True)
	app.MainLoop()


if __name__ == "__main__":
	main()
