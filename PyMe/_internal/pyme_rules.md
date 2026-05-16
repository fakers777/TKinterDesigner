---
description: PyMe 界面项目格式转换规范
globs: *.py
alwaysApply: true
---
# PyMe 项目生成规范
    PyMe是一个Python开发工具，用于帮助开发者创建基于tkinter的Python项目，PyMe的主要特点是:
    1、根据项目需要有一个合适的英文名称，PyMe会根据项目名称创建一个新的文件夹，文件夹名就是项目名称。
    2、每个项目是由一个或多个界面组成，每个界面由一个界面控件布局文件、一个以文件名加上后缀"_cmd.py"对应的逻辑文件、一个文件名加上后缀"_sty.py"对应的样式文件成对匹配来产生，如果工程只有一个界面，则生成界面文件“项目名.py”，逻辑文件“项目名_cmd.py”，样式文件“项目名_sty.py”。
    3、界面控件布局文件主要是加载界面控件的属性和事件信息，所有的控件信息保存在一个JSON字符串中。
    4、界面的控件逻辑文件名为界面控件布局文件名加上后缀"_cmd.py"来生成，文件主要对控件的事件触发的绑定函数进行逻辑编写。
    5、每个界面的样式文件直接使用基础结构就行，不要修改。
    6、每个项目会有一个Fun.py文件，Fun.py文件主要是存储了一些公共的函数，比如销毁UI、显示消息框等,这些函数用于在界面逻辑文件中直接调用，不用生成出来，因为PMe打开后会自动生成Fun.py文件。
    举例说明：
    以一个火车票查询工具为示例,就只有一个查询界面即可，生成的文件夹结构为：
    TrainTicket/
    ├── TrainTicket.py
    └── TrainTicket_cmd.py
    └── TrainTicket_sty.py
    └── Fun.py
    如果是需要多个界面的项目，比如一个数据库管理软件，就需要有登录界面和每一个管理页面，有两个或多个独立的界面，以保证每个界面或逻辑文件都在32K以内，生成的文件夹结构为：
    DataManager/
    ├── DataManager.py
    ├── DataManager_cmd.py
    ├── DataManager_sty.py
    ├── Login.py
    ├── Login_cmd.py
    ├── Login_sty.py
    ├── Main.py
    ├── Main_cmd.py
    ├── Main_sty.py
    ├── Fun.py
    ...

 ## 核心原则
  1. **界面-逻辑-样式分离**：每个界面都有对应的逻辑文件和样式文件
  2. **命名规范**：逻辑文件名 = 界面文件名 + "_cmd.py"，样式文件名 = 界面文件名 + "_sty.py"
  3. **文件大小限制**：单个文件控制在 32K 以内，复杂项目拆分为多个界面
  4. **Fun函数库调用原则**：逻辑文件代码实现逻辑，要参考Fun函数库文件中的全局变量、功能函数和组件类进行功能实现，确认函数是否存在，是否参数正确。

# PyMe 界面格式规范

## PyMe 界面文件格式
    PyMe 界面文件是一个Python文件，文件名就是界面的名称，文件内容主要是提供窗口框架，能加载字符串"UIJsonString"，这里面存储了界面布局信息、属性和事件绑定信息。
### 基础结构
    以登录界面为例，登录界面的文件内容参考下面代码，主要是有一个Login类，并存储了根据界面需求生成的字符串"UIJsonString"、其它信息不变，代码中保持双引号不转义：
```python
#coding=utf-8
#import libs 
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import Login_cmd
import Login_sty
import Fun
import EXUIControl
EXUIControl.FunLib = Fun
EXUIControl.G_ExeDir = Fun.G_ExeDir
EXUIControl.G_ResDir = Fun.G_ResDir
import tkinter
from   tkinter import *
import tkinter.ttk
import tkinter.font
from   PIL import Image,ImageTk

#Add your Varial Here: (Keep This Line of comments)
#Define UI Class
class  Login:
    def __init__(self,root,isTKroot = True,params=None):
        uiName = Fun.GetUIName(root,self.__class__.__name__)
        self.uiName = uiName
        Fun.Register(uiName,'UIClass',self)
        self.root = root
        self.configure_event = None
        self.isTKroot = isTKroot
        self.firstRun = True
        self.rootZoomed = False
        Fun.G_UIParamsDictionary[uiName]=params
        Fun.G_UICommandDictionary[uiName]=Login_cmd
        Fun.Register(uiName,'root',root)
        style = Login_sty.SetupStyle(isTKroot)
        self.UIJsonString = '{"Version": "1.0.0", "UIName": "Login", "Description": "", "WindowSize": [300, 160], "WindowPosition": "Center", "WindowHide": false, "WindowResizable": true, "WindowTitle": "Login", "DarkMode": false, "BorderWidth": 0, "BorderColor": "#ffffff", "DropTitle": false, "DragWindow": false, "MinSize": [0, 0], "ResolutionScaling": false, "PopupDebugDialog": false, "TransparentColor": null, "RootTransparency": 255, "ICOFile": null, "WinState": 1, "WinTopMost": false, "BGColor": "#f8f9fa", "GroupList": {}, "WidgetList": [{"Type": "Form", "Index": 1, "AliasName": "Form_1", "BGColor": "#f8f9fa", "Size": [300, 160], "PlaceInfo": null, "EventList": {"Load": "Form_1_onLoad"}}, {"Type": "Label", "Index": 2, "AliasName": "Label_1", "ParentName": "Form_1", "PlaceInfo": [20, 20, 80, 23, "nw", true, false], "Visible": true, "Size": [80, 23], "BGColor": "#f8f9fa", "Text": "账号", "FGColor": "#495057", "Font": ["Microsoft YaHei UI", 14, "normal", "roman", 0, 0]}, {"Type": "Label", "Index": 4, "AliasName": "Label_2", "ParentName": "Form_1", "PlaceInfo": [20, 50, 80, 23, "nw", true, false], "Visible": true, "Size": [80, 23], "BGColor": "#f8f9fa", "Text": "密码", "FGColor": "#495057", "Font": ["Microsoft YaHei UI", 14, "normal", "roman", 0, 0]}, {"Type": "Entry", "Index": 3, "AliasName": "Entry_1", "ParentName": "Form_1", "PlaceInfo": [120, 24, 160, 23, "nw", true, false], "Visible": true, "Size": [160, 23], "BGColor": "#FFFFFF", "BGColor_ReadOnly": "#f8f9fa", "FGColor": "#000000", "Font": ["Microsoft YaHei UI", 14, "normal", "roman", 0, 0], "InnerBorderColor": "#000000", "TipFGColor": "#888888", "Relief": "sunken"}, {"Type": "Entry", "Index": 5, "AliasName": "Entry_2", "ParentName": "Form_1", "PlaceInfo": [120, 54, 160, 23, "nw", true, false], "Visible": true, "Size": [160, 23], "BGColor": "#FFFFFF", "BGColor_ReadOnly": "#f8f9fa", "FGColor": "#000000", "Font": ["Microsoft YaHei UI", 14, "normal", "roman", 0, 0], "ShowChar": "*", "InnerBorderColor": "#000000", "TipFGColor": "#888888", "Relief": "sunken"}, {"Type": "Button", "Index": 6, "AliasName": "Button_1", "ParentName": "Form_1", "PlaceInfo": [146, 103, 60, 23, "nw", true, false], "Visible": true, "Size": [60, 23], "BGColor": "#0d6efd", "ActiveBGColor": "#0b5ed7", "Text": "确定", "FGColor": "#ffffff", "ActiveFGColor": "#ffffff", "Font": ["Microsoft YaHei UI", 14, "normal", "roman", 0, 0], "Relief": "flat", "EventList": {"Command": "Button_1_onCommand"}}, {"Type": "Button", "Index": 7, "AliasName": "Button_2", "ParentName": "Form_1", "PlaceInfo": [220, 103, 60, 23, "nw", true, false], "Visible": true, "Size": [60, 23], "BGColor": "#6c757d", "ActiveBGColor": "#5c636a", "Text": "退出", "FGColor": "#ffffff", "ActiveFGColor": "#ffffff", "Font": ["Microsoft YaHei UI", 14, "normal", "roman", 0, 0], "Relief": "flat", "EventList": {"Command": "Button_2_onCommand"}}]}'
        Form_1 = Fun.CreateUIFormJson(uiName,root,isTKroot,style,self.UIJsonString)
        #Inital all element's Data 
        Fun.InitElementData(uiName)
        #Call Form_1's OnLoad Function
        Fun.RunForm1_CallBack(uiName,"Load",Login_cmd.Form_1_onLoad)
        #Add Some Logic Code Here: (Keep This Line of comments)



        #Exit Application: (Keep This Line of comments)
        if self.isTKroot == True and Fun.GetElement(self.uiName,"root"):
            self.root.protocol('WM_DELETE_WINDOW', self.Exit)
            self.root.bind('<Configure>', self.Configure)
            if self.rootZoomed == True and isinstance(self.root,tkinter.Tk) == True:
                self.root.state("zoomed")
                Fun.SetUIState(uiName,"zoomed")
                self.rootZoomed = False
            
    def GetRootSize(self):
        return Fun.GetUIRootSize(self.uiName)
    def GetAllElement(self):
        return Fun.G_UIElementDictionary[self.uiName]
    def Escape(self,event):
        if Fun.AskBox('提示','确定退出程序？') == True:
            self.Exit()
    def Exit(self):
        if self.isTKroot == True:
            Fun.DestroyUI(self.uiName,0,'')

    def Configure(self,event):
        Form_1 = Fun.GetElement(self.uiName,'Form_1')
        if Form_1 == event.widget:
            Fun.ReDrawCanvasRecord(self.uiName)
            Fun.ResizeRoot(self.uiName,self.root,event)
        if self.root == event.widget and (self.configure_event is None or self.configure_event[2]!= event.width or self.configure_event[3]!= event.height):
            uiName = self.uiName
            self.configure_event = [event.x,event.y,event.width,event.height]
            Fun.ResizeRoot(self.uiName,self.root,event)
            Fun.ResizeAllChart(self.uiName)
            pass
#Create the root of tkinter 
if  __name__ == '__main__':
    Fun.RunApplication(Login)

```

