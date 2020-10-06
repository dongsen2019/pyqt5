from PyQt5.Qt import *
import time

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDateTimeEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        dte = QDateTimeEdit(self)
        # dte = QDateTimeEdit(QDateTime.currentDateTime(), self)
        # dte = QDateTimeEdit(QDate.currentDate(), self)
        # dte = QDateTimeEdit(QTime.currentTime(), self)
        dte.move(100, 100)

        """
        QDateTimeEdit   构造函数
        
        应用场景：
            根据指定日期或时间, 创建出日期时间编辑器控件
            并会初始化该控件展示的section
        
        QDateTimeEdit(parent: QWidget = None)
        QDateTimeEdit(Union[QDateTime, datetime.datetime], parent: QWidget = None)
        QDateTimeEdit(Union[QDate, datetime.date], parent: QWidget = None)
        QDateTimeEdit(Union[QTime, datetime.time], parent: QWidget = None)
        """

        dte.setDisplayFormat("yy-MM-dd $ m: ss: zzz")

        btn = QPushButton(self)
        btn.move(200, 200)
        btn.setText("测试")
        # btn.clicked.connect(lambda :print(dte.currentSectionIndex()))
        def test():
            # print("xxx")
            # dte.setFocus()
            # dte.setCurrentSectionIndex(3)
            # dte.setCurrentSection(QDateTimeEdit.DaySection)
            # print(dte.sectionText(QDateTimeEdit.DaySection))
            # dte.setMaximumDateTime(QDateTime(2020, 8, 15, 12, 30))
            #
            # dte.setMinimumDateTime(QDateTime.currentDateTime())

            # dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3), QDateTime.currentDateTime().addDays(3))
            # print(dte.dateTime())
            print(dte.date())
            print(dte.time())

        btn.clicked.connect(test)
        print(dte.sectionCount())
        dte.setCalendarPopup(True)

        dte.dateTimeChanged.connect(lambda val:print(val))
        dte.dateChanged.connect(lambda val: print("日期发生改变", val))
        dte.timeChanged.connect(lambda val: print("时间发生改变", val))



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())