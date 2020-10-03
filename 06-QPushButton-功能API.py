# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

class Window(QWidget):
    def contextMenuEvent(self, evt):
        print("默认上下文菜单调用这个方法")
        menu = QMenu(self)
        """
        为菜单设置父控件
        """

        # 子菜单 最近打开

        open_recent_menu = QMenu(menu)
        open_recent_menu.setTitle("最近打开")
        # open_recent_menu.setIcon()

        # 行为动作 新建  打开  分割线 退出
        # new_action = QAction()
        # new_action.setText("新建")
        # new_action.setIcon(QIcon("xxx.png"))
        new_action = QAction(QIcon("xxx.png"), "新建", menu)
        new_action.triggered.connect(lambda: print("新建文件"))

        open_action = QAction(QIcon("xxx.png"), "打开", menu)
        open_action.triggered.connect(lambda: print("打开文件"))

        exit_action = QAction("退出", menu)
        exit_action.triggered.connect(lambda: print("退出程序"))

        file_action = QAction("Python-GUI编程-PyQt5")

        menu.addAction(new_action)
        menu.addAction(open_action)
        open_recent_menu.addAction(file_action)
        menu.addMenu(open_recent_menu)
        menu.addSeparator()
        menu.addAction(exit_action)

        # point
        menu.exec_(evt.globalPos())
        """
        设置右击菜单展示的点位
        """
        # menu.exec_(evt.pos())

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("按钮的功能")
window.resize(500, 500)


btn = QPushButton(window)
btn.setParent(window)
btn.setText("xxx")
btn.setIcon(QIcon("xxx.png"))

"""
    QPushButton的三大构造函数
    QPushButton(parent: QWidget = None)
    QPushButton(str, parent: QWidget = None)
    QPushButton(QIcon, str, parent: QWidget = None)
"""


# *************菜单的设置***************开始
menu = QMenu(window)
"""
QMenu(parent: QWidget = None)
QMenu(str, parent: QWidget = None)
"""

# 子菜单 最近打开

open_recent_menu = QMenu(menu)
open_recent_menu.setTitle("最近打开")
# open_recent_menu.setIcon()
"""
QMenu(menu)     构建子菜单
setTitle(str)    设置子菜单标题
setIcon()       设置子菜单图标
"""

# 行为动作 新建  打开  分割线 退出
# new_action = QAction()
# new_action.setText("新建")
# new_action.setIcon(QIcon("xxx.png"))
new_action = QAction(QIcon("xxx.png"), "新建", menu)
new_action.triggered.connect(lambda :print("新建文件"))

open_action = QAction(QIcon("xxx.png"), "打开", menu)
open_action.triggered.connect(lambda :print("打开文件"))

exit_action = QAction("退出", menu)
exit_action.triggered.connect(lambda :print("退出程序"))

file_action = QAction("Python-GUI编程-PyQt5")

"""
QAction()   构造行为
setText(str)    创建行为文本
setIcon(QIcon("xxx.png"))   创建行为图标
triggered       触发行为的信号
"""

menu.addAction(new_action)
menu.addAction(open_action)
open_recent_menu.addAction(file_action)
menu.addMenu(open_recent_menu)
menu.addSeparator()
menu.addAction(exit_action)

"""
menu.addAction(new_action)      添加行为
menu.addMenu(open_recent_menu)  添加子菜单
menu.addSeparator()             添加分割线
"""

# btn.setMenu(menu)
"""
btn.setMenu(menu)       设置菜单
btn.showMenu()如果在它之前，无法展示，因为要先设置，再展示
"""

# print(btn.menu())

"""
获取菜单
"""

# btn.setStyleSheet("background-color: red;")
# btn.setFlat(True)
# print(btn.isFlat())
"""
setFlat(True)   扁平化
btn.isFlat()    获取是否扁平
"""

# *************菜单的设置***************结束

btn2 = QPushButton(window)
btn2.setText("btn2")
btn2.move(200, 200)

btn2.setAutoDefault(True)

print(btn.autoDefault())
print(btn2.autoDefault())

btn2.setDefault(True)
"""
setAutoDefault(True)    设置按钮为自动默认
autoDefault()           查看按钮是否为自动默认
setDefault(True)        设置按钮为默认
isDefault()             查看按钮是否为默认
"""


def show_menu(point):
    menu = QMenu(window)

    # 子菜单 最近打开

    open_recent_menu = QMenu(menu)
    open_recent_menu.setTitle("最近打开")
    # open_recent_menu.setIcon()

    # 行为动作 新建  打开  分割线 退出
    # new_action = QAction()
    # new_action.setText("新建")
    # new_action.setIcon(QIcon("xxx.png"))
    new_action = QAction(QIcon("xxx.png"), "新建", menu)
    new_action.triggered.connect(lambda: print("新建文件"))

    open_action = QAction(QIcon("xxx.png"), "打开", menu)
    open_action.triggered.connect(lambda: print("打开文件"))

    exit_action = QAction("退出", menu)
    exit_action.triggered.connect(lambda: print("退出程序"))

    file_action = QAction("Python-GUI编程-PyQt5")

    menu.addAction(new_action)
    menu.addAction(open_action)
    open_recent_menu.addAction(file_action)
    menu.addMenu(open_recent_menu)
    menu.addSeparator()
    menu.addAction(exit_action)

    # point
    dest_point = window.mapToGlobal(point)
    """
    将局部坐标转换为全局坐标
    """
    menu.exec_(dest_point)
    """
    设置菜单展示点位
    """

window.setContextMenuPolicy(Qt.CustomContextMenu)
window.customContextMenuRequested.connect(show_menu)
"""
setContextMenuPolicy(Qt.CustomContextMenu)      设置上下文菜单调用策略
Qt.DefaultContextMenu  默认上下文菜单             调用对象方法contextMenuEvent()
Qt.CustomContextMenu    发射信号                 自定义
customContextMenuRequested(QPoint)               自定义上下文菜单请求信号，信号会发送一个局部坐标
"""

# btn.show()
"""
如果控件为顶层窗口，作用等价于window.show()
"""

# 2.3 展示控件
window.show()

# btn.showMenu()
"""
菜单展示放在window.show()之后，不然会展示到左上角
"""

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())