## 界面字符串生成原则
    1、**UIJsonString格式规范**：UIJsonString为一个JSON字符串，用于存储界面布局信息，参考界面配置格式，必须去除所有空格和换行符后输出为一行并符合JSON格式规范,尤其注首尾大括号，方括号配对。
    2、**EventList格式规范**：EventList为一个字典，用于根据需求为控件增加需要的事件绑定函数，存储控件的事件和对应触发函数，事件类型参考事件类型，事件触发函数参考事件触发函数格式。
    3. **界面设计规范**：注意尺寸要合理，布局不要挤在一起,特别是如果使用LabelFrame,要注意好其它控件与LabelFrame间距，不要与LabelFrame边缘发生重叠。
    4. **AI组件使用规范**：如果使用PyMe的AI组件来实现AI对话、文生图和TTS，需要字符串中有AI组件。
    5. **控件层级设计规范**：只有在LabelFrame或Frame上放置相应的控件，才需要创建LabelFrame或Frame。子控件的ParentName属性为所属的Frame和LabelFrame的控件名称，比如有界面全局索引是2的LabelFrame或Frame,则其子控件的ParentName填写LabelFrame_2或Frame_2...
    6. **Frame和LabelFrame上的设计规范**：LabelFrame上面或内部的控件因为LabelFrame顶部是有标题文字，所以要注意与LabelFrame保持一定距离，如果控件在LabelFrame里显示不全，就调整LabelFrame的高度更多一些。
    7. **父控件名称设置规范**：注意控件的层级和位置要合理,要注意ParentName的名称为父控件的全局索引名称，也就“父控件类型_父控件在界面上的全局索引”，假设父控件Frame的索引为10，则父控件名称为Frame_10。
    8. **控件属性设置规范**：注意控件的属性设置合理，如果有中文文本，请直接用中文文本，不要使用\\u开头的 Unicode 编码。
    9. **控件文本设置规范**： 注意控件的文本大小和长度，尤其控件的文字长度大于控件宽度。


## PyMe 界面字符串UIJsonString配置格式

### 基础结构

```json
{
  "version": "1.0.0",
  "uiName": "PyMe",
  "description": "界面描述",
  "windowSize": [800, 600],
  "windowPosition": "Center",
  "windowHide": false,
  "windowResizable": false,
  "windowTitle": "",
  "darkMode": false,
  "borderWidth": 0,
  "borderColor": "#ffffff",
  "dropTitle": false,
  "dragWindow": false,
  "minSize": [0, 0],
  "resolutionScaling": false,
  "popupDebugDialog": false,
  "transparentColor": null,
  "rootTransparency": 255,
  "icoFile": null,
  "winState": 1,
  "winTopMost": false,
  "bgColor": "#ffffff",
  "groupList": {},
  "widgetList": []
}
```

## 控件类型列表

### 基础控件
1. **Form** - 窗体根控件
2. **Label** - 标签，用于显示文本
3. **Button** - 按钮
4. **LabelButton** - 按钮
5. **Entry** - 文本输入框
6. **Text** - 多行文本输入框
7. **ListBox** - 列表框
8. **ComboBox** - 组合框
9. **RadioButton** - 单选按钮
10. **CheckButton** - 复选按钮
11. **SwitchButton** - 开关按钮，点击触发 Switch 事件
12. **LabelFrame** - 带标签的框架，用于作为容器控件放置其它控件
13. **Frame** - 框架，用于作为容器控件放置其它控件
14. **Scale** - 刻度控件
15. **Slider** - 滑动条
16. **Progress** - 进度条
17. **ProgressDial** - 进度表盘
18. **SpinBox** - 数值选择框
19. **TreeView** - 树形控件
20. **ListView** - 列表控件
21. **Canvas** - 画布
22. **NoteBook** - 页签容器
23. **PanedWindow** - 分割窗格
24. **Calendar** - 日历型日期选择器
25. **DatePicker** - 下拉列表式日期选择器
26. **Navigation** - 导航条，内置文字按钮
27. **ListMenu** - 列表菜单，用于展现两级菜单

### Matplotlib 图表控件
1. **Scatter** - 散点图
2. **Line** - 直线图
3. **Curve** - 曲线图
4. **Histogram** - 直方图
5. **Bar** - 条状图
6. **Pie** - 饼图
7. **Spider** - 蜘蛛图
8. **XYZ3d** - 3D 散点图

### AI 组件
1. **AIChat** - AI 对话
2. **AIImage** - AI 文字生成图片
3. **AITTS** - 文本转语音或语音转文字

## Components 组件配置示例

### 1. 窗体 (Form)
```json
{
  "type": "Form",
  "index": 1,
  "aliasName": "Form_1",
  "bgColor": "#ffffff",
  "size": [800, 600],
  "packInfo": null
}
```

### 2. 标签 (Label)
```json
{
  "type": "Label",
  "index": 2,
  "aliasName": "Label_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 200, 30, "nw", true, false],
  "visible": true,
  "size": [200, 30],
  "bgColor": "#ffffff",
  "text": "标签文本",
  "fgColor": "#000000",
  "anchor": "w",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "tipText": "",
  "autoWrap": false,
  "state": "normal"
}
```

### 3. 按钮 (Button)
```json
{
  "type": "Button",
  "index": 3,
  "aliasName": "Button_1",
  "parentName": "Form_1",
  "placeInfo": [10, 50, 100, 35, "nw", true, false],
  "visible": true,
  "size": [100, 35],
  "bgColor": "#007bff",
  "text": "按钮",
  "fgColor": "#ffffff",
  "font": ["Arial", 12, "bold", "roman", 0, 0],
  "relief": "raised",
  "state": "normal",
  "eventList": {
    "command": "on_button_click"
  }
}
```

### 4. 输入框 (Entry)
```json
{
  "type": "Entry",
  "index": 4,
  "aliasName": "Entry_1",
  "parentName": "Form_1",
  "placeInfo": [10, 100, 200, 30, "nw", true, false],
  "visible": true,
  "size": [200, 30],
  "bgColor": "#ffffff",
  "bgColor_ReadOnly": "#CCCCCC",
  "text": "",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "showChar": "",
  "restriction": "",
  "innerBorderType": "borderline",
  "innerBorderWidth": 1,
  "state": "normal",
  "eventList": {
    "textChanged": "on_text_changed"
  }
}
```

### 5. 多行文本框 (Text)
```json
{
  "type": "Text",
  "index": 5,
  "aliasName": "Text_1",
  "parentName": "Form_1",
  "placeInfo": [10, 150, 400, 200, "nw", true, false],
  "visible": true,
  "size": [400, 200],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "autoWrap": true,
  "state": "normal"
}
```

### 6. 列表框 (ListBox)
```json
{
  "type": "ListBox",
  "index": 6,
  "aliasName": "ListBox_1",
  "parentName": "Form_1",
  "placeInfo": [10, 200, 200, 150, "nw", true, false],
  "visible": true,
  "size": [200, 150],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "selectMode": "BROWSE",
  "textList": ["选项 1", "选项 2", "选项 3"],
  "eventList": {
    "listboxSelect": "on_listbox_select"
  }
}
```

### 7. 组合框 (ComboBox)
```json
{
  "type": "ComboBox",
  "index": 7,
  "aliasName": "ComboBox_1",
  "parentName": "Form_1",
  "placeInfo": [10, 250, 200, 30, "nw", true, false],
  "visible": true,
  "size": [200, 30],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "textList": ["选项 1", "选项 2", "选项 3"],
  "state": "readonly",
  "eventList": {
    "comboboxSelected": "on_combobox_selected"
  }
}
```

### 8. 单选按钮 (RadioButton)
```json
{
  "type": "RadioButton",
  "index": 8,
  "aliasName": "RadioButton_1",
  "parentName": "Form_1",
  "placeInfo": [10, 300, 100, 25, "nw", true, false],
  "visible": true,
  "size": [100, 25],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "text": "选项 1",
  "value": "option1",
  "groupID": "Group_1",
  "state": "normal",
  "eventList": {
    "command": "on_radio_change"
  }
}
```

### 9. 复选按钮 (CheckButton)
```json
{
  "type": "CheckButton",
  "index": 9,
  "aliasName": "CheckButton_1",
  "parentName": "Form_1",
  "placeInfo": [10, 340, 100, 25, "nw", true, false],
  "visible": true,
  "size": [100, 25],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "text": "复选框",
  "value": false,
  "state": "normal",
  "eventList": {
    "command": "on_check_change"
  }
}
```

### 10. 开关按钮 (SwitchButton)
```json
{
  "type": "SwitchButton",
  "index": 10,
  "aliasName": "SwitchButton_1",
  "parentName": "Form_1",
  "placeInfo": [10, 380, 80, 30, "nw", true, false],
  "visible": true,
  "size": [80, 30],
  "shape": "circular",
  "bgColor_Off": "#333333",
  "text_Off": "",
  "fgColor_Off": "#FFFFFF",
  "btnColor_Off": "#2F9F00",
  "bgColor_On": "#2F9F00",
  "text_On": "",
  "fgColor_On": "#FFFFFF",
  "btnColor_On": "#FFFFFF",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "value": false,
  "switchMode": 0,
  "state": "normal",
  "eventList": {
    "switch": "on_switch_change"
  }
}
```

