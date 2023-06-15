##############################
# import
##############################
import wx
import win32api

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
