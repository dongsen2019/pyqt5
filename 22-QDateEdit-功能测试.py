from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        de = QDateEdit(self)

        """
        构造函数
            QDateEdit(QWidget *parent = nullptr)
            QDateEdit(const QDate &date, QWidget *parent = nullptr)
        """
        de.setDisplayFormat("yy-MMMM-dddd")

        """
        设置展示的section格式
            setDisplayFormat(format_str)
                设置日期时间显示格式
            displayFormat() -> str
                获取日期时间显示格式
        
        时间日期格式符 见 21-QDateTimeEdit-功能测试 
        """

        print(de.date())    # 获取日期  date() -> QDate

        """
        最大和最小日期
            最大
                setMaximumDate(QDate)   设置最大日期  默认包含9999年12月31日
                maximumDate() -> QDate  获取最大日期
                clearMaximumDate()      清除自定义最大日期, 恢复默认
            最小
                setMinimumDate(QDate)   设置最小日期  默认1752年9月14日
                minimumDate() -> QDate  获取最小日期
                clearMinimumDate()      清除自定义最小日期, 恢复默认
            范围
                setDateRange(min_date, max_date)
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()

    sys.exit(app.exec_())
