# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mousePressEvent(self, evt):
        # print(self.focusWidget())
        # self.focusNextChild()
        # self.focusPreviousChild()
        self.focusNextPrevChild(True)

"""
focusWidget()           获取当前窗口内部, 所有子控件当中获取焦点的那个控件
focusNextChild()        聚焦下一个子控件
focusPreviousChild()    聚焦上一个子控件
focusNextPrevChild(True)    True: 下一个   False: 上一个
"""


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)


# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("焦点控制")
window.resize(500, 500)


le1 = QLineEdit(window)
le1.move(50, 50)

le2 = QLineEdit(window)
le2.move(100, 100)

le3 = QLineEdit(window)
le3.move(150, 150)
"""
默认情况下，点击鼠标和按下键盘来获取或者切换焦点
"""
# 注意这是静态类方法
QWidget.setTabOrder(le1, le3)
QWidget.setTabOrder(le3, le2)

"""
设置子控件获取焦点的先后顺序
"""

# le2.setFocus()        设置le2为打开界面时默认获取的焦点


# le2.setFocusPolicy(Qt.TabFocus)
# le2.setFocusPolicy(Qt.ClickFocus)
# le2.setFocusPolicy(Qt.StrongFocus)
# le2.setFocusPolicy(Qt.NoFocus)
"""
设置焦点策略：
setFocusPolicy(Qt.TabFocus)     通过Tab键获得焦点
setFocusPolicy(Qt.ClickFocus)   通过被单击获得焦点
setFocusPolicy(Qt.StrongFocus)  可通过上面两种方式获得焦点
Qt.NoFocus                      不能通过上两种方式获得焦点(打开界面后默认情况下),setFocus仍可使其获得焦点
"""

# le2.setFocus()        设置为焦点
# le2.clearFocus()      取消焦点


# 2.3 展示控件
window.show()

# print(le1)
# print(le2)
# print(le3)

# le2.setFocus()

# 获取当前窗口内部, 所有子控件当中获取焦点的那个控件
"""
文本框获取焦点的时间在下面的代码之后，因此打印位None
但如果展示窗口后设置了焦点，就能被打印出来
window.show()

# print(le1)
# print(le2)
# print(le3)

# le2.setFocus()
"""
# print(window.focusWidget())

# le1.clearFocus()

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())