from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QInputDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):

        # result = QInputDialog.getInt(self, "xxx1", "xxx2", 888, step=8)
        # result = QInputDialog.getDouble(self, "xxx1", "xxx2", 888.88, decimals = 2)
        # result = QInputDialog.getText(self, "xx1", "xx2", echo=QLineEdit.Password)
        # result = QInputDialog.getMultiLineText(self, "xx1", "xx2", "default")
        # result = QInputDialog.getItem(self, "xx1", "xx2", ["1", "2", "3"], 2, True)
        # print(result)
        """
        常用的静态方法
            getInt(QWidget, str, str, value: int = 0, min: int = -2147483647, max: int = 2147483647, step: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[int, bool]
            getDouble(QWidget, str, str, value: float = 0, min: float = -2147483647, max: float = 2147483647, decimals: int = 1, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags()) -> Tuple[float, bool]
            getDouble(QWidget, str, str, float, float, float, int, Union[Qt.WindowFlags, Qt.WindowType], float) -> Tuple[float, bool]
            getText(QWidget, str, str, echo: QLineEdit.EchoMode = QLineEdit.Normal, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
            getMultiLineText(QWidget, str, str, text: str = '', flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
            getItem(QWidget, str, str, Iterable[str], current: int = 0, editable: bool = True, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags(), inputMethodHints: Union[Qt.InputMethodHints, Qt.InputMethodHint] = Qt.ImhNone) -> Tuple[str, bool]
        """

        input_d = QInputDialog(self, Qt.FramelessWindowHint)
        """
        构造函数
            QInputDialog(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
        
        windowFlags:
            顶层窗口外观标志
                Qt.MSWindowsFixedSizeDialogHint     窗口无法调整大小
                Qt.FramelessWindowHint              窗口无边框
                Qt.CustomizeWindowHint              有边框但无标题栏和按钮，不能移动和拖动
                Qt.WindowTitleHint                  添加标题栏和一个关闭按钮
                Qt.WindowSystemMenuHint             添加系统目录和一个关闭按钮
                Qt.WindowMaximizeButtonHint         激活最大化和关闭按钮，禁止最小化按钮
                Qt.WindowMinimizeButtonHint         激活最小化和关闭按钮，禁止最大化按钮
                Qt.WindowMinMaxButtonsHint          激活最小化，最大化和关闭按钮
                Qt.WindowCloseButtonHint            添加一个关闭按钮
                Qt.WindowContextHelpButtonHint      添加问号和关闭按钮，同对话框
                Qt.WindowStaysOnTopHint             窗口始终处于顶层位置
                Qt.WindowStaysOnBottomHint          窗口始终处于底层位置
        """

        # input_d.setOption(QInputDialog.UseListViewForComboBoxItems)
        """
        选项设置
            setOption(self, QInputDialog.InputDialogOption, on: bool = True)
            setOptions(self, Union[QInputDialog.InputDialogOptions, QInputDialog.InputDialogOption])
            testOption(self, QInputDialog.InputDialogOption) -> bool
            options(self) -> QInputDialog.InputDialogOptions
            
            补充
                QInputDialog.InputDialogOption:
                    QInputDialog.NoButtons                      不显示“ 确定”和“ 取消”按钮（对“实时对话框”有用）。
                    QInputDialog.UseListViewForComboBoxItems    使用QListView而不是不可编辑的QComboBox来显示使用setComboBoxItems（）设置的项目。
                                                                只有当条目是多个的时候才能看出该设置项的作用！
                    QInputDialog.UsePlainTextEditForTextInput   使用QPlainTextEdit进行多行文本输入。该值在5.2中引入。
        """

        # input_d.setLabelText("请输入你的姓名")
        # input_d.setOkButtonText("好的")
        # input_d.setCancelButtonText("我想取消")
        """
        界面文本设置
            setLabelText(str)       labelText(self) -> str
            setOkButtonText(str)
            setCancelButtonText(str)
        """

        #
        input_d.setInputMode(QInputDialog.TextInput)
        """
        输入模式
            inputMode(self) -> QInputDialog.InputMode
            setInputMode(self, QInputDialog.InputMode)
            QInputDialog.InputMode:
                QInputDialog.TextInput
                QInputDialog.IntInput
                QInputDialog.DoubleInput
        """
        # input_d.setDoubleRange(9.9, 19.9)
        # input_d.setDoubleStep(2)
        # input_d.setDoubleDecimals(3)
        """
        各个小分类设置
            整型  setIntMaximum(self, int)    intMaximum(self) -> int
                  setIntMinimum(self, int)    intMinimum(self) -> int
                  setIntRange(self, int, int)
                  setIntStep(self, int)       intStep(self) -> int
                  setIntValue(self, int)      intValue(self) -> int
            浮点型
                  setDoubleMaximum(self, float)     doubleMaximum() -> float
                  setDoubleDecimals(self, int)      doubleDecimals() -> int
                  setDoubleMinimum(self, float)     doubleMinimum(self) -> float
                  setDoubleRange(self, float, float) 
                  setDoubleStep(self, float)        doubleStep(self) -> float
                  setDoubleValue(self, float)       doubleValue(self) -> float
            字符串
                  setTextEchoMode(self, QLineEdit.EchoMode)     textEchoMode(self) -> QLineEdit.EchoMode
                  setTextValue(self, str)                       textValue(self) -> str
            下拉列表
                  setComboBoxItems(self, Iterable[str])         comboBoxItems(self) -> List[str]
                  setComboBoxEditable(self, bool)               isComboBoxEditable(self) -> bool
        """

        #
        input_d.setComboBoxItems(["abc", "def", "ccc"])
        # input_d.setComboBoxEditable(True)

        # input_d.intValueChanged.connect(lambda val:print("整型数据发生改变", val))
        # input_d.intValueSelected.connect(lambda val:print("整型数据最终被选中", val))

        # input_d.doubleValueChanged.connect(lambda val:print("浮点型数据发生改变", val))
        # input_d.doubleValueSelected.connect(lambda val:print("浮点型数据最终被选中", val))

        input_d.textValueChanged.connect(lambda val: print("字符串型数据发生改变", val))
        input_d.textValueSelected.connect(lambda val: print("字符串型数据最终被选中", val))
        """
        信号
            intValueChanged(int value)
            intValueSelected(int value)
            doubleValueChanged(double value)
            doubleValueSelected(double value)
            textValueChanged(text_str)
            textValueSelected(text_str)
        """


        input_d.show()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

