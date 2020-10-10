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

        """
        设置展示的section格式
            setDisplayFormat(format_str)    设置日期时间显示格式
            displayFormat() -> str          获取日期时间显示格式
           
        时间日期格式符如下：
                 
        日期
            d       没有前导零的数字的日期（1到31）
            dd      有前导零的数字的日期（01到31）
            ddd     缩写的本地化日期名称（例如'Mon'到'Sun'
            dddd    完整本地化的日期名称（例如“星期一”到“星期日”）
            M       没有前导零的数字的月份（1-12）
            MM      月份为前导零的数字（01-12）
            MMM     缩写的本地化月份名称（例如'Jan'到'Dec'）
            MMMM    完整的本地化月份名称（例如“1月”到“12月”）
            yy      年份为两位数字（00-99）
            yyyy    年份为四位数字
        
        时间
            h       没有前导零的小时（如果显示AM / PM，则为0到23或1到12）
            hh      前导零的小时（如果AM / PM显示，则为00到23或01到12）
            H       没有前导零的小时（0到23，即使有AM / PM显示）
            HH      前导零的小时（00到23，即使有AM / PM显示）
            m       没有前导零的分钟（0到59）
            mm      前导零（00到59）的分钟
            s       整个秒没有前导零（0到59）
            ss      带有前导零（00到59）
            z       第二个小数部分, 没有尾随零的毫秒（0到999）
            zzz     第二个小数部分, 有尾随零的毫秒（000到999）
            AP / A  使用AM / PM显示
            ap / a  使用am / pm显示
            t       时区
        """

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
            """
            控制section部分
                sectionCount() -> int   获取section个数
                setCurrentSectionIndex(int)     设置当前的section索引
                currentSectionIndex() -> int    获取section索引
                setCurrentSection(QDateTimeEdit.Section)    设置当前操作的日期时间section
                currentSection() -> QDateTimeEdit.Section   获取当前的section部分
                sectionAt(index_int) -> QDateTimeEdit.Section   获取指定索引位置的section
                sectionText(QDateTimeEdit.Section) -> str       获取指定section的文本内容
                00-01-01 $ 0: 01: 000
        索引号:  0  1  2   3   4   5

            QDateTimeEdit.Section
                QDateTimeEdit.NoSection
                QDateTimeEdit.AmPmSection
                QDateTimeEdit.MSecSection
                QDateTimeEdit.SecondSection
                QDateTimeEdit.MinuteSection
                QDateTimeEdit.HourSection
                QDateTimeEdit.DaySection
                QDateTimeEdit.MonthSection
                QDateTimeEdit.YearSection
            """
            # dte.setMaximumDateTime(QDateTime(2020, 8, 15, 12, 30))
            #
            # dte.setMinimumDateTime(QDateTime.currentDateTime())

            # dte.setDateTimeRange(QDateTime.currentDateTime().addDays(-3), QDateTime.currentDateTime().addDays(3))
            # print(dte.dateTime())
            print(dte.date())
            print(dte.time())

            """
            最小和最大日期时间：
            
                日期时间
                    最大
                        setMaximumDateTime(QDateTime)   默认  9999年12月31日 23:59:59 999毫秒
                        maximumDateTime() -> QDateTime
                        clearMaximumDateTime()
                    最小
                        setMinimumDateTime(QDateTime)
                        minimumDateTime() -> QDateTime
                        clearMinimumDateTime()
                    范围
                        setDateTimeRange(min_datetime, max_datetime)
                
                日期
                    最大
                        setMaximumDate(QDate)   设置最大日期      默认包含9999年12月31日
                        maximumDate() -> QDate  获取最大日期
                        clearMaximumDate()      清除自定义最大日期, 恢复默认
                    最小
                        setMinimumDate(QDate)   设置最小日期  默认1752年9月14日
                        minimumDate() -> QDate  获取最小日期
                        clearMinimumDate()      清除自定义最小日期, 恢复默认
                    范围  
                        setDateRange(min_date, max_date)
                
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

        btn.clicked.connect(test)
        print(dte.sectionCount())
        dte.setCalendarPopup(True)
        """
        通过日历选择控件, 快速的让用户输入日期
            是否弹出日历选择控件
                setCalendarPopup(bool)
                calendarPopup()
            
            自定义日历选择控件
                setCalendarWidget(QCalendarWidget)
                calendarWidget() -> QCalendarWidget
        """

        print(dte.dateTime())

        """
        QDateTime获取用户所输入的日期时间
            dateTime() -> QDateTime
            date() -> QDate
            time() -> QTime
        
        QDate获取时间    
            day()           这一个月的第几日
            month()         第几月
            year()          第几年
            dayOfWeek()     这一周 第几日
            dayOfYear()     这一年 第几日
            daysInMonth()   这一月总共多少天
            daysInYear()    这一年总共多少天
        
        QTime获取时间
            hour()
            minute()
            second() 
            msec()
        """

        dte.dateTimeChanged.connect(lambda val: print(val))
        dte.dateChanged.connect(lambda val: print("日期发生改变", val))
        dte.timeChanged.connect(lambda val: print("时间发生改变", val))

        """
        信号
            dateTimeChanged(QDateTime datetime)
            dateChanged(QDate date)
            timeChanged(QTime time)
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
