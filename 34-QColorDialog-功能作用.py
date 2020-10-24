from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QColorDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # self.setStyleSheet("background-color: rgb(100, 200, 150);")
        "利用底层的父控件的方法设置控件的背景色"
        # QColorDialog.setCustomColor(3, QColor(100, 200, 50))
        # QColorDialog.setStandardColor(2, QColor(255, 0, 0))
        # cd = QColorDialog(QColor(100, 200, 150), self)
        """
        静态方法
            customCount() -> int        颜色对话框自定义颜色的个数
            setCustomColor(int index, QColor color)     设置某个自定义索引位置的颜色
            customColor(int index) -> QColor        返回某个自定义索引位置的颜色
            setStandardColor(int index, QColor color)   设置某个标准索引位置的颜色
            standardColor(int index) -> QColor      返回某个标准索引位置的颜色
            getColor(initial: Union[QColor, Qt.GlobalColor, QGradient] = Qt.white, 
                     parent: QWidget = None, title: str = '', 
                     options: Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption] = QColorDialog.ColorDialogOptions())
                     -> QColor
            
            initial：初始化颜色
            parent：父对象
            title：对话框标题
        """
        # cd.setWindowTitle("选择一个好看的颜色")
        """
        构造函数
            QColorDialog(parent: QWidget = None)
            QColorDialog(Union[QColor, Qt.GlobalColor, QGradient], parent: QWidget = None)
        """
        # def color():
        #
        #     print(cd.customCount())
        #     cd.setCustomColor(0, QColor(200, 100, 20))
        #     return None
        #     palette = QPalette()
        "设置调色盘"
        #     # palette.setColor(QPalette.Background, cd.selectedColor())
        #     palette.setColor(QPalette.Background, cd.currentColor())
        "设置颜色用作背景，颜色设置为选择的颜色，cd.currentColor()为当前的颜色，cd.selectedColor()为选择的颜色"
        #     self.setPalette(palette)
        "将控件的背景色设置为调色盘的颜色"
        # cd.colorSelected.connect(color)
        "选择颜色按下确定后，自动触发该信号"

        # cd.currentColorChanged.connect(color)
        # cd.setOptions(QColorDialog.NoButtons | QColorDialog.ShowAlphaChannel)
        """
        setOption(self, QColorDialog.ColorDialogOption, on: bool = True)    bool值用于控制某个控制选项是否生效
        setOptions(self, Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption])
        testOption(self, QColorDialog_ColorDialogOption)
        
        QColorDialog.ColorDialogOption
            QColorDialog.ShowAlphaChannel   允许用户选择颜色的alpha(透明度)分量。
            QColorDialog.NoButtons          不显示“ 确定”和“ 取消”按钮。（对“实时对话框”有用。）
            QColorDialog.DontUseNativeDialog    使用Qt的标准颜色对话框而不是操作系统原生颜色对话框。
        """
        # cd.show()

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")

        def test():
            cd = QColorDialog(self)
            cd.setOption(QColorDialog.NoButtons)
            cd.setWindowTitle("选择一个人生的颜色")

            def sel_color(color):
                palette = QPalette()

                palette.setColor(QPalette.ButtonText, color)

                btn.setPalette(palette)
                pass
            # cd.colorSelected.connect(sel_color)
            cd.currentColorChanged.connect(sel_color)
            """
            信号
                colorSelected(QColor color)     被选中的颜色
                currentColorChanged(QColor color)   当前颜色变换
            """

            cd.show()
            """
            打开对话框
                open(self)
                open(PYQT_SLOT)     打开后, 会自动连接colorSelected信号与此处指定的槽函数
                exec() -> int
            """

            # color = QColorDialog.getColor(QColor(10, 20, 100), self, "选择颜色")
            """
            静态方法
                customCount() -> int        颜色对话框自定义颜色的个数
                setCustomColor(int index, QColor color)     设置某个自定义索引位置的颜色
                customColor(int index) -> QColor        返回某个自定义索引位置的颜色
                setStandardColor(int index, QColor color)   设置某个标准索引位置的颜色
                standardColor(int index) -> QColor      返回某个标准索引位置的颜色
                getColor(initial: Union[QColor, Qt.GlobalColor, QGradient] = Qt.white, 
                            parent: QWidget = None, title: str = '', 
                            options: Union[QColorDialog.ColorDialogOptions, QColorDialog.ColorDialogOption] = QColorDialog.ColorDialogOptions())
                            -> QColor

                initial：初始化颜色
                parent：父对象
                title：对话框标题
                options：控制选项
                返回  QColor ，前面可用一个变量接收
            """
            # palette = QPalette()
            # # palette.setColor(QPalette.Background, cd.selectedColor())
            # palette.setColor(QPalette.Background, color)
            # self.setPalette(palette)
            # print(color)
        btn.clicked.connect(test)

        # btn.clicked.connect(lambda :print(QColorDialog.customCount()))
        "打印自定义颜色的数量"

        # cd.open(color)
        "窗口级别触发的信号不会向color槽函数传递选择的颜色，可以用cd.selectedColor()获取选择的颜色"
        # if cd.exec():
        "如果返回1，则选择了确定，选择了颜色"
        #     color()
        "返回1则执行color函数"


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
