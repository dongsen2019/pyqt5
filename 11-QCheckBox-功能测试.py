# 0. 导入需要的包和模块
from PyQt5.Qt import * 
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QCheckBox 功能测试")
window.resize(500, 500)

# print(QCheckBox.__bases__)

cb = QCheckBox("&Python", window)
cb.setIcon(QIcon("xxx.png"))
cb.setIconSize(QSize(60, 60))
cb.setTristate(True)
"""
设置三态，第三态为部分选中
checkState()    获取当下的状态
"""

# cb.setChecked(True)
# cb.setCheckState(Qt.PartiallyChecked)
cb.setCheckState(Qt.Checked)
"""
Qt.Unchecked    该项目未选中
Qt.PartiallyChecked 部分选中
Qt::Checked     真的被选中
"""

# cb.stateChanged.connect(lambda state: print(state))
cb.toggled.connect(lambda isChecked: print(isChecked))
"""
stateChanged(int state) 选中或清除选中时, 发射此信号
比二态多了一种值 （0，1，2）
"""
# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())