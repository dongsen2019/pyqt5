# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
# window = QWidget(flags=Qt.FramelessWindowHint)
window = QWidget()

# 2.2 设置控件
window.setWindowTitle("顶层窗口操作-案例")
window.resize(500, 500)

window.setWindowFlags(Qt.FramelessWindowHint)
window.setWindowOpacity(0.9)

# 按钮尺寸
btn_w = 80
btn_h = 40

# 关闭按钮
close_btn = QPushButton(window)
close_btn.resize(btn_w, btn_h)
close_btn.setText("关闭")

close_btn_x = window.width() - btn_w
close_btn_y = 10
close_btn.move(close_btn_x, close_btn_y)


def close_cao():
    window.close()


close_btn.pressed.connect(close_cao)

# 最大化按钮
max_btn = QPushButton(window)
max_btn.resize(btn_w, btn_h)
max_btn.setText("最大化")

max_btn_x = close_btn_x - btn_w
max_btn_y = 10
max_btn.move(max_btn_x, max_btn_y)


def max_normal():
    if window.isMaximized():
        # window.showMaximized()
        window.setWindowState(Qt.WindowNoState)
        max_btn.setText("最大化")
    else:
        window.setWindowState(Qt.WindowMaximized)
        max_btn.setText("还原")


max_btn.pressed.connect(max_normal)

# 最小化按钮
min_btn = QPushButton(window)
min_btn.resize(btn_w, btn_h)
min_btn.setText("最小化")

min_btn_x = max_btn_x - btn_w
min_btn_y = 10
min_btn.move(min_btn_x, min_btn_y)


def min_cao():
    # window.showMinimized()
    window.setWindowState(Qt.WindowMinimized)


min_btn.pressed.connect(min_cao)

# 2.3 展示控件
window.show()

# 应用程序执行，进入消息循环
sys.exit(app.exec_())

