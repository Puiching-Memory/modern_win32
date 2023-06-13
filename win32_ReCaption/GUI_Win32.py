# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class Main
###########################################################################

class Main ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		Main_Sizer = wx.BoxSizer( wx.VERTICAL )

		Caption_Sizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Ico_Button = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		Caption_Sizer.Add( self.Ico_Button, 0, wx.ALL, 5 )

		self.Title_Text = wx.StaticText( self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Title_Text.Wrap( -1 )

		Caption_Sizer.Add( self.Title_Text, 0, wx.ALL, 5 )

		self.Minimize = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		Caption_Sizer.Add( self.Minimize, 0, wx.ALL, 5 )

		self.Maximize = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		Caption_Sizer.Add( self.Maximize, 0, wx.ALL, 5 )

		self.Close_Button = wx.Button( self, wx.ID_ANY, u"MyButton", wx.DefaultPosition, wx.DefaultSize, 0 )
		Caption_Sizer.Add( self.Close_Button, 0, wx.ALL, 5 )


		Main_Sizer.Add( Caption_Sizer, 0, 0, 5 )


		self.SetSizer( Main_Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


