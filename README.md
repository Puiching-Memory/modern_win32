<div align="center">

# modern_win32

#### Visual modernization guide for win32 in wxpython

#### 针对wxpython中win32的视觉效果现代化指导

#### |[中文]()|[English]()|

</div>

# 一切之前

* 作者母语为中文，其他语言的文档使用AI翻译而来，如果有错误，请通过issue向我反馈
* 请善用readme大纲
* issue反馈请带上ReadMe日期

ReadMe last Update : 2023/6/13

# 目的

wxpyhton默认创建的窗口是基于win32的，相较于win8中新增的[DirectComposition API](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437371(v=vs.85).aspx)和win10/11中广泛使用的[WinUI](https://learn.microsoft.com/zh-cn/windows/apps/winui/)来说已经落后于时代发展。

本文将作为一篇指导，寻找实现win32的现代化改造方法，最终目的是实现视觉层上的统一和代码层的通用，这意味着你可以在几乎不改变原有代码的情况下，快速改进你的GUI视觉效果。

**尽管题为win32的现代化改造，但我仍需要将范围限制在较小的范围以减小工作量。在这里，我选择wxpyhton作为例子。

# 方向

在开始工作前，我们需要了解win32与现代API（例如WinUI）所创建的窗口在视觉效果上有什么不同。

1. win32不支持暗模式（颜色主题）
2. win32使用[GDI](https://learn.microsoft.com/zh-cn/windows/win32/gdi/windows-gdi)，不支持GPU绘制
3. win32不支持动画（强行绘制性能极差）
4. win32不支持云母/亚克力/毛玻璃等高级效果（对应win11/win10/win7效果）
5. win32不能响应多点触控等现代事件

总而言之，win32不能调用GPU绘制，导致其无法实现许多高级视觉效果。

我们的主要方向是实现GPU绘制。

大致有几种方法：

* 使用openGL：wxpython支持此类调用，基于wx.glcanvas--[[link](https://docs.wxpython.org/wx.glcanvas.GLCanvas.html)]
* 使用Composition API：见微软文档--[[link](https://learn.microsoft.com/zh-cn/windows/apps/desktop/modernize/using-the-visual-layer-with-win32)]

对win32的黑夜模式支持：已有人在尝试，见<对 wxMSW 的暗模式的实验性支持>[[link](https://github.com/wxWidgets/wxWidgets/pull/23028)]

其他细节我们将逐渐完善

# 做法

## PlanA--wxpython

win32创建的标题栏可以很好地适应windows视觉效果变化。然而，它不支持黑夜模式。一种可能的方法是，隐藏默认的标题栏，然后使用wxpython控件进行替代。

优点：基于wxpython原生控件，对代码的改造和破坏最少。可相应wx事件。

缺点：依然不能摆脱GDI限制，无法实现高级窗口效果。

### Step1-移除原有标题栏

一般来说，我们通常会这样实例化一个wx.Frame：

```python
wx.Frame.__init__( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
```

在此处，`wx.DEFAULT_FRAME_STYLE`包含了 `wx.CAPTION`等子集，见[[link](https://docs.wxpython.org/wx.Frame.html)]

我们需要做的是删除这些Flag，将其替换为0，例如：

```python
wx.Frame.init ( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0|wx.TAB_TRAVERSAL )
```

### Step2-添加wx控件

标题栏通常是由一系列按钮和文本组成的横排结构，要复现它的样式，我们要创建一组对应的wx控件：

```python
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
```

这段代码做了什么？

1. 调用SetSizeHints()方法设置窗口的最小大小和最大大小。这里设置为wx.DefaultSize,意思是由wxWidgets决定大小。
2. 创建一个垂直的BoxSizer,名为Main_Sizer,用于容纳整个界面elements。
3. 创建一个水平的WrapSizer,名为Caption_Sizer,用于容纳标题栏的elements。 wx.WRAPSIZER_DEFAULT_FLAGS表示使用WrapSizer的默认样式。
4. 添加一个按钮控件Ico_Button到Caption_Sizer中,周边间距为5。
5. 添加一个静态文本控件Title_Text到Caption_Sizer中,周边间距为5。
6. 添加最小化按钮Minimize,最大化按钮Maximize和关闭按钮Close_Button到Caption_Sizer中,周边间距均为5。
7. 将Caption_Sizer添加到Main_Sizer中,上下边距为5。
8. 使用SetSizer()方法将Main_Sizer设置为窗口的主Sizer。

所以总体来说,这段代码设计了一个带有标准标题栏的窗口界面,标题栏包含图标按钮、标题文本、最小化按钮、最大化按钮和关闭按钮。整个界面使用BoxSizer和WrapSizer布局。

现在它看起来应该是这样的：![[picture1]](image/README/1686812765328.png)

### Step3-样式调整

我们将对这些控件进行调整，使他们看起来像是标题栏。设计标准参考win11设计原则--[[link](https://learn.microsoft.com/zh-cn/windows/apps/design/signature-experiences/design-principles)]

```python
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
```

有什么变化？

1. 设置了背景色self.SetBackgroundColour( wx.Colour( 249, 249, 249 ) )
2. 使用了wx.ArtProvider获取了一个文件夹图标给Ico_Button
3. 为各个按钮设置了自定义的背景色和前景色
4. 为Title_Text按钮设置了自定义字体
5. 使用Unicode字符作为最小化、最大化和关闭按钮的内容

现在它看起来是这样的：

![[img2]](image/README/1686827657547.png)

### Step4-绑定windows API/wx.event

### Step5-圆角窗口

### Step6-黑夜模式

### step7-自适应大小

### step8-窗口缩放

### Step9-高DPI支持

## PlanB--Composition API

## PlanC--openGL


https://learn.microsoft.com/zh-cn/windows/windows-app-sdk/api/winrt/microsoft.ui.windowing.appwindow?view=windows-app-sdk-1.3

https://learn.microsoft.com/zh-cn/windows/apps/desktop/modernize/using-the-visual-layer-with-win32

https://learn.microsoft.com/zh-cn/windows/apps/windows-app-sdk/windowing/windowing-overview#ui-framework-and-hwnd-interop

https://learn.microsoft.com/zh-cn/windows/apps/develop/title-bar?tabs=wasdk

https://github.com/Microsoft/xlang/tree/master/src/package/pywinrt/projection

https://github.com/wxWidgets/wxWidgets/pull/23028

https://www.cnblogs.com/validvoid/p/windows-composition-api-guide-introduction.html