### 11. 滑块 (Slider)
```json
{
  "type": "Slider",
  "index": 11,
  "aliasName": "Slider_1",
  "parentName": "Form_1",
  "placeInfo": [10, 420, 200, 30, "nw", true, false],
  "visible": true,
  "size": [200, 30],
  "minValue": 0,
  "maxValue": 100,
  "currValue": 50,
  "bgColor1": "#808080",
  "bgColor2": "#808080",
  "btnColor": "#007bff",
  "eventList": {
    "valueChanged": "on_slider_change"
  }
}
```

### 12. 进度条 (Progress)
```json
{
  "type": "Progress",
  "index": 12,
  "aliasName": "Progress_1",
  "parentName": "Form_1",
  "placeInfo": [10, 460, 200, 25, "nw", true, false],
  "visible": true,
  "size": [200, 25],
  "orient": "horizontal",
  "mode": "determinate",
  "maxValue": 100,
  "value": 75,
  "roundCorner": 0
}
```

### 13. 数值选择框 (SpinBox)
```json
{
  "type": "SpinBox",
  "index": 13,
  "aliasName": "SpinBox_1",
  "parentName": "Form_1",
  "placeInfo": [10, 500, 100, 30, "nw", true, false],
  "visible": true,
  "size": [100, 30],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "from": 0,
  "to": 100,
  "increment": 1,
  "wrap": false,
  "valueList": [],
  "value": 50,
  "relief": "sunken",
  "state": "normal"
}
```

### 14. 树形控件 (TreeView)
```json
{
  "type": "TreeView",
  "index": 14,
  "aliasName": "TreeView_1",
  "parentName": "Form_1",
  "placeInfo": [300, 10, 250, 300, "nw", true, false],
  "visible": true,
  "size": [250, 300],
  "selectMode": "BROWSE",
  "iconList": [],
  "treeItemList": [
    ["根节点 1", "value1", "", "", null, []],
    ["根节点 2", "value2", "", "", null, [
      ["子节点 1", "subvalue1", "", "", null, []],
      ["子节点 2", "subvalue2", "", "", null, []]
    ]]
  ],
  "treeExpand": true,
  "eventList": {
    "treeviewSelect": "on_tree_select",
    "treeviewOpen": "on_tree_open",
    "treeviewClose": "on_tree_close"
  }
}
```

### 15. 列表视图 (ListView)
```json
{
  "type": "ListView",
  "index": 15,
  "aliasName": "ListView_1",
  "parentName": "Form_1",
  "placeInfo": [300, 320, 400, 200, "nw", true, false],
  "visible": true,
  "size": [400, 200],
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "selectMode": "EXTENDED",
  "columnList": [
    ["名称", "center", 150, true],
    ["值", "e", 100, true],
    ["描述", "w", 150, true]
  ],
  "eventList": {
    "cellClicked": "on_cell_click",
    "cellDoubleClicked": "on_cell_double_click"
  }
}
```

### 16. 页签容器 (NoteBook)
```json
{
  "type": "NoteBook",
  "index": 16,
  "aliasName": "NoteBook_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 500, 400, "nw", true, false],
  "visible": true,
  "size": [500, 400],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "selectedBGColor": "#ffffff",
  "selectedFGColor": "#000000",
  "closebtn": false,
  "btnPosition": "top",
  "pageList": [
    ["页面 1", "icon1.png", "page1.py"],
    ["页面 2", "icon2.png", "page2.py"]
  ],
  "eventList": {
    "notebookTabChanged": "on_tab_change"
  }
}
```

### 17. 画布 (Canvas)
```json
{
  "type": "Canvas",
  "index": 17,
  "aliasName": "Canvas_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 400, 300, "nw", true, false],
  "visible": true,
  "size": [400, 300],
  "bgColor": "#ffffff",
  "relief": "sunken",
  "eventList": {
    "clickXY": "on_canvas_click"
  }
}
```

### 18. 日历 (Calendar)
```json
{
  "type": "Calendar",
  "index": 18,
  "aliasName": "Calendar_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 250, 200, "nw", true, false],
  "visible": true,
  "size": [250, 200],
  "bgColor": "#ffffff",
  "relief": "solid",
  "datebarBGColor": "#007bff",
  "datebarFGColor": "#ffffff",
  "selectedBGColor": "#dddddd",
  "selectedFGColor": "#000000",
  "yearRange": [2020, 2030],
  "eventList": {
    "selectDate": "on_date_select"
  }
}
```

### 19. 日期选择器 (DatePicker)
```json
{
  "type": "DatePicker",
  "index": 19,
  "aliasName": "DatePicker_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 200, 30, "nw", true, false],
  "visible": true,
  "size": [200, 30],
  "bgColor": "#ffffff",
  "fgColor": "#000000",
  "font": ["Arial", 12, "normal", "roman", 0, 0],
  "calendarBGColor": "#ffffff",
  "selectedBGColor": "#007bff",
  "selectedFGColor": "#ffffff",
  "yearRange": [2020, 2030],
  "separatorChar": "-",
  "relief": "sunken",
  "eventList": {
    "selectDate": "on_date_select"
  }
}
```

### 20. 导航条 (Navigation)
```json
{
  "type": "Navigation",
  "index": 20,
  "aliasName": "Navigation_1",
  "parentName": "Form_1",
  "placeInfo": [0, 0, 800, 50, "nw", true, false],
  "visible": true,
  "size": [800, 50],
  "orient": "horizontal",
  "anchor": "",
  "compound": "left",
  "borderWidth": 20,
  "borderHeight": 20,
  "spacing": 10,
  "innerSpacing": 10,
  "roundCorner": 6,
  "bgColor": "#EFEFEF",
  "itemBGColor": "#EFEFEF",
  "itemFGColor": "#000000",
  "itemFont": ["Arial", 12, "normal", "roman", 0, 0],
  "itemBGColor_Hover": "#FFFFFF",
  "itemFGColor_Hover": "#000000",
  "itemFont_Hover": ["Arial", 12, "bold", "roman", 0, 0],
  "itemBGColor_Click": "#DDDDDD",
  "itemFGColor_Click": "#000000",
  "itemList": [
    ["首页", "home.png", "home.py"],
    ["设置", "settings.png", "settings.py"]
  ]
}
```

### 21. 分割窗格 (PanedWindow)
```json
{
  "type": "PanedWindow",
  "index": 21,
  "aliasName": "PanedWindow_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 600, 400, "nw", true, false],
  "visible": true,
  "size": [600, 400],
  "orient": "horizontal",
  "showhandle": true,
  "sashrelief": "raised",
  "sashwidth": 5,
  "window1Place": [0, 0, 300, 400],
  "window1UI": "left_panel.py",
  "window2Place": [305, 0, 295, 400],
  "window2UI": "right_panel.py"
}
```

### 22. 散点图 (Scatter)
```json
{
  "type": "Scatter",
  "index": 22,
  "aliasName": "Scatter_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 500, 400, "nw", true, false],
  "visible": true,
  "size": [500, 400],
  "title": "散点图标题",
  "xLabel": "X 轴",
  "yLabel": "Y 轴",
  "externalBG": "#FFFFFF",
  "internalBG": "#EAEAF2",
  "color": "#4C72B0",
  "marker": "o"
}
```

### 23. AI 对话 (AIChat)
```json
{
  "type": "AIChat",
  "index": 23,
  "aliasName": "AIChat_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 400, 500, "nw", true, false],
  "visible": true,
  "size": [400, 500],
  "xy": [10, 10],
  "usage": "post",
  "base_url": "https://api.example.com",
  "api_key": "your-api-key",
  "model_name": "gpt-3.5-turbo"
}
```

### 24. AI 图像生成 (AIImage)
```json
{
  "type": "AIImage",
  "index": 24,
  "aliasName": "AIImage_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 400, 500, "nw", true, false],
  "visible": true,
  "size": [400, 500],
  "xy": [10, 10],
  "usage": "post",
  "base_url": "https://api.example.com",
  "api_key": "your-api-key",
  "model_name": "dall-e-3"
}
```

### 25. AI 语音 (AITTS)
```json
{
  "type": "AITTS",
  "index": 25,
  "aliasName": "AITTS_1",
  "parentName": "Form_1",
  "placeInfo": [10, 10, 400, 300, "nw", true, false],
  "visible": true,
  "size": [400, 300],
  "xy": [10, 10],
  "usage": "post",
  "base_url": "https://api.example.com",
  "api_key": "your-api-key",
  "model_name": "tts-1"
}
```

## 事件类型 
  事件以tkinter的事件格式为准，但增加了下面一些自定义事件：
  事件名称	触发时机	适用控件
  Load	窗体加载时	Form
  Exit	退出时	Form, Exit
  Command	命令执行时	Button, CheckButton, RadioButton
  TextChanged	文本改变时	Entry
  LeftIconClicked	左图标点击时	Entry
  RightIconClicked	右图标点击时	Entry
  Switch	开关切换时	Switch
  ValueChanged	值改变时	Slider
  ListboxSelect	列表框选择时	ListBox
  ComboboxSelected	下拉框选择时	ComboBox
  TreeviewSelect	树视图选择时	TreeView
  TreeviewOpen	树视图打开时	TreeView
  TreeviewClose	树视图关闭时	TreeView
  PageClick	页面点击时	SwitchPage
  ClickXY	点击XY坐标时	Canvas
  Timer	定时器触发时	Timer
  SelectDate	选择日期时	DateTimePicker
  SelectTime	选择时间时	DateTimePicker
  NotebookTabChanged	页面改变时	Notebook
  CellClicked	单元格点击时	ListView
  CellDoubleClicked	单元格双击时	ListView
  HeadingClicked	标题点击时	ListView


  
