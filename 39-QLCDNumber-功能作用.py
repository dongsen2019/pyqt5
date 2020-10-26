from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLCDNumber的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # lcd = QLCDNumber(self)
        """
        构造函数
            QLCDNumber(parent: QWidget = None)
            QLCDNumber(int, parent: QWidget = None)     参数1代表展示的数值位数
        """

        lcd = QLCDNumber(self)
        lcd.move(0, 0)
        lcd.resize(300, 100)

        lcd.setDigitCount(2)
        """
        位数限制
            setDigitCount(int)
            digitCount() -> int
        """

    #     0 / O, 1, 2, 3, 4, 5 / S, 6, 7, 8, 9 / g
    #
    # A, B, C, D, E, F, h, H, L, o, P, r, u, U, Y
    # : ' 空格
    #     lcd.display(": '")    单引号是 度 °
    #     lcd.display(12)
        """
        设置显示数值
            display(str)        当位数超出限制，显示内容去除前面的位
            display(float)      四舍五入或0
            display(int)        四舍五入或0
            intValue() -> int   获取数据int
            value() -> float    获取数据float
        """

        # lcd.setMode(QLCDNumber.Hex)
        """
        模式设置
            setMode(self, QLCDNumber.Mode)
            mode(self) -> QLCDNumber.Mode
            QLCDNumber.Mode
                QLCDNumber.Hex      十六进制
                QLCDNumber.Dec      十进制
                QLCDNumber.Oct      八进制
                QLCDNumber.Bin      二进制
        快捷
            setHexMode（）
            setDecMode（）
            setOctMode（）
            setBinMode（）
        """

        print(lcd.checkOverflow(99))
        print(lcd.checkOverflow(100))
        lcd.overflow.connect(lambda :print("数值溢出"))
        "信号     overflow()      数据溢出时发射"

        """
        溢出
            checkOverflow(self, float) -> bool
            checkOverflow(self, int) -> bool
        """

        lcd.display(99)

        lcd2 = QLCDNumber(self)
        lcd2.move(0, 100)
        lcd2.resize(300, 100)

        lcd3 = QLCDNumber(self)
        lcd3.move(0, 200)
        lcd3.resize(300, 100)

        lcd2.display(99)
        lcd3.display(99)

        lcd.setSegmentStyle(QLCDNumber.Outline)
        lcd2.setSegmentStyle(QLCDNumber.Filled)
        lcd3.setSegmentStyle(QLCDNumber.Flat)
        """
        分段样式
            setSegmentStyle(self, QLCDNumber.SegmentStyle)
            
            segmentStyle(self) -> QLCDNumber.SegmentStyle
                QLCDNumber.Outline      生成填充了背景颜色的凸起部分
                QLCDNumber.Filled       默认值     生成填充前景色的凸起部分。
                QLCDNumber.Flat         生成填充前景色的平坦段。
        """

        # btn = QPushButton(self)
        # btn.setText("测试按钮")
        # btn.move(50, 50)
        # btn.clicked.connect(lambda :print(lcd.value()))
        # btn.clicked.connect(lambda :print(lcd.intValue()))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
