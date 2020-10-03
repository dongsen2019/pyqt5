from PyQt5.Qt import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("QLineEdit-登录案例")
        self.setup_ui()
        self.setMinimumSize(400, 400)
        self.resize(500, 500)

        self.btn.clicked.connect(self.btn_click)


    def setup_ui(self):
        le_1 = QLineEdit(self)
        le_1.resize(200, 30)
        self.le_1 = le_1

        le_2 = QLineEdit(self)
        le_2.resize(200, 30)
        le_2.setEchoMode(QLineEdit.Password)
        self.le_2 = le_2

        btn = QPushButton(self)
        btn.resize(60, 30)
        btn.setText("登录")
        self.btn = btn

        # 占位文本的提示

        self.le_1.setPlaceholderText("请输入账号")
        self.le_2.setPlaceholderText("请输入密码")
        """
        119.占位文本的设置
        
        setPlaceholderText(notice_str)  设置文本占位符，在用户输入文本内容之前, 给用户的提示语句
        placeholderText()       获取文本占位符内容
        """

        # 设置密码文本框，自动显示清空按钮

        self.le_2.setClearButtonEnabled(True)
        print(self.le_2.isClearButtonEnabled())
        """
        120.清空显示的按钮
        
        setClearButtonEnabled(bool)     设置清除按钮
        isClearButtonEnabled() -> bool  返回是否使用清除按钮
        """


        action = QAction(self.le_2)
        action.setIcon(QIcon("E:\pycharm\pyqt5\source/close.png"))

        def change():
            if self.le_2.echoMode() == QLineEdit.Password:
                self.le_2.setEchoMode(QLineEdit.Normal)
                action.setIcon(QIcon("E:\pycharm\pyqt5\source/open.png"))
            else:
                self.le_2.setEchoMode(QLineEdit.Password)
                action.setIcon(QIcon("E:\pycharm\pyqt5\source/close.png"))

        action.triggered.connect(change)

        self.le_2.addAction(action, QLineEdit.TrailingPosition)

        """
        121.添加自定义行为
        
        创建行为，为行为添加图标，点击触发行为时发送信号所连接的槽函数
        """


        completer = QCompleter(["Sz", "shunzi", "wangzha"], self.le_1)
        self.le_1.setCompleter(completer)

        """
        122-自动补全联想

        构造完整器和设置完整器
        """


    def resizeEvent(self, evt) -> None:
        self.le_1.move(self.width() / 2 - 100, self.height() / 4 - 5)
        self.le_2.move(self.width() / 2 - 100, self.height() / 4 * 2 - 5)
        self.btn.move(self.width() / 2 - 30, self.height() / 4 * 3 - 15)

    def btn_click(self):
        print(self.le_1.text())
        if self.le_1.text() == "sz":
            if self.le_2.text() == "itlike":
                print("登录成功")
            else:
                self.le_2.clear()
        else:
            self.le_1.clear()
            self.le_2.clear()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())