# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


class Window(QWidget):
    def paintEvent(self, evt):
        print("窗口被绘制了")
        return super().paintEvent(evt)


class Btn(QPushButton):
    def paintEvent(self, evt):
        print("按钮被绘制了")
        return super().paintEvent(evt)


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = Window()
# 2.2 设置控件
window.setWindowTitle("交互状态[*]")
window.resize(500, 500)

window.setWindowModified(True)
"""
window.setWindowModified(True)      设置窗口为被编辑状态，显示*
print(window.isWindowModified())    获取窗口是否是被编辑状态
"""

btn = Btn(window)
btn.setText("按钮")
btn.destroyed.connect(lambda : print("按钮被释放了"))
print(btn.isEnabled())
btn.setEnabled(False)
print(btn.isEnabled())
"""
setEnabled() 设置控件是否可用
isEnabled()  获取控件是否可用
"""

# btn.setVisible(False)
# btn.setHidden(True)
# btn.hide()
# btn.close()
"""
基于 setVisible(bool)     的三个马甲
setHidden(bool)
hide()
show()
所谓的显示和隐藏本质是控件有没有被绘制出来
而不是这个对象有没有存在

此外，如果父控件没有被展示，即使子控件设置为setVisible(True)
它也不会被展示

close() 控件被关闭 
当未设置
setAttribute(Qt.WA_DeleteOnClose, True)
作用相当于setVisible，控件没有被释放

否则将会被释放
"""

# btn.deleteLater()
# btn.setAttribute(Qt.WA_DeleteOnClose, True)
# btn.close()
# btn.setVisible(False)

# 2.3 展示控件
window.show()

"""
isActiveWindow()    获取该窗口是否为活跃窗口
"""
                       # show()  注释show()
print(btn.isHidden())  # False   False
print(btn.isVisible())  # True   False
print(btn.isVisibleTo(window)) # True
"""
isHidden()          判定控件是否隐藏    一般是基于父控件可见
isVisible()         获取控件最终状态是否可见
isVisibleTo(widget) 如果能随着widget控件的显示和隐藏, 而同步变化, 则返回True
"""

# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())