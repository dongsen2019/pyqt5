# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("按钮组的使用")
window.resize(500, 500)


# 创建四个单选按钮
# 男女
r_male = QRadioButton("男", window)
r_female = QRadioButton("女", window)
r_male.move(100, 100)
r_female.move(100, 150)
r_male.setChecked(True)

sex_group = QButtonGroup(window)
sex_group.addButton(r_male, 1)
sex_group.addButton(r_female, 2)
"""
QButtonGroup    创建按钮组
addButton       为按钮组添加按钮
按钮组中的选项都具有排他性
"""

# 是否
r_yes = QRadioButton("是", window)
r_no = QRadioButton("否", window)
r_yes.move(300, 100)
r_no.move(300, 150)
answer_group = QButtonGroup(window)
answer_group.addButton(r_yes)
answer_group.addButton(r_no)
"""
addButton(self, QAbstractButton, id=-1)     构造函数中可以设置id值
"""

answer_group.setId(r_yes, 1)
answer_group.setId(r_no, 2)

"""
setId   设置id值
"""

print(answer_group.id(r_yes))
print(answer_group.id(r_no))
r_no.setChecked(True)
print(answer_group.checkedId())

"""
setId(QAbstractButton，int)
id(QAbstractButton)     指定按钮对应的ID，如果不存在此按钮，则返回-1
checkedId()             选中的ID，如果没有选中按钮则返回-1
"""

# sex_group.setExclusive(False)
"""
为按钮组设置排他性属性
"""

# sex_group.removeButton(r_female)
# print(sex_group.buttons())
# print(sex_group.button(2))
# print(sex_group.checkedButton())
"""
buttons()   查看所有按钮组中的按钮
button(ID)  根据ID获取对应按钮, 没有则返回None
checkedButton()     获取选中的那个按钮
removeButton(QAbstractButton)   从group中移除指定按钮
"""

def test(val):
    # print(val)
    print(sex_group.id(val))    # 也可以传第一参数，然后用id()进行查看id
sex_group.buttonClicked.connect(test)
# sex_group.buttonClicked[int].connect(test)    传输触发信号按钮的ID

"""
buttonClicked(self, QAbstractButton) [signal]
            buttonClicked(self, int) [signal]

signal_name[type]   
信号名称    signal_name
参数类型    type
"""



# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())