## 事件触发函数格式
  事件触发函数的名称一般为"控件名称_事件类型",根据不同的事件绑定不同的参数.
  有event参数的事件触发函数的参数,则事件触发函数的定义格式为：
  def 触发函数(event,uiName,widgetName,threadings=0):
    # 事件触发时执行的代码

  没有event参数的事件触发函数的参数数,则事件触发函数的定义格式为：
  def 触发函数(uiName,widgetName,threadings=0):
    # 事件触发时执行的代码

  自定义事件的触发函数参数的数量根据事件类型的不同而不同.具体参考如下：
  1、"def Entry_1_onTextChanged(uiName,widgetName,text,threadings=0)"
  2、"def ListBox1_onListboxSelect(event,uiName,widgetName,tabIndex,threadings=0)"
  3、"def ComboBox1_onComboboxSelected(event,uiName,widgetName,value,threadings=0)"
  4、"def TreeView1_onTreeviewSelect(event,uiName,widgetName,value,threadings=0)"
  5、"def TreeView1_onTreeviewOpen(event,uiName,widgetName,value,threadings=0)"
  6、"def TreeView1_onTreeviewClose(event,uiName,widgetName,value,threadings=0)"
  7、"def ListView1_onHeadingClicked(uiName,widgetName,columnname,threadings=0)"
  8、"def ListView1_onCellClicked(uiName,widgetName,rowIndex,columnIndex,threadings=0)"
  9、"def ListView1_onCellDoubleClicked(uiName,widgetName,rowIndex,columnIndex,threadings=0)"
  10、"def SwitchPage1_onPageClick(uiName,widgetName,pageIndex,pageTitle,targetPage,threadings=0)"
  11、"def Canvas1_onClickXY(uiName,widgetName,x,y,threadings=0)"
  12、"def Timer1_onTimer(uiName,widgetName,threadings=0)"
  13、"def Form1_onLoad(uiName,threadings=0)"
  14、"def DatePicker1_onSelectDate(uiName,widgetName,date,threadings=0)"
  15、"def Form1_onExit(uiName,threadings=0)"
  16、"def Navigation1_onItemSelect(uiName,widgetName,itemText,itemValue,threadings=0)"
  17、"def NoteBook1_onTabChange(uiName,widgetName,tabIndex,tabTitle,threadings=0)"
  18、"def SwitchButton1_onSwitch(uiName,widgetName,value,threadings=0)"
  19、"def Slider1_onValueChanged(uiName,widgetName,value,threadings=0)"
  20、"def SpinBox1_onValueChanged(uiName,widgetName,value,threadings=0)"
  21、"def Progress1_onValueChanged(uiName,widgetName,value,threadings=0)"
  22、"def ProgressDial1_onValueChanged(uiName,widgetName,value,threadings=0)"
```python

def 事件名称_触发函数(event):
    # 事件触发时执行的代码
```

- **事件名称**：根据事件类型的小写形式命名，例如 `command_click`、`text_changed` 等。
- **event**：事件参数，根据事件类型的定义传递。

## 位置信息 (PlaceInfo) 格式

```json
"placeInfo": [x, y, width, height, anchor, visible, lock_code]
```

- **x**: 控件左上角 x 坐标
- **y**: 控件左上角 y 坐标
- **width**: 控件宽度 (空字符串''表示自适应)
- **height**: 控件高度 (空字符串''表示自适应)
- **anchor**: 锚点位置 ("nw", "ne", "sw", "se", "center")
  - nw: 以窗口左上角为基准
  - ne: 以窗口右上角为基准
  - sw: 以窗口左下角为基准
  - se: 以窗口右下角为基准
  - center: 以控件中心点为基准
- **visible**: 是否可见 (true/false)
- **lock_code**: 是否锁定 (true/false)

## 字体格式

```json
"font": [family, size, weight, slant, underline, overstrike]
```

- **family**: 字体名称，如 "Arial", "宋体"
- **size**: 字体大小
- **weight**: 粗细 ("normal", "bold")
- **slant**: 倾斜 ("roman", "italic")
- **underline**: 下划线 (0 或 1)
- **overstrike**: 删除线 (0 或 1)

## 分组 (GroupList) 配置

用于 RadioButton 分组：

```json
"groupList": {
  "Group_1": "option1",
  "Group_2": "yes"
}
```

## 使用说明

### 在 Trae 中使用
1. 将 Python 代码根据功能转换为 PyMe 界面项目。
2. 按照上述 JSON 格式作为 UIJsonString 生成界面文件内容。
3. 每个控件必须严格按照 JSON 格式中的属性定义，不能缺少或多写属性。
4. 事件处理函数需要在 eventList 中声明

### 转换规则
1. tkinter 的 Tk 根窗口 → Form 控件
2. tkinter 的 Label → Label 控件
3. tkinter 的 Button → Button 控件
4. tkinter 的 Entry → Entry 控件
5. tkinter 的 Text → Text 控件
6. tkinter 的 Listbox → ListBox 控件
7. tkinter 的 Combobox → ComboBox 控件
8. tkinter 的 Radiobutton → RadioButton 控件
9. tkinter 的 Checkbutton → CheckButton 控件
10. tkinter 的 Scale → Scale 控件
11. tkinter 的 Canvas → Canvas 控件
12. tkinter 的 Treeview → TreeView 控件
13. tkinter 的 Notebook → NoteBook 控件
14. tkinter 的 PanedWindow → PanedWindow 控件

### 注意事项
1. 所有颜色必须使用 16 进制色值 (如 "#ffffff")，不能使用颜色名称
2. 没有透明色概念
3. 控件索引必须是唯一递增的，从 1 开始
4. 父控件名称使用"类型_索引"格式，如"Form_1", "LabelFrame_2"
5. 事件函数名称需要在 eventList 中声明对应关系
6. 控件的parentName 必须是已存在的控件名称，不能是不存在的控件名称，父控件如果是放在Frame或LabelFrame等容器控件中 ，则parentName 必须是Frame或LabelFrame等容器控件的名称。
7. 如果一个Frame或LabelFrame,但界面没有控件指定 parentName 为当前Frame或LabelFrame控件，就不应该创建出当前Frame或LabelFrame控件。


# Fun函数库文件说明
  Fun函数库文件是PyMe的基础函数库，包含了PyMe开发中提供的全局变量、功能函数和一些组件类，如获取控件文本、设置控件文本、显示消息框等，文件由PyMe生动生成，不可修改，下面是Fun函数库文件的基础结构和包括的函数列表，用于生成逻辑代码时调用：
# Fun 函数库中的变量、函数和类

## 1. 全局变量

| 变量名 | 类型 | 初始值 | 描述 |
|-------|------|-------|------|
| G_TKRoot | NoneType | None | 根窗口实例 |
| G_TKKey | list | [] | 键盘事件列表 |
| G_RootSize | NoneType | None | 根窗口大小 |
| G_UIScale | float | 1.0 | UI 缩放比例 |
| G_UserVarDict | dict | {} | 用户变量字典 |
| G_TopDialog | NoneType | None | 顶层对话框 |
| G_LaunchDlg | NoneType | None | 启动对话框 |
| G_ResourcesFileList | dict | {} | 资源文件列表 |
| G_EventFunctionThreadDict | dict | {} | 事件函数线程字典 |
| G_CutContent | NoneType | None | 剪切内容 |
| G_FlaskReturnContent | NoneType | None | Flask 返回内容 |
| G_UrlUILoadDictionary | dict | {} | URL UI 加载字典 |
| G_UrlParamMessageBox | NoneType | None | URL 参数消息框 |
| G_TargetUIName | NoneType | None | 目标 UI 名称 |
| G_WindowDraggable | NoneType | None | 窗口可拖动状态 |
| G_AppID | str | '' | 应用 ID |
| G_AppSecret | str | '' | 应用密钥 |
| G_PrintFunctionMode | bool | False | 函数调用打印模式 |

## 2. 工具函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| GetPKGResources | ResourcePathName | 资源路径 | 获取打包后的配置文件路径 |
| PrintFunctionInfo | TargetFunction, args=[] | 无 | 函数调用打印 |
| IsInt | text | bool | 是否是整数字符串 |
| IsFloat | text | bool | 是否是浮点字符串 |
| IsNumeric | text | bool | 是否是数字字符串 |
| IsAlphanumeric | text | bool | 是否是字母或数字 |
| CheckSpecialChar | text | bool | 是否包含特殊字符 |
| IsMobilePhone | text | bool | 是否是手机号 |
| IsEmail | text | bool | 是否是 Email |
| RandNumber | begin=0, end=100 | int | 获取 0~100 的随机数字 |
| GetCurrTime | splitChar=':' | str | 获取当前时间字符串 |
| GetCurrDate | splitChar=':' | str | 获取当前日期字符串 |
| Sleep | second=1 | 无 | 等待指定秒数 |
| OutputProcessToText | cmdText, uiName, elementName | 无 | 运行命令并输出到文本控件 |
| EventFunction_Adaptor | fun, **params | 无 | 重新定义消息映射函数，自定义参数 |
| EventTwoFunction_Adaptor | fun1, fun2, **params | 无 | 重新定义消息映射函数，支持两个函数 |
| CommandFunction_Adaptor | fun, uiName, widgetName | 无 | 重新定义消息映射函数，带界面和控件参数 |
| GetParentCallFunc | 无 | [函数名称, 参数列表] | 获取堆栈中上层调用函数的名称和参数 |

