# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# class Label(QLabel):
#     def mousePressEvent(self, evt) -> None:
#         # QMouseEvent
#         if evt.button() == Qt.LeftButton:
#             self.setStyleSheet("background-color: red")

class Window(QWidget):
    def mousePressEvent(self, evt) -> None:
        # QMouseEvent
        local_x = evt.localPos().x()
        local_y = evt.localPos().y()
        sub_widget = self.childAt(local_x, local_y)
        if sub_widget is not None:
            sub_widget.setStyleSheet("background-color: red")


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("父子关系-案例")
window.resize(500, 500)

for i in range(10):
    label = QLabel(window)
    label.move(40 * i, 40 * i)
    label.setText(f"标签{i}")

# 2.3 展示控件
window.show()

# 应用程序执行，进入消息循环
sys.exit(app.exec_())
