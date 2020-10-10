from PyQt5.Qt import *


class MyASB(QAbstractSpinBox):
    def __init__(self, parent=None, num ="0", *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.lineEdit().setText(num)

    def stepEnabled(self):
        # 0 -- 9
        # current_num = int(self.text())
        # if current_num == 0:
        #     return QAbstractSpinBox.StepUpEnabled
        # elif current_num == 9:
        #     return QAbstractSpinBox.StepDownEnabled
        # elif current_num < 0 or current_num > 9:
        #     return QAbstractSpinBox.StepNone
        # else:
        return QAbstractSpinBox.StepUpEnabled | QAbstractSpinBox.StepDownEnabled
    """
        1. 子类化此类
        2. 实现控制上下能用的方法
            stepEnabled(self) -> QAbstractSpinBox.StepEnabled
                QAbstractSpinBox.StepNone
                    都不能用
                QAbstractSpinBox.StepUpEnabled
                    上可用
                QAbstractSpinBox.StepDownEnabled
                    下可用
    """

    def stepBy(self, p_int):
        current_num = int(self.text()) + p_int
        self.lineEdit().setText(str(current_num))
        "lineEdit()     获取步长调节器左边的文本框，用于设置文本内容"

        """
        当点击向上或者向下键时，调用此方法
        
        3. 实现步长调整方法
            stepBy(self, p_int)
        """

    def validate(self, p_str, p_int):   # p_int表示光标位置
        # 18 - 180
        num = int(p_str)
        if num < 18:
            return (QValidator.Intermediate, p_str, p_int)
        elif num <= 180:
            return (QValidator.Acceptable, p_str, p_int)
        else:
            return (QValidator.Invalid, p_str, p_int)


    def fixup(self, p_str):
        print(p_str)
        return "18"


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        asb = MyASB(self, "6")
        self.asb = asb
        asb.resize(100, 30)
        asb.move(100, 100)

        self.asb.editingFinished.connect(lambda :print("结束编辑"))
        """
        editingFinished()       结束编辑时调用(按下enter键或者使控件失去焦点时)
        """

        # print(asb.isAccelerated())
        # asb.setAccelerated(True)
        # print(asb.isAccelerated())
        """
        长按调整步长加快频率:
            setAccelerated(bool)
            isAccelerated() -> bool
        """

        # print(asb.isReadOnly())
        # asb.setReadOnly(True)
        """
        只读:
        setReadOnly(bool r)
        isReadOnly() -> bool
        
        此处的只读只限制文本框的内容只读，不限制小控件上下按钮的修改操作
        """

        test_btn = QPushButton(self)
        test_btn.move(200, 200)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

    def btn_test(self):
        # print(self.asb.text())
        # # print(self.asb.lineEdit().text())
        "获取步长调节器左侧的单行文本编辑器，再用text()方法获取内容"
        # print(self.asb.lineEdit().setText("88"))
        "设置单行文本编辑器的内容"
        # QLineEdit
        # cl = QCompleter(["sz", "123", "18"], self.asb)
        # self.asb.lineEdit().setCompleter(cl)
        "测试步长调节器能否使用完整器"
        # # self.asb.lineEdit().setAlignment(Qt.AlignCenter)
        "测试步长调节器能否使用对齐方式"

        "大部分的QLineEdit方法均可在步长调节器的lineEdit中使用"

        # self.asb.setAlignment(Qt.AlignCenter)
        """
        对齐方式(asb层级)：
            setAlignment(Qt.Alignment)
            alignment() -> Qt.Alignment
        """

        # print(self.asb.hasFrame())
        # self.asb.setFrame(False)
        """
        设置周边框架(显示或去除空间的边框)
            setFrame(bool)
                默认True
            hasFrame() -> bool
        """

        # self.asb.clear()  清空文本框内容
        self.asb.setButtonSymbols(QAbstractSpinBox.NoButtons)
        """
        NoButtons = 2   无按钮
        PlusMinus = 1   + -
        UpDownArrows = 0 箭头按钮
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
