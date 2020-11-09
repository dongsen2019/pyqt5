from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QProgressDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pd = QProgressDialog(self)
        """
        构造函数
            QProgressDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
            QProgressDialog(str, str, int, int, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
        
        界面内容设置
            对话框标题       setWindowTitle(str)
            标签文本         setLabelText(str)
                            labelText() -> str
            取消按钮文本     setCancelButtonText(cancelButtonText_str)
            子控件设置       setBar(QProgressBar bar)
                            setCancelButton(QPushButton cancelButton)
                            setLabel(QLabel label)
        """

        # pd = QProgressDialog("xx1", "xx2", 1, 1000, self)
        "                       提示标签，取消按钮文本，区间左值，区间右值，父对象"
        pd.setWindowTitle("xx3")
        "对话框标题      setWindowTitle(str)"

        pd.setLabelText("下载进度")
        """
        标签文本
            setLabelText(str)
            labelText() -> str
        """

        pd.setCancelButtonText("取消下载")

        pd.setRange(0, 100)
        pd.setValue(95)
        print(pd.minimum())
        print(pd.maximum())

        # pd.setAutoClose(False)
        # pd.setAutoReset(False)
        """
        自动操作
            setAutoClose(bool close)    autoClose() -> bool     当进度拉满，自动关闭
            setAutoReset(bool reset)    autoReset() -> bool     当进度拉满，自动重置为进度0%
            reset()     手动重置
        """

        # pd.open(lambda :print("对话框被取消"))
        "当点击对话框的取消按钮，激活槽函数"
        pd.show()
        # pd.setMinimumDuration(0)
        """
        自动弹出(默认时超过四秒钟，进度条还没有读到100%，将自动弹出进度条窗口)
            最小展示时长
                setMinimumDuration(int ms)      默认4秒
                minimumDuration() -> int        
                展示之前的等待时间
                    如果在等待直接内, 进度条满了, 就不会弹出
                    否则, 会被弹出
        """
        # for i in range(1, 101):
        #     # import time
        #     # time.sleep(1)
        #     pd.setValue(i)
        timer = QTimer(pd)

        def test():
            # if pd.value() + 1 >= pd.maximum() or pd.wasCanceled():
            if pd.value() + 1 >= pd.maximum():
                timer.stop()
                print(pd.autoClose())
            pd.setValue(pd.value() + 1)

            if pd.value() == 98:
                pd.cancel()

        timer.timeout.connect(test)
        timer.start(1000)

        pd.canceled.connect(timer.stop)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
