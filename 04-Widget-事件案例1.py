from PyQt5.Qt import *
import sys


class Label(QLabel):
    def enterEvent(self, ee):
        self.setText("欢迎光临")

    def leaveEvent(self, le):
        self.setText("谢谢惠顾")


app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)

label = Label(window)
label.setText("社会我顺哥，人狠话不多")
label.move(200, 200)

window.show()

sys.exit(app.exec_())


