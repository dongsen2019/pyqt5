# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QDialog")
window.resize(500, 500)

d = QDialog(window)

btn1 = QPushButton(d)
btn1.setText("btn1")
btn1.move(20, 20)
btn1.clicked.connect(lambda :d.accept())

btn2 = QPushButton(d)
btn2.setText("btn2")
btn2.move(60, 60)
btn2.clicked.connect(lambda :d.reject())
# btn2.clicked.connect(lambda :print(d.result()))

btn3 = QPushButton(d)
btn3.setText("btn3")
btn3.move(60, 160)
btn3.clicked.connect(lambda :d.done(8))
# btn3.clicked.connect(lambda :d.setResult(888))

"""
常用操作槽
    accept()        结束对话框并返回1
    reject()        结束对话框并返回0
    done(int r)     结束对话框并返回 int r
    
设置和获取数值
    setResult(int)
    result() -> int     不结束对话框，返回 int 值
"""

d.accepted.connect(lambda :print("点击了, 接受按钮"))
d.rejected.connect(lambda :print("点击了, 拒绝按钮"))
d.finished.connect(lambda val:print("点击了, 完成按钮", val))

"""
信号
    accepted()              执行accept操作时，发送信号
    finished(int result)    结束对话框时
    rejected()              执行reject操作时，发送信号
"""

d.setWindowTitle("对话框")
# d.setModal(True)
# d.setWinndowModality(Qt.WindowModal)
# d.setSizeGripEnabled(True)

"""
是否显示尺寸调整控件  (窗口右下角有个小箭头可以拖拽使得窗口变大变小)
    setSizeGripEnabled(bool)
    isSizeGripEnabled() -> bool
"""

# d.show()
result = d.exec()

"""
模态对话框   
    分类:
        应用程序级别  默认值
            exec()    当该种模态的对话框出现时，用户必须首先对对话框进行交互，
                      直到关闭对话框，然后才能访问程序中其他的窗口
        窗口级别
            open()    该模态仅仅阻塞与对话框关联的窗口，但是依然允许用户与程序中其它窗口交互

    应用场景
        文件选择
        是否同意
        ...


非模态对话框
    show()      不会阻塞与对话框关联的窗口以及与其他窗口进行交互
    
    show()      结合setModal(True)也可以实现模态对话框
    show()      结合setWindowModality(Qt.WindowModal)也可以实现模态对话框
                    Qt.WindowModal
                    Qt.ApplicationModal

    应用场景
        查找替换
"""

print(result)
# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())