## 3. 界面管理函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| GetUIName | root, className | 界面名称 | 取得界面名称 |
| GetUIParams | uiName | 界面参数 | 取得界面参数 |
| Register | uiName, elementName, element, alias=None, groupName=None, styleName=None | 无 | 注册一个控件，用于记录它 |
| SetTitleBar | root, titleText='', isDarkMode=False, isDropTitle=False | 无 | 设置标题文字及暗色 |
| PlayDestroyDialogAction | uiName, result, topLevel, animation='zoomout' | 无 | 播放窗口消失动画 |
| DestroyUI | uiName, result=0, animation='' | 无 | 销毁一个界面 |
| SetCursor | uiName, elementName, cursor='hand2' | 无 | 设置控件光标 |
| HideCursor | uiName | 无 | 隐藏控件光标 |
| GetCursorPosition | uiName='', elementName='root' | 光标位置 | 取得当前光标位置 |
| GetElement | uiName, elementName | 控件实例 | 取得控件实例，不是取得控件的值或文本 |
| GetElementName | element, isAliasName=True | [界面类名, 控件名称] 或别名 | 取得控件的界面类名与控件名称 |
| DestroyElement | uiName, elementName | 无 | 删除指定的控件 |
| GenNewElementName | uiName, elementType | 新生成的控件名称 | 取得新生成的控件名称 |

## 4. 控件创建函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| CreateLabel | uiName, parentName='Form_1', elementName='' | 创建的 Label 控件实例 | 创建 Label 控件 |
| CreateButton | uiName, parentName='Form_1', elementName='' | 创建的 Button 控件实例 | 创建 Button 控件 |
| CreateLabelButton | uiName, parentName='Form_1', elementName='' | 创建的 LabelButton 控件实例 | 创建 LabelButton 控件 |
| CreateEntry | uiName, parentName='Form_1', elementName='' | 创建的 Entry 控件实例 | 创建 Entry 控件 |
| CreateText | uiName, parentName='Form_1', elementName='' | 创建的 Text 控件实例 | 创建 Text 控件 |
| CreateListBox | uiName, parentName='Form_1', elementName='' | 创建的 ListBox 控件实例 | 创建 ListBox 控件 |
| CreateComboBox | uiName, parentName='Form_1', elementName='' | 创建的 ComboBox 控件实例 | 创建 ComboBox 控件 |
| CreateRadioButtonGroup | uiName, parentName='Form_1', groupName='', defaultValue=1 | 创建的 RadioButtonGroup 控件实例 | 创建 RadioButtonGroup 控件 |
| CreateRadioButton | uiName, parentName='Form_1', elementName='', groupName='', defaultValue=1, style='indicatoron' | 创建的 RadioButton 控件实例 | 创建 RadioButton 控件 |
| CreateCheckButton | uiName, parentName='Form_1', elementName='', defaultValue=False, style='indicatoron' | 创建的 CheckButton 控件实例 | 创建 CheckButton 控件 |
| CreateSwitchButton | uiName, parentName='Form_1', elementName='' | 创建的 SwitchButton 控件实例 | 创建 SwitchButton 控件 |
| CreateLabelFrame | uiName, parentName='Form_1', elementName='' | 创建的 LabelFrame 控件实例 | 创建 LabelFrame 控件 |
| CreateFrame | uiName, parentName='Form_1', elementName='' | 创建的 Frame 控件实例 | 创建 Frame 控件 |
| CreateCanvas | uiName, parentName='Form_1', elementName='' | 创建的 Canvas 控件实例 | 创建 Canvas 控件 |
| CreateScale | uiName, parentName='Form_1', elementName='', orient=tkinter.HORIZONTAL | 创建的 Scale 控件实例 | 创建 Scale 控件 |
| CreateSlider | uiName, parentName='Form_1', elementName='', orient=tkinter.HORIZONTAL | 创建的 Slider 控件实例 | 创建 Slider 控件 |
| CreateProgress | uiName, parentName='Form_1', elementName='', orient=tkinter.HORIZONTAL | 创建的 Progress 控件实例 | 创建 Progress 控件 |
| CreateProgressDial | uiName, parentName='Form_1', elementName='' | 创建的 ProgressDial 控件实例 | 创建 ProgressDial 控件 |
| CreateSpinBox | uiName, parentName='Form_1', elementName='' | 创建的 SpinBox 控件实例 | 创建 SpinBox 控件 |
| CreateTreeView | uiName, parentName='Form_1', elementName='' | 创建的 TreeView 控件实例 | 创建 TreeView 控件 |
| CreateListView | uiName, parentName='Form_1', elementName='' | 创建的 ListView 控件实例 | 创建 ListView 控件 |
| CreateNoteBook | uiName, parentName='Form_1', elementName='' | 创建的 NoteBook 控件实例 | 创建 NoteBook 控件 |
| CreatePanedWindow | uiName, parentName='Form_1', elementName='', orient=tkinter.HORIZONTAL | 创建的 PanedWindow 控件实例 | 创建 PanedWindow 控件 |
| CreateCalendar | uiName, parentName='Form_1', elementName='' | 创建的 Calendar 控件实例 | 创建 Calendar 控件 |
| CreateDatePicker | uiName, parentName='Form_1', elementName='' | 创建的 DatePicker 控件实例 | 创建 DatePicker 控件 |
| CreateNavigation | uiName, parentName='Form_1', elementName='', direction=tkinter.HORIZONTAL | 创建的 Navigation 控件实例 | 创建 Navigation 控件 |
| CreateListMenu | uiName, parentName='Form_1', elementName='' | 创建的 ListMenu 控件实例 | 创建 ListMenu 控件 |
| CreateSwitchPage | uiName, parentName='Form_1', elementName='' | 创建的 SwitchPage 控件实例 | 创建 SwitchPage 控件 |
| CreateShowCase | uiName, parentName='Form_1', elementName='' | 创建的 ShowCase 控件实例 | 创建 ShowCase 控件 |

## 5. 控件属性操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| SetBindEventFunction | uiName, elementName, eventName, callbackFunction=None | 无 | 设置控件的事件响应函数 |
| SetElementScrollbar | uiName, elementName, orient=tkinter.VERTICAL | 无 | 设置控件的滚动条 |
| GetElementType | uiName, elementName | 控件类型 | 取得控件类型 |
| GetElementXYWH | uiName, elementName | 控件所在矩形 [x, y, width, height] | 取得控件所在矩形 |
| SetElementXY | uiName, elementName, x, y | 无 | 设置控件显示位置 |
| SetElementWH | uiName, elementName, width, height | 无 | 移动控件显示大小 |
| SetElementXYWH | uiName, elementName, x, y, width, height | 无 | 设置控件显示位置和大小 |
| AddTKVariable | uiName, elementName, defaultValue=None | 无 | 为控件增加一个 Tkinter 的内置控件变量 |
| SetTKVariable | uiName, elementName, value | 无 | 设置控件的 Tkinter 变量的值 |
| GetTKVariable | uiName, elementName | 变量值 | 取得控件的 tkinter 变量 |
| AddUserData | uiName, elementName, dataName, datatype, datavalue, isMapToText=0 | 无 | 为控件添加一个用户自定义数据 |
| DelUserData | uiName, elementName, dataName | 无 | 删除一个控件绑定用户自定义数据 |
| SetUserData | uiName, elementName, dataName, datavalue | 无 | 设置控件绑定的用户自定义数据值 |
| GetUserData | uiName, elementName, dataName | 数据值 | 取得控件绑定的用户自定义数据值 |
| SetTKAttrib | uiName, elementName, AttribName, attribValue | 无 | 设置控件的 tkinter 属性值 |
| GetTKAttrib | uiName, elementName, AttribName | 属性值 | 获取控件的 tkinter 属性值 |
| SetVisible | uiName, elementName, Visible | 无 | 设置控件显示或隐藏 |
| SetEnable | uiName, elementName, Enable | 无 | 设置控件可用或无效 |
| IsVisible | uiName, elementName | bool | 取得控件显示或隐藏 |
| IsEnable | uiName, elementName | bool | 取得控件可用或无效 |

## 6. 文本操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| SetText | uiName, elementName, textValue | 无 | 设置控件的文本或输入文字 |
| InsertText | uiName, elementName, position=tkinter.END, textValue='', tag='' | 插入位置 | 在文本框插入文本 |
| GetCurrentLine | uiName, elementName | 当前行号 | 取得文本框当前行号 |
| DeleteContent | uiName, elementName, fromPosition='', toPosition=None | 无 | 删除文本框区域内容 |
| GetText | uiName, elementName | 文本内容 | 获取控件的文本或输入文字 |
| CreateFont | fontName, fontSize, fontWeight=False, fontSlant=False, fontUnderline=False, fontOverstrike=False | 字体实例 | 创建控件字体 |
| SetFont | uiName, elementName, fontName, fontSize, fontWeight='normal', fontSlant='roman', fontUnderline=0, fontOverstrike=0 | 无 | 设置控件字体 |
| GetFont | uiName, elementName, fontName, fontSize, fontWeight='normal', fontSlant='roman', fontUnderline=0, fontOverstrike=0, createifnofind=True | 字体实例 | 取得字体 |

## 7. 颜色操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| SetBGColor | uiName, elementName, RGBColor | 无 | 设置控件的背景色 |
| SetRadioButtonSelectedColor | uiName, elementName, BGColor, FGColor | 无 | 设置 RadioButton 控件的选中时候背景色与文字色 |
| SetCheckButtonSelectedColor | uiName, elementName, BGColor, FGColor | 无 | 设置 CheckButton 控件的选中时候背景色与文字色 |
| SetComboBoxListColor | uiName, elementName, BGColor, FGColor | 无 | 设置 ComboBox 控件下拉框的背景色与文字色 |
| GetBGColor | uiName, elementName | 背景颜色 | 获取控件的背景色 |
| SetTextColor | uiName, elementName, RGBColor | 无 | 设置控件的文字色 |
| GetTextColor | uiName, elementName | 文字颜色 | 获取控件的文字色 |

