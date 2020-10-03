# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mousePressEvent(self, QMouseEvent):

        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.resize(500, 500)
window.setWindowTitle("w1")

# icon = QIcon("E:\BaiduNetdiskDownload\pyqt5\代码\PyQt5\source/xxx.png")
# window.setWindowIcon(icon)
"""
setWindowIcon()     将窗口图标替换为QIcon对象的图片
"""
# # QIcon
# print(window.windowIcon())
"""
windowIcon()        获取窗口图标
"""

# window.setWindowTitle("社会我顺哥,")
# print(window.windowTitle())
"""
setWindowTitle()    设置窗口标题
window.windowTitle()    获取窗口标题
"""

# window.setWindowOpacity(0.9)
# print(window.windowOpacity())
"""
setWindowOpacity()      设置窗口的不透明度
windowOpacity()         获取窗口的不透明度
"""

# print(window.windowState() == Qt.WindowNoState)

# window.setWindowState(Qt.WindowMinimized)
# window.setWindowState(Qt.WindowMaximized)
# window.setWindowState(Qt.WindowFullScreen)

"""
设置为
Qt.WindowNoState    无状态
Qt.WindowMinimized  最小化
Qt.WindowMaximized  最大化
Qt.WindowFullScreen 全屏
Qt.WindowActive     活动窗口
"""


# w2 = QWidget()
# w2.setWindowTitle("w2")


# 2.3 展示控件
window.show()

# window.showMaximized()

# window.showFullScreen()
# window.showMinimized()

# window.setWindowState(Qt.WindowActive)

"""
展示为
window.showMaximized()      最大化
window.showFullScreen()     全屏
window.showMinimized()      最小化
window.showNormal()         正常化

判定
isMinimized()               最小化
isMaximized()               最大化
isFullScreen()              全屏
"""

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())
