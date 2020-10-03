# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


class MyWindow(QWidget):
    def keyPressEvent(self, evt) -> None:
        QKeyEvent
        if evt.key() == Qt.Key_Tab:
            print("Tab键被按下")
        elif evt.modifiers() == Qt.ControlModifier and evt.key() == Qt.Key_S:
            print("Ctrl+S被按下")
        elif evt.modifiers() == Qt.ShiftModifier | Qt.AltModifier and evt.key() == Qt.Key_J:
            print("Alt+Shift+J被按下")


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = MyWindow()
# 2.2 设置控件
window.setWindowTitle("事件案例2")
window.resize(500, 500)

window.grabKeyboard()   # 捕获键盘

# 2.3 展示控件
window.show()

# 应用程序执行，进入消息循环
sys.exit(app.exec_())
