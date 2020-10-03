from PyQt5.Qt import *
import sys


class Window(QWidget):
    def mouseMoveEvent(self, me) -> None:
        # QMouseEvent
        print("鼠标移动了", me.localPos())


app = QApplication(sys.argv)

window = Window()

print(window.hasMouseTracking())
window.setMouseTracking(True)
print(window.hasMouseTracking())

window.show()

sys.exit(app.exec_())



