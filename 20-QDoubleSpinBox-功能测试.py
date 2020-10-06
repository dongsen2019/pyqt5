from PyQt5.Qt import *

class MyDoubleSB(QDoubleSpinBox):
    def textFromValue(self, p_float):
        print("xxxxx", p_float)
        return str(p_float) + "*" + str(p_float)

    """
    自定义展示格式
        重写
            textFromValue(self, p_int) -> format_str
    应用场景
        展示数值之前, 调用此方法, 转换成对应的格式字符串进行展示
    """

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QDoubleSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    """
    构造函数    QDoubleSpinBox(parent: QWidget = None)
    默认功能
        步长为1.0, 调整0.00到99.99范围之间的浮点数    
            步长调节
            修改文本框内容
    """

    def setup_ui(self):

        dsb = MyDoubleSB(self)
        dsb.move(100, 100)
        dsb.resize(100, 30)
        # 0.00 - 99.99
        # dsb.setMaximum(88.88)
        # dsb.setMinimum(22.22)
        """
        setMaximum(max_num)
            设置最大值
            maximum() -> float
        setMinimum(min_num)
            设置最小值
            minimum() -> float
        setRange(min_num, max_num)
            设置数值区间
        """
        # dsb.setSingleStep(0.02)
        """
        设置步长调节器, 单步步长值
            setSingleStep(step_float)
            singleStep() -> float
        """
        # dsb.setWrapping(True)
        """
        数值循环
            设置数值达到最大/小时, 跳转到最小/大
                setWrapping(bool)
                wrapping() -> bool
        """
        dsb.setPrefix("$")
        dsb.setSuffix("%")
        """
        特定场景下, 设置前缀或者后缀
            setPrefix("$")
                设置前缀作为展示
            prefix() -> str
            
            setSuffix("%")
                设置后缀作为展示
            suffix() -> str
        """
        # dsb.setRange(1.0, 2.0)
        # dsb.setSingleStep(0.5)
        # dsb.setSuffix("倍速")
        # dsb.setSpecialValueText("正常")
        """
        setSpecialValueText(str)    父类中的方法
            当数据到达最小值时, 会显示此字符串
        
        应用场景
            设置特殊含义的数值字符串:
                1.0     正常
                1.5
                2.0
        """
        # dsb.setWrapping(True)

        # dsb.setDecimals(1)

        """
        设置小数位数:
            setDecimals(int)
            decimals() -> int
        """

        test_btn = QPushButton(self)
        test_btn.move(300, 300)
        test_btn.setText("测试按钮")
        # test_btn.clicked.connect(lambda :dsb.setValue(-166.66))
        # test_btn.clicked.connect(lambda :print(type(dsb.value()), dsb.value()))
        # test_btn.clicked.connect(lambda :print(type(dsb.cleanText()), dsb.cleanText()))
        # test_btn.clicked.connect(lambda :print(type(dsb.text()), dsb.text()))
        test_btn.clicked.connect(lambda :print(type(dsb.lineEdit().text()), dsb.lineEdit().text()))

        """
        setValue(float)
            如果设置的小数位数过多, 则会按照真实位数四舍五入
        value() -> float
            真实的数值
        cleanText() -> str
            纯净的文本，不包括任何前缀，后缀或前导或尾随空格，与value的区别是它的类型是str
        """

        # dsb.valueChanged.connect(lambda val: print(val, type(val)))
        dsb.valueChanged[str].connect(lambda val: print(val, type(val)))

        """
        信号:
        valueChanged(float)
        valueChanged(QString text)      重载
        """

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())