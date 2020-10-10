from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTimeEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        te = QTimeEdit(QTime.currentTime(), self)
        """
        构造函数
            QTimeEdit(QWidget *parent = nullptr)
            QTimeEdit(const QTime &time, QWidget *parent = nullptr)
        """

        te.setDisplayFormat("hh=m-ss:zzz a")
        """
        设置展示的section格式
            setDisplayFormat(format_str)
                设置日期时间显示格式
            displayFormat() -> str
                获取日期时间显示格式
        
        时间日期格式符 见 21-QDateTimeEdit-功能测试 
        """

        print(te.time())    # 获取时间  time() -> QTime

        """
        时间
            最大
                setMaximumTime(QTime)
                maximumTime() -> QTime
                clearMaximumTime()
            最小
                setMinimumTime(QTime)
                minimumTime() -> QTime
                clearMinimumTime()
            范围
                setTimeRange(min_time, max_time)
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
