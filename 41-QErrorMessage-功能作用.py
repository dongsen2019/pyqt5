from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QErrorMessage的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # em = QErrorMessage(self)
        """
        构造函数    QErrorMessage（QWidget * parent = nullptr）
        """
        # em.setWindowTitle("错误提示")
        "设置错误提示对话框标题"
        #
        # em.showMessage("社会我顺哥, 人狠话不多")
        "设置错误提示的内容"
        # em.showMessage("社会我顺哥, 人狠话不多")
        # em.showMessage("社会我顺哥, 人狠话不多")
        # em.showMessage("社会我顺哥, 人狠话不多4")

        # em.open()
        # em.exec()
        pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    QErrorMessage.qtHandler()
    # qDebug("xxxx")
    qWarning("123456")
    """
    展示级别信息
        QErrorMessage.qtHandler()       调用上述方法后, 后续所有的方法均会使用对话框显示
        qDebug()                        调试消息
        qWarning()                      警告消息和可恢复的错误
        ...
    """

    sys.exit(app.exec_())
