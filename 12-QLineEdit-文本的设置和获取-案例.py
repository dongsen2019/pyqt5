# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("文本的设置和获取-案例")
window.resize(500, 500)

le1 = QLineEdit(window)
le1.move(100, 100)

btn = QPushButton(window)
btn.move(200, 200)

le2 = QLineEdit(window)
le2.move(300, 300)

def copy_cao():
    str = le1.text()
    le2.setText(str)


btn.clicked.connect(copy_cao)

# 2.3 展示控件
window.show()

# 应用程序执行，进入消息循环
sys.exit(app.exec_())