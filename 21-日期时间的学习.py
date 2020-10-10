from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("日期时间的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # dt = QDateTime(2018, 12, 12, 12, 30)
        # dt = QDateTime.currentDateTime()
        # # dt = dt.addYears(-2)
        # print(dt.offsetFromUtc() // 3600)
        # # print(dt)
        #
        # QDateTimeEdit(dt, self)
        # QDate
        # QTime
        time = QTime.currentTime()
        time.start()

        btn = QPushButton(self)
        btn.setText("测试")
        btn.move(200, 200)
        btn.clicked.connect(lambda :print(time.elapsed() / 1000))

        """
        QDateTime日期时间对象构造
        
            QDateTime()
            QDateTime(QDateTime)
            QDateTime(QDate)
            QDateTime(QDate,  QTime, Qt.TimeSpec = Qt.LocalTime)
            推荐：QDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)
            QDateTime(QDate, QTime, Qt.TimeSpec, int)
            QDateTime(QDate, QTime, QTimeZone)
            
            静态方法:
            currentDateTime()
                当前时间
            currentDateTimeUtc()
                世界标准时间
        
        调整日期时间
            addYears(int)
            addMonths(int)
            addDays(int)
            addSecs(int)
            addMSecs(int)
            setDate(const QDate &date)
            setTime(const QTime &time)
        
        计算时间差
            offsetFromUtc()
            secsTo(QDateTime)
            msecsTo(QDateTime)
        """

        """
        QDate日期对象的构造
        
            QDate()
            QDate(int y, int m, int d)
            currentDate()
        调整日期
            setDate(int year, int month, int day)
            addYears(int nyears)
            addMonths(int nmonths)
            addDays(qint64 ndays)
        计算时间差
            daysTo(const QDate &d)
        获取时间
            day()       这一个月的第几日
            month()     第几月
            year()      第几年
            dayOfWeek()     这一周 第几日
            dayOfYear()     这一年 第几日
            daysInMonth()   这一月总共多少天
            daysInYear()    这一年总共多少天
        """

        """
        QTime时间对象构造
            QTime()
            QTime(int h, int m, int s = 0, int ms = 0)
            currentTime()
        调整时间
            addSecs(int s)
            addMSecs(int ms)
        计算时间差
            secsTo(QTime t) 
        计时
            start()
            restart()
            elapsed()   以上两个方法启动后, 至此方法调用时, 经历的毫秒数
        获取时间
            hour()
            minute()
            second() 
            msec()
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())