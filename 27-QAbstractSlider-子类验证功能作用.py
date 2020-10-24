from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QAbstractSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        label = QLabel(self)
        label.setText("0")
        label.move(200, 200)
        label.resize(100, 30)
        # print(QAbstractSlider.__subclasses__())
        sd = QSlider(self)
        sd.move(100, 100)
        # sd.valueChanged.connect(lambda val:label.setText(str(val)))
        sd.valueChanged.connect(lambda :label.setText(str(sd.value())))
        "value() -> int 获取滑块当前数值"

        # 设置最大值 最小值
        sd.setMaximum(100)
        sd.setMinimum(66)

        """
        数值范围
            setMaximum(int)     maximum() -> int
            setMinimum(int)     minimum() -> int
        """

        # 当前数值
        # sd.setValue(88)

        """
        当前数值    
            setValue(int)   value() -> int
        """

        # 步长设置
        # sd.setSingleStep(5)
        # sd.setPageStep(8)
        """
        步长
            setPageStep(int)    pageStep() -> int
            setSingleStep(int)  singleStep() -> int
        """

        # 跟踪设置
        # print(sd.hasTracking())
        # sd.setTracking(False)
        """
        是否追踪
            setTracking(bool enable)    hasTracking() -> bool
        理解为:
            value是否跟随着滑块的位置变化而变化, 默认值为True
            对valueChanged信号发射时机的影响
        """

        # 滑块位置的设置
        # sd.setSliderPosition(88)

        """
        滑块位置
            setSliderPosition(int)  sliderPosition() -> int
            滑块位置的设置 如果此时为非追踪，value不会跟随着滑块的位置变化而变化
        """

        # 倒立外观
        # sd.setInvertedAppearance(True)
        # sd.setInvertedControls(True)
        # sd.setOrientation(Qt.Horizontal)
        """
        倒立外观
            setInvertedAppearance(bool)
            invertedAppearance() -> bool
            大小头反过来
        """

        # sd.sliderMoved.connect(lambda val:print(val))
        """
        操作反转
            setInvertedControls(bool)
            invertedControls() -> bool
            上下键位反过来
        """

        "倒立外观和操作反转配合使用，可以使得滑块上减下加"

        sd.actionTriggered.connect(lambda val:print(val))
        sd.rangeChanged.connect(lambda min, max:print(min, max))

        """
        信号
        valueChanged()
        sliderPressed()
        sliderMoved(int value)
        sliderReleased()
        
        actionTriggered(int action)
            QAbstractSlider.SliderNoAction
            QAbstractSlider.SliderSingleStepAdd
            QAbstractSlider.SliderSingleStepSub
            QAbstractSlider.SliderPageStepAdd
            QAbstractSlider.SliderPageStepSub
            QAbstractSlider.SliderToMinimum
            QAbstractSlider.SliderToMaximum
            QAbstractSlider.SliderMove
            ____________________________________
            
            SliderMove = 7
            SliderNoAction = 0
            SliderOrientationChange = 1
            SliderPageStepAdd = 3
            SliderPageStepSub = 4
            SliderRangeChange = 0
            SliderSingleStepAdd = 1
            SliderSingleStepSub = 2
            SliderStepsChange = 2
            SliderToMaximum = 6
            SliderToMinimum = 5
            SliderValueChange = 3

        rangeChanged(int min，int max)
        """

        sd.setMaximum(99)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())