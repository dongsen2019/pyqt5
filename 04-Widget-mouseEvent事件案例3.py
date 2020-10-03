from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.flag = False
        # self.setup_ui()

    def mousePressEvent(self, evt) -> None:
        if evt.button() == Qt.LeftButton:
            self.flag = True
            self.mouse_x = evt.globalX()
            self.mouse_y = evt.globalY()
            self.origin_x = self.pos().x()
            self.origin_y = self.pos().y()

    def mouseMoveEvent(self, evt) -> None:
        if self.flag == True:
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y
            self.move(self.origin_x + move_x, self.origin_y + move_y)

    def mouseReleaseEvent(self, evt) -> None:
        print("鼠标释放")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
