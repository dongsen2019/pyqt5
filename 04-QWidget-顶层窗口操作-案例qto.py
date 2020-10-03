from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("顶层窗口操作oop")
        self.resize(500, 500)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowOpacity(0.9)
        # 按钮尺寸
        self.btn_w = 80
        self.btn_h = 40
        # 标记
        self.flag = False

        self.setup_ui()

    def setup_ui(self):
        # 关闭按钮
        close_btn = QPushButton(self)
        close_btn.resize(self.btn_w, self.btn_h)
        close_btn.setText("关闭")
        self.close_btn = close_btn

        def close_cao():
            self.close()

        close_btn.pressed.connect(close_cao)

        # 最大化按钮
        max_btn = QPushButton(self)
        max_btn.resize(self.btn_w, self.btn_h)
        max_btn.setText("最大化")
        self.max_btn = max_btn

        def max_normal():
            if self.isMaximized():
                # window.showMaximized()
                self.setWindowState(Qt.WindowNoState)
                max_btn.setText("最大化")
            else:
                self.setWindowState(Qt.WindowMaximized)
                max_btn.setText("还原")

        self.max_btn.pressed.connect(max_normal)

        # 最小化按钮
        min_btn = QPushButton(self)
        min_btn.resize(self.btn_w, self.btn_h)
        min_btn.setText("最小化")
        self.min_btn = min_btn

        def min_cao():
            # window.showMinimized()
            print(self)
            self.setWindowState(Qt.WindowMinimized)

        self.min_btn.pressed.connect(min_cao)

    def resizeEvent(self, QResizeEvent) -> None:
        close_btn_x = self.width() - self.btn_w
        close_btn_y = 10
        self.close_btn.move(close_btn_x, close_btn_y)

        max_btn_x = close_btn_x - self.btn_w
        max_btn_y = 10
        self.max_btn.move(max_btn_x, max_btn_y)

        min_btn_x = max_btn_x - self.btn_w
        min_btn_y = 10
        self.min_btn.move(min_btn_x, min_btn_y)

    def mousePressEvent(self, me) -> None:
        if me.button() == Qt.LeftButton:
            self.flag = True
            self.wd_origin_x = self.pos().x()
            self.wd_origin_y = self.pos().y()
            self.mouse_x = me.globalX()
            self.mouse_y = me.globalY()

    def mouseMoveEvent(self, me) -> None:
        if self.flag == True:
            move_x = me.globalX() - self.mouse_x
            move_y = me.globalY() - self.mouse_y
            self.move(self.wd_origin_x+move_x, self.wd_origin_y+move_y)

    def mouseReleaseEvent(self, me) -> None:
        print("鼠标被释放了！")
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())

