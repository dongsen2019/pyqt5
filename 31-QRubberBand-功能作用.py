from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QRubberBand的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        rb = QRubberBand(QRubberBand.Rectangle, self)
        """
        构造函数
            QRubberBand(QRubberBand.Shape, QWidget)
                QRubberBand.Line
                QRubberBand.Rectangle
        """

        rb.setGeometry(10, 10, 60, 60)
        "设置皮筋尺寸"

        print(rb.isVisible())
        rb.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

