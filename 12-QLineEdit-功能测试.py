# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys

"""
QLineEdit是一个单行文本编辑器,允许用户输入和编辑单行纯文本
"""

# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QLineEdit功能测试")
window.resize(500, 500)

"""
# 113.控件创建

QLineEdit(parent: QWidget = None)
QLineEdit(str, parent: QWidget = None)
"""

le_a = QLineEdit(window)
le_a.move(100, 200)

le_b = QLineEdit(window)
le_b.move(100, 300)

# le_b.setEchoMode(QLineEdit.PasswordEchoOnEdit)
# print(le_b.echoMode())

"""
# 116.文本输出模式

NoEcho = 1      不输出
Normal = 0      正常输出
Password = 2    密文形式
PasswordEchoOnEdit = 3      编辑时明文, 结束后密文
setEchoMode(QLineEdit.PasswordEchoOnEdit)   设置输出模式
echoMode() -> QLineEdit.EchoMode        获取输出模式
"""

copy_btn = QPushButton(window)
copy_btn.setText("复制")
copy_btn.move(100, 400)

def copy_cao():
    # 1. 获取文本框a, 内容
    # content = le_a.text()
    # # 2. 把上面获取到的内容, 设置到文本框B里面
    # # le_b.setText(content)
    # # le_b.setText("")
    # # le_b.insert(content)
    # print(le_b.text())
    # print(le_b.displayText())
    print(le_b.isModified())
    le_b.setModified(False)
    print(le_b.isModified())


"""
129.文本修改状态

isModified()    检测文本内容是否被修改
setModified(bool)   标识文本内容是否被修改
"""

copy_btn.clicked.connect(copy_cao)

"""
# 114-115.文本的设置与获取

setText(str)        设置内容文本
insert(newText)     在光标处插入文本
text()              获取真实内容文本
displayText()       获取用户能看到的内容文本
"""


# 最大长度限制
le_a.setMaxLength(3)
print(le_a.maxLength())
"""
# 123.文本内容限制-长度和只读限制

setMaxLength(int)    设置限制输入的长度
maxLength()          获取输入长度  
"""

le_a.setReadOnly(True)

le_a.setText("王炸, 要不起!")
""" 
# 123.文本内容限制-长度和只读限制

setReadOnly     只读限制(但是可以通过代码设置文本，代码设置的文本也无法超越长度限制的值)
isReadOnly()     获取只读限制
"""

# le_b 设置掩码
# 总共输入5 位  左边 2(必须是大写字母) - 右边 2(必须是一个数字)
# le_b.setInputMask(">AA-99;#")
# le_b.setInputMask("9999-9999999;0")

"""
setInputMask(mask_str)  设置掩码验证

掩码可以指定固定位置的固定数据类型, 达到一个格式上的限制

例如:
座机号码    四位区号-七位电话
IP地址      XXX.XXX.XXX.XXX

掩码由一串掩码字符和分隔符组成     +   可选的分号; 和 空白占位字符

!!!掩码字符见 Xmind 笔记的图片
"""


# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())