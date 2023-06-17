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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0|wx.BORDER_NONE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )

		Main_Sizer = wx.BoxSizer( wx.VERTICAL )

		Caption_Sizer = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )

		self.Ico_Button = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )

		self.Ico_Button.SetBitmap( wx.ArtProvider.GetBitmap( wx.ART_FOLDER_OPEN, wx.ART_MENU ) )
		self.Ico_Button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.Ico_Button.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

		Caption_Sizer.Add( self.Ico_Button, 0, 0, 5 )

		self.Title_Button = wx.Button( self, wx.ID_ANY, u"Title_Text_win32", wx.DefaultPosition, wx.Size( -1,32 ), wx.BORDER_NONE )
		self.Title_Button.SetFont( wx.Font( 12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Segoe UI Variable Text" ) )
		self.Title_Button.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

		Caption_Sizer.Add( self.Title_Button, 0, 0, 5 )

		self.Space_Button = wx.Button( self, wx.ID_ANY, u"Space", wx.DefaultPosition, wx.Size( -1,32 ), wx.BORDER_NONE )
		self.Space_Button.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

		Caption_Sizer.Add( self.Space_Button, 0, 0, 5 )

		self.Minimize = wx.Button( self, wx.ID_ANY, u"–", wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )

		self.Minimize.SetBitmap( wx.NullBitmap )
		self.Minimize.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.Minimize.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

		Caption_Sizer.Add( self.Minimize, 0, 0, 5 )

		self.Maximize = wx.Button( self, wx.ID_ANY, u"▢", wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )

		self.Maximize.SetBitmap( wx.NullBitmap )
		self.Maximize.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.Maximize.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

		Caption_Sizer.Add( self.Maximize, 0, 0, 5 )

		self.Close_Button = wx.Button( self, wx.ID_ANY, u"✕", wx.DefaultPosition, wx.Size( 32,32 ), wx.BORDER_NONE )

		self.Close_Button.SetBitmap( wx.NullBitmap )
		self.Close_Button.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
		self.Close_Button.SetBackgroundColour( wx.Colour( 243, 243, 243 ) )

		Caption_Sizer.Add( self.Close_Button, 0, 0, 5 )


		Main_Sizer.Add( Caption_Sizer, 0, 0, 5 )


		self.SetSizer( Main_Sizer )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.Bind( wx.EVT_RIGHT_DOWN, self.MainOnRightDown )
		self.Space_Button.Bind( wx.EVT_LEFT_DOWN, self.OnMoveWindow )
		self.Minimize.Bind( wx.EVT_LEFT_UP, self.OnMinimizeWindow )
		self.Maximize.Bind( wx.EVT_LEFT_UP, self.OnMaximizeWindow )
		self.Close_Button.Bind( wx.EVT_LEFT_UP, self.OnCloseWindow )

	def __del__( self ):
		pass


	# Virtual event handlers, override them in your derived class
	def MainOnRightDown( self, event ):
		event.Skip()

	def OnMoveWindow( self, event ):
		event.Skip()

	def OnMinimizeWindow( self, event ):
		event.Skip()

	def OnMaximizeWindow( self, event ):
		event.Skip()

	def OnCloseWindow( self, event ):
		event.Skip()


