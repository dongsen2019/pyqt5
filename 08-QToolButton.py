# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QToolButton使用")
window.resize(500, 500)

tb = QToolButton(window)
# tb = QPushButton(window)
tb.setText("工具")
tb.setIcon(QIcon("xxx.png"))
"""
对于工具按钮，文本和图标同时设置
只显示图标，不显示文本
而QPushButton同时设置，既显示图标，又显示文本
"""

# tb.setIconSize(QSize(60, 60))
"""
设置图标尺寸
"""

# tb.setToolTip("这是一个新建按钮")
"""
按钮的功能贴士
"""

# Qt.ToolButtonIconOnly
# 	仅显示图标
# Qt.ToolButtonTextOnly
# 	仅显示文字
# Qt.ToolButtonTextBesideIcon
# 	文本显示在图标旁边
# Qt.ToolButtonTextUnderIcon
# 	文本显示在图标下方
# Qt.ToolButtonFollowStyle
# 	遵循风格
print(tb.toolButtonStyle())
tb.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
print(tb.toolButtonStyle())
tb.setToolButtonStyle(Qt.ToolButtonFollowStyle)
print(tb.toolButtonStyle())
"""
setToolButtonStyle(Qt.ToolButtonTextBesideIcon)     设置工具按钮的样式风格
样式风格的枚举值：
1. Qt.ToolButtonIconOnly
# 	仅显示图标
2. Qt.ToolButtonTextOnly
# 	仅显示文字
3. Qt.ToolButtonTextBesideIcon
# 	文本显示在图标旁边
4. Qt.ToolButtonTextUnderIcon
# 	文本显示在图标下方
5. Qt.ToolButtonFollowStyle
# 	遵循风格
"""

tb.setAutoRaise(True)
"""
setAutoRaise(bool)   在自动提升模式下，该按钮仅在鼠标指向时才会绘制3D帧 
                     在工具栏(QToolBar)中, 默认就是自动提升  
autoRaise()          查看是否设置为自动提升
"""


menu = QMenu(tb)
# menu.setTitle("菜单")


sub_menu = QMenu(menu)
sub_menu.setTitle("子菜单")
sub_menu.setIcon(QIcon("xxx.png"))

action1 = QAction(QIcon("xxx.png"), "行为1", menu)
action1.setData([1, 2, 3])
action2 = QAction("行为2", menu)
action2.setData({"name": "sz"})
"""
action1.setData([1, 2, 3])      为行为绑定数据
"""
# action.triggered.connect(lambda :print("点击了行为菜单选项"))

menu.addMenu(sub_menu)
menu.addSeparator()
menu.addAction(action1)
menu.addAction(action2)

tb.clicked.connect(lambda :print("工具按钮被点击了"))

tb.setMenu(menu)
"""
为工具按钮设置菜单
"""

# tb.setPopupMode(QToolButton.InstantPopup)

"""
QToolButton.DelayedPopup    鼠标按住一会才显示，类似于浏览器后退按钮
QToolButton.MenuButtonPopup 有一个专门的指示箭头，点击箭头才显示
QToolButton.InstantPopup    点了按钮就显示，点击信号不会发射
setPopupMode(QToolButton.InstantPopup)  设置弹出模式
popupMode()                 获取弹出模式
"""

def do_action(action):
    print("点击了行为", action.data())
tb.triggered.connect(do_action)

"""
triggered(QAction *action)      当点击工具按钮菜单某个action时触发, 并会将action传递出来
action.data()           获取行为绑定的数据
"""


# btn = QPushButton(window)
# btn.setText("一般按钮")
# btn.move(100, 100)
# btn.setFlat(True)
#
#
#
# btn.setMenu(menu)



# Qt.NoArrow
# 	无箭头
# Qt.UpArrow
# 	向上箭头
# Qt.DownArrow
# 	向下箭头
# Qt.LeftArrow
# 	向左箭头
# Qt.RightArrow
# 	向右箭头

tb.setArrowType(Qt.RightArrow)
"""
setArrowType(Qt.RightArrow)     设置箭头方向，箭头的优先级比图标的优先级高
arrowType()                     获取设置的箭头方向类型
"""

# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())