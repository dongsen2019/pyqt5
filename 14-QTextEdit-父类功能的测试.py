# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QTextEdit父类功能测试")
window.resize(500, 500)


te = QTextEdit("社会顺哥", window)

te.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
te.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
"""
setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy)
setVerticalScrollBarPolicy(Qt.ScrollBarPolicy)

Qt.ScrollBarPolicy:
Qt.ScrollBarAsNeeded    当内容太大而不适合时，QAbstractScrollArea显示滚动条。这是默认值。
Qt.ScrollBarAlwaysOff   QAbstractScrollArea从不显示滚动条。
Qt.ScrollBarAlwaysOn    QAbstractScrollArea始终显示滚动条。具有瞬态滚动条的系统会忽略此属性（例如，在版本10.7的Mac上）。

具体的枚举值见Xmind的笔记，以及图片样式表
"""

btn = QPushButton(window)
btn.setIcon(QIcon("xxx.png"))
btn.pressed.connect(lambda :print("xxx"))

te.setCornerWidget(btn)

"""
setCornerWidget(QWidget *widget)    设置右下角控件
"""

# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())