## 8. 图片操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| SetImage | uiName, elementName, imagePath, autoSize=True, format='RGBA', state='normal' | 无 | 设置控件的背景图片 |
| InsertImage | uiName, elementName, position=tkinter.END, imagePath='', imageSize=None | 无 | 在文本框插入图片 |
| SetCanvasBGImage | uiName, elementName, imagePath, wrapType='zoom' | 无 | 设置画布 Canvas 的背景图片 |
| SetImageFromURL | uiName, elementName, url, autoSize=True | 无 | 多线程设置控件的图片背景 |
| RemoveImage | uiName, elementName | 无 | 删除控件的背景图像文件 |
| GetImage | uiName, elementName, state='normal' | 背景图像文件路径 | 获取控件的背景图像文件 |
| GetImageFileName | uiName, elementName | 图片文件路径 | 取得控件图片文件 |
| LoadImageFromFile | imagefile, imageSize=None, uiName=None, elementName=None | 图片实例 | 从文件加载图片 |
| LoadGIF | uiName, elementName, imagefile, width=0, height=0 | 图片实例 | 播放 GIF 动画 |
| StopGIF | uiName, elementName | 无 | 停止 GIF 动画 |
| LoadImageToIconList | uiName, elementName, IconName, imageFile | 图片实例 | 加载控件的图像文件 |

## 9. 列表操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| SetItemBGColor | uiName, elementName, lineIndex, color | 无 | 设置选项背景色 |
| SetItemFGColor | uiName, elementName, lineIndex, color | 无 | 设置选项文字色 |
| AddItemText | uiName, elementName, text, lineIndex="end", set_see=False | 无 | 增加当前 ListBox 和 ComboBox 的文字项内容 |
| GetItemText | uiName, elementName, lineIndex=0 | 文本内容 | 取得当前 ListBox 和 ComboBox 的文字项内容 |
| AddLineText | uiName, elementName, text, lineIndex="end", textTag='', set_see=False | 无 | 为 Text 控件或 ListBox 控件增加一行文字内容 |
| SetLineText | uiName, elementName, lineIndex=0, text='' | 无 | 增加当前 Text 和 ListBox 的文字项内容 |
| GetLineText | uiName, elementName, lineIndex=0 | 文字内容 | 增加当前 Text 和 ListBox 的文字项内容 |
| DelItemText | uiName, elementName, lineIndexOrText | 无 | 删除当前 ListBox 和 ComboBox 的文字项内容 |
| DelLineText | uiName, elementName, lineIndex="end" | 无 | 删除 Text 控件或 ListBox 控件的指定行文字 |
| DelAllLines | uiName, elementName | 无 | 清空 Text 控件或 ListBox 控件的文字内容 |
| DelAllItemText | uiName, elementName | 无 | 删除 ComboBox 控件的所有行文字 |
| GetValueList | uiName, elementName | 值列表 | 取得当前 ListBox、ComboBox 和 SpinBox 等控件值列表的函数 |
| GetSelectedValueList | uiName, elementName | 值列表 | 取得当前 ListBox 控件选中项的值列表 |
| SetValueList | uiName, elementName, valueList | 无 | 设置当前 ListBox、ComboBox 和 SpinBox 等控件值列表的函数 |

## 10. 页签操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| AddPage | uiName, elementName, title="", iconFile="", importUI='' | 无 | 增加选项页 |
| GetPage | uiName, elementName, index=0 | 页面实例 | 取得指定页 |
| SelectPage | uiName, elementName, index=0 | 无 | 选中选项页 |
| GetSelectedPageIndex | uiName, elementName | 选中页索引 | 取得选中页索引 |
| GetPageText | uiName, elementName, index=0 | 页面标题 | 取得指定页标题 |
| GetPageIndex | uiName, elementName, title | 页面索引 | 取得指定页索引 |
| HidePage | uiName, elementName, index=0 | 无 | 隐藏选项页 |
| DelPage | uiName, elementName, index=0 | 无 | 删除选项页 |
| AddPanedWindowPage | uiName, elementName='', WidthOrHeight=100 | 页面实例 | 增加分割窗体页面 |
| DelPanedWindowPage | uiName, elementName='', index=0 | 无 | 删除分割窗体页面 |

## 11. 树形控件操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| AddTreeItem | uiName, elementName, parentItem="", insertItemPosition="end", itemName="", itemText="", itemValues=(), iconName="", tag="" | 树项实例 | 增加树项 |
| SetTreeItemText | uiName, elementName, itemName, itemText | 无 | 设置树项的文字 |
| GetTreeItemText | uiName, elementName, itemName | 文字内容 | 取得树项的文字 |
| SetTreeItemValues | uiName, elementName, itemName, itemValues | 无 | 设置树项的值 |
| GetTreeItemValues | uiName, elementName, itemName | 值列表 | 取得树项的值 |
| SetTreeItemIcon | uiName, elementName, itemName, iconName='' | 无 | 设置树项的图片 |
| ExpandTreeItem | uiName, elementName, itemName, expand=True | 无 | 展开或收缩树项 |
| CheckPickedTreeItem | uiName, elementName, x, y | 树结点项实例 | 判断当前点击的树结点项 |
| SelectTreeItem | uiName, elementName, itemName | 无 | 选中对应树结点项 |
| GetSelectedTreeItem | uiName, elementName | 选中项实例 | 取得选中项 |
| UnSelecteTreeItem | uiName, elementName | 无 | 取消选中项 |
| MoveTreeItem | uiName, elementName, itemName, parentItemName="", insertPosition="end" | 无 | 移动树结点项的位置 |
| DelTreeItem | uiName, elementName, itemName | 无 | 删除树项 |
| DelAllTreeItem | uiName, elementName | 无 | 删除所有的树结点项 |
| ExpandAllTreeItem | targetTree, isOpen, parentItem=None | 无 | 展开或关闭树项 |
| ExpandTreeView | uiName, elementName | 无 | 展开或关闭树项 |

## 12. 列表视图操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| SetColumnList | uiName, elementName, columnList | 无 | 设置列名称列表 |
| SetColumnInfo | uiName, elementName, columnName='', anchor='center', width=100, stretch=True | 无 | 设置各列信息 |
| AddRowText | uiName, elementName, rowIndex='end', values=(''), tag='' | 无 | 为 ListView 插入一行 |
| AddMultiRowText | uiName, elementName, rowIndex='end', rowValuesList=[], tagList=[] | 无 | 按列表填充 ListView 的多行数据 |
| GetRowTextList | uiName, elementName, rowIndex | 值列表 | 取得 ListView 指定行的所有列文本 |
| GetColumnTextList | uiName, elementName, columnIndex | 值列表 | 取得 ListView 指定列的所有行文本 |
| GetAllRowTextList | uiName, elementName | 值列表 | 取得 ListView 所有行和列文本 |
| GetCellText | uiName, elementName, rowIndex, columnIndex | 文本内容 | 取得 ListView 指定单元格的文本 |
| SetCellText | uiName, elementName, rowIndex, columnIndex, text | 无 | 设置 ListView 指定单元格文字 |
| SetCellCheckBox | uiName, elementName, rowIndex, columnIndex, selected=True | 无 | 设置 ListView 指定单元格复选框 |
| SetColumnCheckBox | uiName, elementName, beginRowIndex=0, endRowIndex=-1, columnIndex=0, selected=True | 无 | 设置 ListView 指定行范围的单元格复选框 |
| GetCellBox | uiName, elementName, rowIndex, columnIndex | 单元格位置大小 [x, y, width, height] | 取得 ListView 指定单元格位置大小 |
| SetCellIcon | uiName, elementName, rowIndex, columnIndex, imageFile='' | 无 | 设置 ListView 指定单元格为文本标签 |
| CloseCellLabel | uiName, elementName, rowIndex, columnIndex | 无 | 关闭 ListView 指定单元格本标签 |
| SetCellEntry | uiName, elementName, rowIndex, columnIndex, callback=None | 无 | 设置 ListView 指定单元格为输入框 |
| GetCellEntry | uiName, elementName, rowIndex, columnIndex | 输入框实例 | 取得 ListView 指定单元格输入框 |
| GetCellEntryText | uiName, elementName, rowIndex, columnIndex | 输入框文本 | 取得 ListView 指定单元格输入框的文本 |
| CloseCellEntry | uiName, elementName, rowIndex, columnIndex | 无 | 关闭 ListView 指定单元格输入框 |
| SetCellComboBox | uiName, elementName, rowIndex, columnIndex, initList=[], callback=None | 无 | 设置 ListView 指定单元格为下拉列表框 |
| GetCellComboBox | uiName, elementName, rowIndex, columnIndex | 下拉列表框实例 | 取得 ListView 指定单元格下拉列表框 |
| GetCellComboBoxValue | uiName, elementName, rowIndex, columnIndex | 下拉列表框文本 | 取得 ListView 指定单元格下拉列表框的文本 |
| CloseCellComboBox | uiName, elementName, rowIndex, columnIndex | 无 | 关闭 ListView 指定单元格下拉列表框 |
| DeleteRow | uiName, elementName, rowIndex | 无 | 删除 ListView 指定行 |
| DeleteAllRows | uiName, elementName | 无 | 清空 ListView 所有行 |
| CheckPickedRow | uiName, elementName, x, y | 行号 | 取得鼠标位置 ListView 的行号 |
| CheckPickedCell | uiName, elementName, x, y | 单元格位置 [x, y] | 取得鼠标位置 ListView 的单元格 |
| SelectRow | uiName, elementName, beginRowIndex=0, endRowIndex=None | 无 | 选中 ListView 指定行 |
| GetSelectedRowIndex | uiName, elementName | 选中行索引列表 | 取得 ListView 选中行的行索引 |
| SortLineByColumn | uiName, elementName, columnIndex=0, reverse=False | 无 | 设置 ListView 按指定列排序 |
| SetRowStyle | uiName, elementName, rowIndex='even', bgColor='lightblue', fgColor='#000000', textFont=None | 无 | 设置 ListView 的行样式 |
| SetRowBGColor | uiName, elementName, rowIndex='even', bgColor='lightblue' | 无 | 设置 ListView 的行背景色 |

