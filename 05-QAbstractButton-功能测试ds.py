# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QAbcBtn功能测试")
window.resize(500, 500)

btn = QPushButton(window)

# ***************累加1案例***************开始
# btn.setText('1')
#
#
# def add_one():
#     btn.setText(str(int(btn.text())+1))
#
#
# btn.pressed.connect(add_one)
# ***************累加1案例***************结束

# ***************图标操作***************开始

# icon = QIcon("E:\pycharm\source/xxx.png")   # 创建图标
# btn.setIcon(icon)       # 设置控件图标
# btn.setIconSize(QSize(30, 30))      # 设置图标尺寸
# print(btn.icon())       # 获取图标
# print(btn.iconSize())   # 获取图标大小
# ***************图标操作***************结束

# ***************快捷键的设定***************开始

# btn.pressed.connect(lambda :print("按钮被点击了"))
# # btn.setText("a&bc")     &a ==> Alt+a
# btn.setShortcut("Alt+b")  # 设置快捷键为Alt+b

# ***************快捷键的设定***************结束

# ***************自动重复***************开始

# btn.setAutoRepeat(True)         # 设置自动重复
# btn.setAutoRepeatDelay(2000)    # 设置初次检测延迟
# btn.setAutoRepeatInterval(1000)   # 设置自动重复检测间隔
# print(btn.autoRepeat())       # 获取是否自动重复
# print(btn.autoRepeatInterval())   # 获取自动重复检测间隔
# print(btn.autoRepeatDelay())      # 获取初次检测延迟

# ***************自动重复***************结束

# *************按钮状态***************开始

# push_button = QPushButton(window)
# push_button.setText("这是QPushButton")
# push_button.move(100, 100)
#
# radio_button = QRadioButton(window)
# radio_button.setText("这是一个radio")
# radio_button.move(100, 150)
#
# checkbox = QCheckBox(window)
# checkbox.setText("这是checkbox")
# checkbox.move(100, 200)
#
# push_button.setStyleSheet("QPushButton:pressed {background-color: red;}")

# 把三个按钮, 置为按下状态
# push_button.setDown(True)
# radio_button.setDown(True)
# checkbox.setDown(True)

"""
isCheckable() 判断按钮是否可以被选中
setCheckable(bool)  设置按钮, 是否可以被选中
setChecked(bool)    设置按钮, 是否被选中
"""
# push_button.setCheckable(True)
# print(push_button.isCheckable())
# print(radio_button.isCheckable())
# print(checkbox.isCheckable())
#
# radio_button.setChecked(True)
# push_button.setChecked(True)
# checkbox.setChecked(True)
#
# print(push_button.isChecked())
# print(radio_button.isChecked())
# print(checkbox.isChecked())

"""
toggle() 切换选中与非选中状态
等价于 ==> push_button.setChecked(not push_button.isChecked())
"""
# def cao():
#     push_button.toggle()
#     radio_button.toggle()
#     checkbox.toggle()
#
#     # push_button.setChecked(not push_button.isChecked())
#
#
# btn.pressed.connect(cao)
#
#
# push_button.setEnabled(False)
# radio_button.setEnabled(False)
# checkbox.setEnabled(False)

# ***************按钮状态***************结束

# ***************排他性设置***************开始

# for i in range(0, 3):
#     btn = QCheckBox(window)
#     btn.setText("btn" + str(i))
#     btn.move(50 * i, 50 * i)
"""
setAutoExclusive()      设置自动排他
autoExclusive()         是否自动排他，一般按钮都是False, 只有单选按钮是True
对于排他性，只有当按钮设置为可选状态时，才有排他性的意义
"""
#     btn.setAutoExclusive(True)
#     print(btn.autoExclusive())
#     print(btn.isCheckable())
#     btn.setCheckable(True)

# ***************排他性设置***************结束

# *************按钮模拟点击***************开始

# btn = QPushButton(window)
# btn.setText("这是按钮")
# btn.move(200, 200)
# btn.pressed.connect(lambda :print("点击了这个按钮"))
#
# btn.click()
#
# # btn.animateClick(2000)  # 让点击有生气
#
# btn2 = QPushButton(window)
# btn2.setText("按钮2")
# def test():
#     # btn.click()
#     btn.animateClick(1000)
# btn2.pressed.connect(test)

"""
click()     普通点击
animateClick(ms)    动画点击
"""

# *************按钮模拟点击***************结束

# ***************设置点击的有效区域***************开始

import math


class Button(QPushButton):
    def hitButton(self, p) -> bool:
        # if p.x() > 50:
        #     return True
        # else:
        #     return False

        r_x = self.width() / 2
        r_y = self.height() / 2

        distance_x = p.x() - r_x
        distance_y = p.y() - r_y

        d = math.sqrt(distance_x**2 + distance_y**2)

        if d < r_x:
            return True
        else:
            return False

    def paintEvent(self, evt) -> None:
        QPaintEvent
        QPushButton.paintEvent(self, evt)
        paint = QPainter(self)

        pen = QPen(QColor(100,150,200),6)
        paint.setPen(pen)

        paint.drawEllipse(0,0,200,200)



# ***************设置点击的有效区域***************结束

btn = Button(window)
btn.move(100, 100)
btn.setText("点击")
btn.resize(200, 200)

# ***************按钮4种常用的可用信号***************开始

# btn.setCheckable(True)
# btn.pressed.connect(lambda : print("按钮被按下了"))
#
# btn.released.connect(lambda : print("按钮鼠标被释放了"))
#
# btn.clicked.connect(lambda value: print("按钮被点击", value))

btn.toggled.connect(lambda value: print("按钮选中状态发生了改变", value))

"""
pressed
released
clicked   ==>  pressed + released
toggled     只有当按钮是可以被选中的状态时才能触发这个信号
"""

# ***************可用信号***************结束

# 2.3 展示控件
window.show()

# 应用程序执行，进入消息循环
sys.exit(app.exec_())

