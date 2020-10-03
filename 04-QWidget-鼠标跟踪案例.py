from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mouseMoveEvent(self, me) -> None:
        lbl = self.findChild(QLabel)
        print("鼠标移动了", me.localPos())
        lbl.move(me.localPos().x(), me.localPos().y())


app = QApplication(sys.argv)

window = Window()
window.resize(500, 500)

label = QLabel(window)
label.setStyleSheet("background-color: cyan;")
label.setText("社会我顺哥，人狠话不多")
label.move(250, 250)

pixmap = QPixmap("E:/pycharm/pyqt5/source/xxx.png").scaled(50, 50)
cursor = QCursor(pixmap)
window.setCursor(cursor)

window.setMouseTracking(True)

window.show()

sys.exit(app.exec_())
