from PyQt5.Qt import *

class SB(QSpinBox):
    def textFromValue(self, p_int):
        print("xx2", p_int)
        # 1 * 1
        return str(p_int) + "*" + str(p_int)

    """
    自定义展示格式
        重写
            textFromValue(self, p_int) -> format_str
    
    应用场景
        此方法现在获取文本框中的数值，然后按自定义的格式输出用户需要展示的效果
        展示数值之前, 调用此方法, 转换成对应的格式字符串进行展示
    """

    def valueFromText(self, p_str):
        print("xxxx", p_str)

    """
    构造函数
    QSpinBox(parent: QWidget = None)
    默认功能:
        调整0到99范围之间的整数
            步长调节器
            修改文本框内容
    """

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSpinBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sb = SB(self)
        self.sb = sb
        sb.resize(100, 25)
        sb.move(100, 100)
        sb.valueChanged[str].connect(lambda val: print(type(val), val))

        """
        信号
            valueChanged(int i)
            valueChanged(QString text)  重载
        """

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(150, 150)
        btn.clicked.connect(lambda :sb.lineEdit().setText("30*30"))
        # btn.clicked.connect(lambda: self.设置以及获取数值())

        # self.最大值最小值()

    def 设置以及获取数值(self):
        # self.sb.setRange(0, 9)
        self.sb.setPrefix("撩课")
        # self.sb.setValue(66)
        print(self.sb.value())  # 仅仅获取数值
        print(self.sb.cleanText())   # 获取纯净的文本，不含前缀
        print(self.sb.Text())  # 获取文本包括前缀
        print(self.sb.lineEdit().text())    #获取文本包括前缀
        """
        设置和获取数值
            setValue(int)
            value() -> int
            cleanText() -> str
        应用场景
            设置以及获取数据
        """
        pass

    def 显示的进制设置(self):
        print(self.sb.displayIntegerBase())
        self.sb.setDisplayIntegerBase(2)
        print(self.sb.displayIntegerBase())
        """
        显示基数(进制)
            setDisplayIntegerBase(int)
                默认是10
            displayIntegerBase() -> int

        应用场景
            控制文本框内容的显示基数
            以几进制的形式进行展示
        """

    def 前缀和后缀(self):
        # self.sb.setRange(1, 12)
        # self.sb.setSuffix("月")
        self.sb.setRange(0, 6)
        self.sb.setPrefix("周")
        self.sb.setSpecialValueText("周日")
        """
        setSpecialValueText(str)    QAbstractSpinBox父类中的方法
            当数据到达最小值时, 会显示此字符串
            
        应用场景    设置特殊含义的数值字符串
        """
        pass

        """
        前缀和后缀
            setPrefix("周")
                设置前缀作为展示
            prefix() -> str
            
            setSuffix("月")
                设置后缀作为展示
            suffix() -> str
            
        应用场景
            特定场景下, 设置前缀或者后缀
            年月日, 星期
        """

    def 步长设置(self):
        self.sb.setSingleStep(3)

        """
        设置步长:
            setSingleStep(step_int)
            singleStep() -> int
        应用场景
            设置步长调节器, 单步步长值
        """

    def 数值循环(self):
        print(self.sb.wrapping())
        self.sb.setWrapping(True)
        print(self.sb.wrapping())

        """
        数值循环
            setWrapping(bool)
            wrapping() -> bool
        应用场景
            设置数值达到最大/小时, 跳转到最小/大
        """

    def 最大值最小值(self):
        # self.sb.setMaximum(180)
        # print(self.sb.maximum())
        #
        # self.sb.setMinimum(18)
        # print(self.sb.minimum())
        self.sb.setRange(18, 180)

        """
        设置数值范围:
            setMaximum(max_num)
                设置最大值
            maximum() -> int
            
            setMinimum(min_num)
                设置最小值
            minimum() -> int
            
            setRange(min_num, max_num)
                设置数值区间 [] 闭区间
        """

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())