## 13. 数值控件操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| GetCurrentValue | uiName, elementName | 选中值 | 取得 RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton、Slider、ProgressDial 控件的选中值 |
| GetCurrentIndex | uiName, elementName | 索引值 | 取得 ListBox、ComboBox、Navigation 的选中索引值 |
| SetCurrentValue | uiName, elementName, value | 无 | 设置 RadioButton、CheckButton、Scale、Progress、ListBox、ComboBox、SpinBox、SwitchButton、Slider、ProgressDial 控件的选中值 |
| SetCurrentIndex | uiName, elementName, index | 无 | 设置 ListBox、ComboBox、Navigation 的选中索引值 |
| SetScale | uiName, elementName, minimum, maximum, tickinterval | 无 | 设置 Scale |
| SetSlider | uiName, elementName, minimum, maximum, value=0 | 无 | 设置 Slider |
| SetProgress | uiName, elementName, maximum, value=0 | 无 | 设置进度条 Progress |

## 14. 滚动操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| MovingChildPageXViewOffset | uiName, elementName, step=1 | 无 | 面板内视野横向移动指定步长 |
| MovingChildPageYViewOffset | uiName, elementName, step=1 | 无 | 面板内视野纵向移动指定步长 |
| MovingChildPageXViewTo | uiName, elementName, x=1.0 | 无 | 面板内视野横向移动到目标位置 |
| MovingChildPageYViewTo | uiName, elementName, y=1.0 | 无 | 面板内视野纵向移动到目标位置 |

## 15. 日期操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| GetDate | uiName, elementName | 日期列表 [年, 月, 日] | 取得选择的日期 |
| SetDate | uiName, elementName, year, month, day | 无 | 设置当前的日期 |

## 16. 界面跳转函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| CallUIDialog | uiName, topmost=1, toolwindow=1, grab_set=1, wait_window=1, animation='', params=None | 所有控件的输入值字典 | 弹出调用显示一个界面，并返回所有控件的输入值 |
| GetUIDataDictionary | uiName | 所有控件的输入值字典 | 取得界面的所有控件数据 |
| GoToUIDialog | uiName, targetUIName, params=None | 无 | 从当前界面跳转到另一个界面 |
| PlayCallUIDialogAction | topLevel, uiInstance, animation='zoomin' | 无 | 播放界面跳转动画 |
| LoadUIDialog | uiName, elementName, targetUIName, params=None, ignoreSameUI=True | 无 | 在指定控件上加载一个界面 |
| SetChildFrameScrollRegion | uiName, elementName, width, height | 无 | 设置 Frame 可观察导入界面的区域大小 |
| AddUIDialog | uiName, elementName, targetUIName, x, y, params=None | 无 | 在指定控件上加载一个界面 |

## 17. 窗口操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| ShowWindow | uiName, WindowState | 无 | 设置窗口显示状态 (0:隐藏, 1:正常显示, 2:最小化, 3最大化) |
| SetWindowTitle | uiName, title='' | 无 | 设置窗口标题 |
| SetWindowIco | uiName, imageFile='' | 无 | 设置窗口图标 |
| SetUIDialogXYWH | uiName, x, y, width, height | 无 | 设置窗口显示位置和大小 |
| SetUIDialogXY | uiName, x, y | 无 | 设置窗口显示位置 |
| SetUIDialogWH | uiName, width, height | 无 | 移动窗口显示大小 |
| MaximizeUI | uiName | 无 | 最大化窗口 |
| MinimizeUI | uiName | 无 | 最小化窗口 |
| RestoreUI | uiName | 无 | 恢复窗口 |
| HideUI | uiName | 无 | 隐藏窗口 |
| SetUIState | uiName, state | 无 | 最大化窗口 |
| SetRoundedRectangle | uiName, elementName, WidthEllipse=20, HeightEllipse=20 | 无 | 在界面布局文件中调用设置控件的圆角属性 |
| ShowRoundedRectangle | Control, WidthEllipse, HeightEllipse | 无 | 立即设置控件的圆角属性 |
| SetTransparencyFunction | root, alpha | 无 | 设置窗体透明值 |
| SetWindowTransparency | uiName, alpha | 无 | 设置窗体透明值 |

## 18. 对话框函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| MessageBox | text="", title="info", type="info", parent=None | 无 | 弹出一个信息对话框 |
| InputBox | title='', prompt='', initialvalue='', parent=None | 输入文本 | 弹出一个输入对话框 |
| InputDialog | width, lines=1, bgColor='#f8f9fa', titleText='', promptText='', defaultText='', callBackFunction=None | 输入框文本 | 弹出一个输入对话框 |
| AskBox | title, text, parent=None | 是否选择 YES | 弹出一个选择对话框，你需要选择 YES 或 NO |
| AskCancelBox | title, text, parent=None | 是否选择是 "Cancel" | 弹出一个选择对话框，你需要选择 YES、NO 或 CANCEL |
| SelectDirectory | title='选择路径', initDir=os.path.abspath('.'), parent=None | 选择的目录路径 | 打开查找目录对话框 |
| SelectColor | title='请选择颜色' | 选择的颜色 | 打开选取颜色对话框 |

## 19. 字体和文件操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| EnumFontName | 无 | 字体名称列表 | 罗列当前系统的所有文字 |
| WalkAllResFiles | parentPath, alldirs=True, extName=None | 文件路径列表 | 返回对应目录的所有指定类型文件 |
| ImportResources | srcFile, coverMode=True | 是否成功 | 将文件复制到资源目录 |
| CopyFile | srcFile, dstFile, coverMode=True | 是否成功 | 复制文件 |
| MoveFile | srcFile, dstFile, coverMode=True | 是否成功 | 移动文件 |
| DeleteFile | dstFile | 无 | 删除文件 |
| GetFileMD5 | srcFile | 文件 MD5 码 | 取得文件 MD5 码 |
| CompareFileMD5 | srcFile, dstFile | 是否一致 | 比较两个文件是否一致 |
| CreateDir | dstDir, coverMode=True | 是否成功 | 创建目录 |
| CopyDir | srcDir, dstDir, coverMode=True | 是否成功 | 复制目录 |
| MoveDir | srcDir, dstDir, coverMode=True | 是否成功 | 移动目录 |
| DeleteDir | srcDir | 无 | 删除目录 |
| CheckIsDir | srcDir | 是否是目录 | 判断是否是目录 |
| CheckExist | srcDir | 是否存在 | 判断文件或目录是否存在 |
| GetFileExtension | srcFile | 文件扩展名 | 取得文件扩展名 |
| ReadFromFile | filePath, encoding='utf-8', autoEval=False | 文件内容 | 从一个文件中读取内容 |
| OpenFile | title="Open Python File", filetypes=[('Python File','*.py'),('All files','*')], initDir='' | 打开的文件路径 | 调用打开文件框 |
| WriteToFile | filePath, content, encoding='utf-8', append=False | True 成功，False 失败 | 将内容写入到一个文件中 |
| SaveFile | title="Save Python File", filetypes=[('Python File','*.py'),('All files','*')], initDir='', defaultextension='py' | 保存的文件路径 | 调用保存文件框 |
| GetResourcePath | FileName | 资源文件的绝对路径 | 查询一个资源文件的路径，返回资源文件的绝对路径 |

## 20. 布局操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| SetControlPack | uiName, elementName, fill, side, padx, pady, expand, width=0, height=0 | 无 | 设置控件的打包布局 |
| SetControlGrid | uiName, elementName, row, column, rowspan, columnspan | 无 | 设置控件的表格布局 |
| SetControlPlace | uiName, elementName, x, y, w, h, anchorpoint='nw', visible=True, modify=True | 无 | 设置控件的绝对或相对位置 |
| GetControlPlace_AnchorPoint | uiName, elementName | 参考位置 | 取得控件的参考位置 |
| SetElementLayer | uiName, elementName, direction='lift' | 无 | 设置控件的层次升降 |

## 21. 画布绘制函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| DrawLine | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, width=1, dash=(0,0), shapeTag='' | shapeTag | 在画布上画线 |
| DrawArrow | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, width=1, dash=(0,0), shapeTag='' | shapeTag | 在画布上画箭头 |
| DrawTriangle | uiName, drawCanvasName, direction, x1, y1, x2, y2, Anchor, color, outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), shapeTag='' | shapeTag | 在画布上画三角形 |
| DrawRectangle | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), shapeTag='' | shapeTag | 在画布上画矩形 |
| DrawRoundedRectangle | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), roundRadius=10, shapeTag='' | shapeTag | 在画布上显示圆角矩形 |
| DrawCircle | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), shapeTag='' | shapeTag | 在画布上画圆 |
| DrawDiamond | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), shapeTag='' | shapeTag | 在画布上画菱形 |
| DrawCylinder | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), shapeTag='' | shapeTag | 在画布上画圆柱 |
| DrawStar | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, color, outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), shapeTag='' | shapeTag | 在画布上画星星 |
| DrawText | uiName, drawCanvasName, x, y, Anchor, text, textFont=None, color='#FFFFFF', anchor='nw', shapeTag='' | shapeTag | 在画布上写字 |
| DrawImage | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, imagefile, shapeTag='' | shapeTag | 在画布上显示图片 |
| DrawButton | uiName, drawCanvasName, x1, y1, x2, y2, Anchor, text='', textcolor='#000000', textFont=None, fillcolor='#FFFFFF', outlinecolor='#FFFFFF', outlinewidth=0, dash=(0,0), shapeTag='' | shapeTag | 在画布上显示圆角按钮 |
| EraserCanvas | uiName, drawCanvasName, x1, y1, x2, y2 | 无 | 在画布上檫去区域 |
| SetCanvasGridBG | uiName, drawCanvasName, bgcolor='#888888', tile_width=20, tile_height=20 | 无 | 设置画布背景格子 |
| SetCanvasGradient | uiName, elementName, StartColor="#050814", EndColor="#F0F8FF" | 无 | 设置画布渐变背景颜色 |
| checkPtInRect | x, y, left, right, top, bottom | 0 或 1 | 判断点是否在矩形内 |

