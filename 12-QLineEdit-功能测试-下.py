# 0. 导入需要的包和模块
from PyQt5.Qt import *
import sys


# 1. 创建一个应用程序对象
app = QApplication(sys.argv)

# 2. 控件的操作
# 2.1 创建控件
window = QWidget()
# 2.2 设置控件
window.setWindowTitle("QLineEdit-功能测试")
window.resize(500, 500)

le = QLineEdit(window)
le.move(100, 100)
le.resize(300, 300)
# le.setContentsMargins(100, 0, 0, 0)
"""
131.文本边距设定

setContentsMargins      设置文本输入区域与控件边界的边距
"""
le.setStyleSheet("background-color: cyan;")
# le.setTextMargins(0, 0, 50, 50)
"""
131.文本边距设定

setTextMargins(int left，int top，int right，int bottom)   设置文本内容边距
getTextMargins()                                           获取文本内容边距

"""


le.setAlignment(Qt.AlignVCenter)
le.setDragEnabled(True)

"""
132.对齐方式

水平:
Qt.AlignLeft
Qt.AlignRight
Qt.AlignHCenter
Qt.AlignJustify     此处同左对齐

垂直:
Qt.AlignTop
Qt.AlignBottom
Qt.AlignVCenter
Qt.AlignBaseline

Qt.AlignCenter:
等同于    Qt.AlignHCenter | Qt.AlignVCenter
垂直和水平都居中
"""

le2 = QLineEdit(window)
le2.resize(50, 50)
le2.move(200, 0)

btn = QPushButton(window)
btn.setText("按钮")
btn.move(50, 50)


def cursor_move():
    # le.cursorBackward(True, 2)
    # le.cursorForward(True, 3)
    # le.cursorWordBackward(True)
    # le.cursorWordForward(True)
    """
    130.光标位置控制

    cursorBackward(bool mark，int steps = 1) 向后(左)移动steps个字符
	cursorForward(bool mark，int steps = 1)  向前(右)移动steps个字符
	cursorWordBackward(bool mark)            向后(左)移动一个单词长度
	cursorWordForward(bool mark)             向前(右)移动一个单词长度

    mark: True      带选中效果
    mark: False     不带选中效果
    """

    # le.home(True)
    # le.end(False)
    """
    130.光标位置控制
    
    home(bool)      移动到行首
	end(bool)       移动到行尾
	
	True    带选中
	False   不带选中
    """

    # le.setCursorPosition(len(le.text()) / 2)
    # le.setCursorPosition(1.5)
    # print(le.cursorPosition())
    # print(le.cursorPositionAt(QPoint(55, 105)))
    """
    130.光标位置控制
    
    setCursorPosition(int)      设置光标位置,起始值为0
    cursorPosition()            获取光标位置
    cursorPositionAt(const QPoint＆ pos)     获取指定坐标位置对应文本光标位置
    """
    # le.setText("社会我顺哥"*10)
    # le.home(False)
    # le.setFocus()
    # le.cursorBackward(True, 2)
    "光标往前选中两位"
    # le.backspace()
    "退格 backspace()     删除选中文本(如果有)   或   删除光标左侧一个字符"
    # le.del_()
    "删除 del_()      删除选中文本(如果有)   或     删除光标右侧的一个字符"
    # le.clear()
    "清空 clear()     删除所有文本框内容"
    # le.setText("")
    # le.setFocus()

    # le.cursorBackward(True, 3)
    # # le.copy()
    "复制 copy()"
    # le.cut()
    "剪切 cut()"
    # le.setCursorPosition(0)
    # le.paste()
    "粘贴 paste()"

    """
    撤消  isUndoAvailable()   undo()
    重做  isRedoAvailable()   redo()
    """

    # le.setSelection(2, 21)
    # le.selectAll()
    # le.setSelection(0, len(le.text()))
    # le.deselect()
    le.setSelection(2, 3)
    print(le.hasSelectedText())
    """
    文本选中
	setSelection(start_pos, length)
		选中指定区间的文本
	selectAll()
		选中所有文本
	deselect()
		取消选中已选择文本
	hasSelectedText()
		是否有选中文本
	selectedText() -> str
		获取选中的文本
	selectionStart() -> int
		选中的开始位置
	selectionEnd() -> int
		选中的结束位置
	selectionLength() -> int
		选中的长度
    """

    print(le.selectedText())
    print(le.selectionStart())
    print(le.selectionEnd())
    print(le.selectionLength())
    pass


btn.clicked.connect(cursor_move)


le.textEdited.connect(lambda val: print("文本框编辑的时候", val))
le.textChanged.connect(lambda val: print("文本框内容发生改变", val))

# le.returnPressed.connect(lambda :print("回车键被按下"))
# le.returnPressed.connect(lambda :le2.setFocus())
# le.editingFinished.connect(lambda :print("结束编辑"))


# le.cursorPositionChanged.connect(lambda old_Pos, new_Pos: print(old_Pos, new_Pos))
le.selectionChanged.connect(lambda : print("选中文本发生改变", le.selectedText()))

"""
信号
	textEdited( text)
		文本编辑时发射的信号      ！！！(主要指的是用户编辑改变文本时所发出的信号)
	textChanged(text)
		文本框文本发生改变时发出的信号
	returnPressed()
		按下回车键时发出的信号
	editingFinished()
		结束编辑时发出的信号
	cursorPositionChanged(int oldPos，int newPos)
		光标位置发生改变时发出的信号
	selectionChanged()
		选中的文本发生改变时发出的信号
	
	！！！注意：常用的是前四个
"""

le.setText("xxx")

# 2.3 展示控件
window.show()
# 3. 应用程序的执行, 进入到消息循环
sys.exit(app.exec_())

