from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontComboBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        label = QLabel(self)
        label.setText("社会我顺哥, 人狠话不多")
        label.move(100, 100)

        fcb = QFontComboBox(self)
        fcb.currentFontChanged.connect(lambda font: label.setFont(font))
        fcb.setEditable(False)

        """
        信号
            继承  currentIndexChanged(QString text)
            当前字体改变发送信号 currentFontChanged(QFont font)
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()

    sys.exit(app.exec_())