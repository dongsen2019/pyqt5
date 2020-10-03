from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        line_edit = QLineEdit(self)
        line_edit.resize(200, 30)
        line_edit.move(150, 80)
        line_edit.setText("")
        print(line_edit.text())
        self.line_edit = line_edit

        push_button = QPushButton(self)
        push_button.resize(80, 30)
        push_button.move(210, 160)
        push_button.setText("按钮")
        push_button.setEnabled(False)
        self.push_button = push_button

        label = QLabel(self)
        label.resize(160, 30)
        label.move(170, 240)
        label.setStyleSheet("background: red")
        label.setVisible(False)
        self.label = label

        def text_cao(text):
            label.setVisible(False)
            if len(text) > 0:
                self.push_button.setEnabled(True)
            else:
                self.push_button.setEnabled(False)

        self.line_edit.textChanged.connect(text_cao)

        def label_cao():
            if line_edit.text() == "Sz":
                label.setText("登陆成功")
            else:
                label.setText("登录失败")

            label.show()

        self.push_button.pressed.connect(label_cao)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
