from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressBar的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pb = QProgressBar(self)
        "构造函数       QProgressBar(self)"
        pb.resize(400, 40)
        # print(pb.minimum())
        # print(pb.maximum())
        #
        # pb.setMinimum(50)

        pb.setRange(0, 80)

        pb.setValue(20)
        """
        设置范围和当前值
            setMinimum(self, int)       minimum() -> int
            setMaximum(self, int)       maximum() -> int
            setRange(self, int, int)    setValue(self, int)
            reset()     重置，清空当前进度值，不改变区间范围
            value()     获取值
        注意
            最大值和最小值如果都是0, 则进入繁忙提示
        """

        # pb.setFormat("当前人数{} / 总人数 %m".format(pb.value() - pb.minimum()))
        """
        setFormat(self, str)
            ％p      百分比
            ％v      当前值
            ％m      总值
        """
        pb.setInvertedAppearance(True)
        "倒立外观       setInvertedAppearance(bool)"

        # pb.setRange(0, 0)
        "该设置应用场景为繁忙时"

        # pb.reset()
        "reset()     重置，清空当前进度值，不改变区间范围"

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试按钮")

        def test():
            # pb.reset()
            # print(pb.minimum())
            # print(pb.maximum())
            # print(pb.value())
            # pb.resetFormat()
            pb.setAlignment(Qt.AlignHCenter)
            """
            格式字符对齐方式
                setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag])
            
            resetFormat()       重置为默认格式
            format() -> str
            """

            # print(pb.text())
            "text()       获取文本"

            pb.setOrientation(Qt.Vertical)
            """
            方向
                setOrientation(Qt.Orientation)
                    Qt.Horizontal
                    Qt.Vertical
                orientation() -> Qt.Orientation
            
            改变进度条水平和垂直方向以后，需要设置进度条的长宽尺寸，才能达到需求
            垂直进度条，无法显示文本
            """

            pb.resize(40, 400)
            print(pb.isTextVisible())
            pb.setTextDirection(QProgressBar.TopToBottom)
            pb.setInvertedAppearance(True)
            "倒立外观       setInvertedAppearance(bool)"

        btn.clicked.connect(test)

        timer = QTimer(pb)

        def change_progress():
            # print("xxx")
            if pb.value() == pb.maximum():
                timer.stop()
            pb.setValue(pb.value() + 1)
            pass
        timer.timeout.connect(change_progress)

        timer.start(1000)
        
        pb.valueChanged.connect(lambda val:print("当前的进度值为", val))

        # pb.setTextVisible(False)
        """
        文本操作
            setTextVisible(bool)    设置进度条文本是否显示
            text()                  获取文本
            
            setTextDirection(QProgressBar.Direction)
                BottomToTop = 1
                TopToBottom = 0
                仅仅对于垂直进度条有效
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