## 22. 画布图形操作函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| GetShapePoint | uiName, drawCanvasName, shapeTag='', pointTag='', absoluteMode=True | None | 获取绑定点位置 |
| SetShapeRect | uiName, canvasName, shapeTag, x1, y1, x2, y2 | 无 | 设置矩形位置大小 |
| GetShapeRect | uiName, canvasName, shapeTag | None | 取得画布图形矩形位置大小 |
| SetShapeFillColor | uiName, canvasName, shapeTag, color | 无 | 设置图形填充颜色 |
| GetShapeFillColor | uiName, canvasName, shapeTag | None | 取得画布图形颜色 |
| SetShapeOutlineColor | uiName, canvasName, shapeTag, color | 无 | 设置图形边框颜色 |
| GetShapeOutlineColor | uiName, canvasName, shapeTag | None | 取得画布图形边框颜色 |
| SetShapeLineWidth | uiName, canvasName, shapeTag, width | 无 | 设置图形线条宽度 |
| SetShapeImage | uiName, canvasName, shapeTag, imageFile, angle=0 | 无 | 更换图片文件 |
| GetShapeImage | uiName, canvasName, shapeTag | None | 取得画布图形图片文件 |
| PasteImageToShapeImage | uiName, canvasName, shapeTag, imageFileName, x1, x2, y1, y2, angle | 无 | 将图片粘贴到画布的图片图形上 |
| SetShapeText | uiName, drawCanvasName, shapeTag, text, color=None | 无 | 设置画布文字及颜色 |
| GetShapeText | uiName, drawCanvasName, shapeTag | None | 取得画布图形文字与颜色 |
| SetCanvasTableCellBGColor | uiName, drawCanvasName, shapeTag, row=0, col=0, bgColor='#FFFFFF' | 无 | 设置单元格背景色 |
| SetCanvasTableCellText | uiName, drawCanvasName, shapeTag, row=0, col=0, cellText='' | 无 | 设置单元格文字，字符 ┇ 作为分隔符，可斜线分割单元格 |
| SetCanvasTableCellTextColor | uiName, drawCanvasName, shapeTag, row=0, col=0, textColor='#000000' | 无 | 设置单元格文字颜色 |
| SetCanvasTableCellTextFont | uiName, drawCanvasName, shapeTag, row=0, col=0, font='TkDefaultFont' | 无 | 设置单元格文字字体 |
| SetCanvasTableCellTextAnchor | uiName, drawCanvasName, shapeTag, row=0, col=0, anchor='center' | 无 | 设置单元格文字对齐方式 |
| SetCanvasTableCellMerge | uiName, drawCanvasName, shapeTag, BeginRow=0, BeginCow=0, EndRow=0, EndCow=0 | 无 | 合并单元格 |
| SetCanvasTableCellSplit | uiName, drawCanvasName, shapeTag, row=0, col=0 | 无 | 拆分单元格 |
| SetCanvasTableRowTextList | uiName, drawCanvasName, shapeTag, row=0, textList=[] | 无 | 使用列表填充表格整行文字 |
| BindShapeEvent_SetShapeRect | uiName, drawCanvasName, shapeTag, bindEvent, targetShapeTag, x, y, w, h | 无 | 绑定事件-设置图形位置与大小 |
| BindShapeEvent_SetFillColor | uiName, drawCanvasName, shapeTag, bindEvent, targetShapeTag, color | 无 | 绑定事件-设置图形颜色 |
| BindShapeEvent_SetOutlineColor | uiName, drawCanvasName, shapeTag, bindEvent, targetShapeTag, color | 无 | 绑定事件-设置图形边框颜色 |
| BindShapeEvent_ChangeImage | uiName, drawCanvasName, shapeTag, bindEvent, targetShapeTag, ImageFile | 无 | 绑定事件-更换图形图片 |
| BindShapeEvent_ChangeText | uiName, drawCanvasName, shapeTag, bindEvent, targetShapeTag, Text, TextColor | 无 | 绑定事件-设置图形文字 |
| BindShapeEvent_JumpToUI | uiName, drawCanvasName, shapeTag, bindEvent, targetUIName | 无 | 绑定事件-跳转其它界面 |
| BindShapeEvent_LoadUI | uiName, drawCanvasName, shapeTag, bindEvent, widgetName, targetUIName | 无 | 绑定事件-嵌入界面 |
| BindShapeEvent_DeleteShape | uiName, drawCanvasName, shapeTag, bindEvent, targetShapeTag | 无 | 绑定事件-删除图形 |
| BindShapeEvent_CallFunction | uiName, drawCanvasName, shapeTag, bindEvent, targetShapeTag, callBackFuncton, param=None | 无 | 绑定事件-调用函数 |
| BindShapeMouseEvent | uiName, drawCanvasName, shapeTag, bindEvent, actionInfo | 无 | 对绑定事件进行处理 |
| DeleteShape | uiName, drawCanvasName, shapeTag | 无 | 删除画布中的画形 |

## 23. 动画和交互函数

| 函数名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| CreateToolTip | uiName, elementName, tipText, bgColor='#CCCCCC', fgColor='#000000' | 无 | 创建工具提示 |
| PlayAction_MoveTo | uiName, elementName, targetX, targetY, duration=1.0, fps=50 | 无 | 控件移动到指定位置 |
| PlayAction_MoveBy | uiName, elementName, moveX=0, moveY=0, duration=1.0, fps=50 | 无 | 控件移动一定距离 |
| PlayAction_ScaleTo | uiName, elementName, anchor="center", scaleW=1.0, scaleH=1.0, duration=1.0, fps=50 | 无 | 控件缩放到指定大小 |
| SetRootRoundRectangle | canvas, hastitlebar, x1, y1, x2, y2, radius=25, **kwargs | 无 | 使用 TKinter 方式设置窗口圆角，支持跨平台 |

## 24. AI 组件类

### AIChat 类
| 方法名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| InitAI | useOpenAI=False, base_url='', api_key='', model_name='' | 无 | 初始化 AI 对话组件 |
| Ask | question='', stream=False, callback=None | 回答内容 | 调用大模型提问并返回解析后的回答 |

### AIImage 类
| 方法名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| InitAI | useOpenAI=False, base_url='', api_key='', model_name='' | 无 | 初始化 AI 图像生成组件 |
| GenerateImage | prompt='', size="512x512", quality="standard", count=1, callback=None | 图片 URL 列表 | 根据设置参数生成图片 |
| DownloadImage | image_url, save_path | bool | 下载图片到本地 |

### AITTS 类
| 方法名 | 参数 | 返回值 | 功能描述 |
|-------|------|-------|----------|
| InitAI | base_url='https://open.bigmodel.cn/api/paas/v4/audio/transcriptions', api_key='', model_name='glm-asr-2512' | 无 | 初始化 AI 语音转换组件 |
| SoundToText | sound_file_path='' | 文本内容 | 声音转文本 |
| TextToSound | text='' | 声音内容 | 文本转声音 |

 ## 使用核心原则
  1. 逻辑文件代码实现逻辑，要参考Fun函数库文件中的全局变量、功能函数和组件类进行功能实现，确认函数是否存在，是否参数正确。

# PyMe 界面逻辑文件（界面_cmd.py）格式规范

## 基础结构
    以上面的登录界面为例，登录界面的文件内容参考下面代码，主要是对UIJsonString中的EventList进行事件处理，为每个事件添加对应的处理函数，比如对于"Button_1"的点击事件，在UIJsonString中"Button_1"的EventList为： {{"Command": "Button_1_onCommand"}}，则将在逻辑文件中必然有Button_1_onCommand函数代码。
    逻辑文件代码实现逻辑，要参考Fun函数库文件中的全局变量、功能函数和组件类进行功能实现，确认调用的全局变量、功能函数和组件类是否在上述表格中存在，是否参数正确。
```python
#coding=utf-8
import sys
import os
from   os.path import abspath, dirname
sys.path.insert(0,abspath(dirname(__file__)))
import tkinter
from   tkinter import *
import Fun
uiName="Login"
ElementBGArray={}  
ElementBGArray_Resize={} 
ElementBGArray_IM={} 
#Form 'Form_1's Load Event :
def Form_1_onLoad(uiName,threadings=0):
    pass
#Button 'Button_1' 's Command Event :
def Button_1_onCommand(uiName,widgetName,threadings=0):
    UserName=Fun.GetText(uiName,"Entry_1")
    PassWord=Fun.GetText(uiName,"Entry_2")
    Fun.MessageBox("UserName:"+UserName+"   PassWord:"+PassWord)
#Button 'Button_2' 's Command Event :
def Button_2_onCommand(uiName,widgetName,threadings=0):
    Fun.DestroyUI(uiName,0,'')

```
 ## 核心原则
  1. 逻辑文件代码调用Fun函数库文件中的函数时，确认函数是否存在，是否参数正确。

# PyMe 界面样式文件（界面_sty.py）格式规范
  生成样式文件时直接用下面基础结构文件，不要修改：
## 基础结构
```python
import tkinter
import tkinter.ttk
def fixed_map(style,option):
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]
def SetupStyle(isTKroot=False):
    style = tkinter.ttk.Style()
    style.map('Treeview', foreground=fixed_map(style,'foreground'),background=fixed_map(style,'background'))
    theme_settings = {

        }
    theme_curr = 'clam'#style.theme_use()
    if isTKroot == True and theme_curr:
        style.theme_use(theme_curr)
    return style
def ResetNotebook(notebook,style,NoteBookStyle = "PyMe.TNotebook"):
    pass

```
 ## 核心原则
  1. 创建时直接用上面的代码，不要修改。