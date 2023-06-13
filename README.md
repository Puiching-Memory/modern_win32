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

## PlanA--重构标题栏

win32创建的标题栏可以很好地适应windows视觉效果变化。然而，它不支持黑夜模式。一种可能的方法是，隐藏默认的标题栏，然后使用wxpython控件进行替代。

优点：基于wxpython原生控件，对代码的改造和破坏最少。可相应wx事件。

缺点：依然不能摆脱GDI限制，无法实现高级窗口效果。

#### Step1-移除原有标题栏

一般来说，我们通常会这样实例化一个wx.Frame：

```python
wx.Frame.__init__( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
```

在此处，`wx.DEFAULT_FRAME_STYLE`包含了 `wx.CAPTION`等子集，见[[link](https://docs.wxpython.org/wx.Frame.html)]

我们需要做的是删除这些Flag，将其替换为0，例如：

```python
wx.Frame.init ( self, parent, id = wx.ID_ANY, title = u"Win32GUI", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = 0|wx.TAB_TRAVERSAL )
```

#### Step2-添加wx控件

标题栏通常是由一系列按钮和文本组成的横排结构，要复现它的样式，我们要创建

#### Step3-样式调整

#### Step4-绑定windows API

#### Step5-圆角窗口

Step6-黑夜模式

## PlanB--Composition API

## PlanC--openGL
