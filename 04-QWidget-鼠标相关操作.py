from PyQt5.Qt import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)

# 对某个控件的鼠标图标设置类型，更多类型见Xmind
window.setCursor(Qt.UpArrowCursor)

# 为鼠标设置自定义的图标类型
pixmap = QPixmap("E:/pycharm/pyqt5/source/xxx.png")  # 图片对象

# 缩放鼠标图标大小
new_pixmap = pixmap.scaled(50, 50)   # return QPixmap

# 设置鼠标图标生效的点击位
cuisor = QCursor(pixmap, 0, 0)    # 鼠标对象（讲鼠标样式转换为图片）
"""
(-1,-1) 表示中心
(0,0) 表示左上角
"""

window.setCursor(cuisor)

# 重置鼠标形状
window.unsetCursor()

# 获取和设置鼠标所在位置
print(window.cursor().pos())
window.cursor().setPos(100, 100)

"""
window.cursor().pixmap() 获取鼠标图片
window.cursor().pos()   获取鼠标位置
"""


window.show()

sys.exit(app.exec_())
