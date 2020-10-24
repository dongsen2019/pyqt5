from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QSlider的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        sd = QSlider(self)
        sd.move(200, 200)
        sd.resize(30, 200)
        sd.setTickPosition(QSlider.TicksBothSides)
        print(sd.tickInterval())
        # sd.setPageStep(5)
        sd.setTickInterval(5)

        """
        控制滑块刻度位置以及刻度密度
            setTickPosition(self, QSlider.TickPosition)
                QSlider.NoTicks 0       不要画任何刻度线。
                QSlider.TicksBothSides  3   在凹槽两侧画刻度线。
                QSlider.TicksAbove  1   在（水平）滑块上方绘制刻度线
                QSlider.TicksBelow  2   在（水平）滑块下方绘制刻度线
                QSlider.TicksLeft   1   在（垂直）滑块的左侧绘制刻度线
                QSlider.TicksRight  2   在（垂直）滑块右侧绘制刻度线
                
            sd.tickPosition() -> QSlider.TickPosition
            
            sd.setTickInterval(int)
                这是值间隔，而不是像素间隔。如果为0，滑块将在singleStep和pageStep之间进行选择
            sd.tickInterval() -> int
        
        """

        sd.valueChanged.connect(lambda val: print(val))


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    
    window = Window()
    window.show()

    sys.exit(app.exec_())
