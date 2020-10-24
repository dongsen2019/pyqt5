from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDial的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        label = QLabel(self)
        label.move(200, 100)
        label.setText("社会我顺哥, 人狠话不多")

        dia = QDial(self)

        dia.setRange(0, 200)

        def test(val):
            label.setStyleSheet("font-size: {}px;".format(val))
            "根据数值大小设置字体大小"
            label.adjustSize()
        dia.valueChanged.connect(test)

        dia.setNotchesVisible(True)
        "显示刻度"
        dia.setPageStep(5)

        dia.setWrapping(True)
        "设置为数值循环后，刻度包裹控件"
        dia.setNotchTarget(10)
        "设置多少个数值添加一个刻度"


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()

    sys.exit(app.exec_())
