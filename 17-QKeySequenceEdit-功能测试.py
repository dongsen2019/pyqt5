from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QKeySequenceEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        kse = QKeySequenceEdit(self)
        # ks = QKeySequence("Ctrl+C")
        # ks = QKeySequence(QKeySequence.Copy)
        ks = QKeySequence(Qt.CTRL + Qt.Key_C, Qt.CTRL + Qt.Key_A)
        kse.setKeySequence(ks)
        kse.clear()
        "清除     clear()"

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        btn.clicked.connect(lambda: print(kse.keySequence().toString(), kse.keySequence().count()))
        "转换成可读字符串   toString() -> str       键位个数    count()"

        kse.editingFinished.connect(lambda: print("结束编辑"))
        kse.keySequenceChanged.connect(lambda key_val: print("键位序列发生改变", key_val.toString()))

        """
        信号      
        editingFinished()   结束编辑时发射     
        keySequenceChanged(QKeySequence  keySequence)   键位序列改变时发射
        keySequenceChanged(self, Union[QKeySequence, QKeySequence.StandardKey, str, int]) [signal]
        """

        """
        QKeySequenceEdit 描述:
            控件允许输入QKeySequence, 它通常用作快捷方式。
            当控件收到焦点时开始录制，并在用户释放最后一个关键字后一秒钟结束录制
            
        设置快捷键
            setKeySequence(QKeySequence keySequence)
            keySequence() -> QKeySequence
            
        构造函数
            QKeySequence(key_str)
                字符串     "Ctrl+S"
                
            QKeySequence(QKeySequence.StandardKey key)
                
                标准键位序列(QKeySequence.)
                    HelpContents	F1
                    WhatsThis	Shift+F1
                    Open	Ctrl+O
                    Close	Ctrl+F4, Ctrl+W
                    Save	Ctrl+S
                    Quit		Ctrl+Q
                    SaveAs		Ctrl+Shift+S
                    New	Ctrl+N
                    Delete	Del
                    Cut	Ctrl+X, Shift+Del	
                    Copy	Ctrl+C, Ctrl+Ins
                    Paste	Ctrl+V, Shift+Ins
                    Preferences		Ctrl+,
                    Undo	Ctrl+Z, Alt+Backspace
                    Redo	Ctrl+Y, Shift+Ctrl+Z, Alt+Shift+Backspace
                    Back	Alt+Left, Backspace
                    Forward	Alt+Right, Shift+Backspace
                    Refresh	             F5	
                    ZoomIn	Ctrl+Plus
                    ZoomOut	Ctrl+Minus
                    FullScreen	F11, Alt+Enter
                    Print	Ctrl+P
                    AddTab	Ctrl+T
                    NextChild	Ctrl+Tab, Forward, Ctrl+F6
                    PreviousChild	Ctrl+Shift+Tab, Back, Ctrl+Shift+F6
                    Find	Ctrl+F
                    FindNext	F3, Ctrl+G
                    FindPrevious	Shift+F3, Ctrl+Shift+G
                    Replace	Ctrl+H
                    SelectAll	Ctrl+A
                    Deselect	Ctrl+Shift+A
                    Bold	Ctrl+B
                    Italic	Ctrl+I
                    Underline	Ctrl+U
                    MoveToNextChar	Right
                    MoveToPreviousChar	Left
                    MoveToNextWord	Ctrl+Right
                    MoveToPreviousWord	Ctrl+Left
                    MoveToNextLine	Down
                    MoveToPreviousLine	Up
                    MoveToNextPage	PgDown
                    MoveToPreviousPage	PgUp
                    MoveToStartOfLine	Home
                    MoveToEndOfLine	End
                    MoveToStartOfDocument	Ctrl+Home
                    MoveToEndOfDocument	Ctrl+End
                    SelectNextChar	Shift+Right
                    SelectPreviousChar	Shift+Left
                    SelectNextWord	Ctrl+Shift+Right
                    SelectPreviousWord	Ctrl+Shift+Left
                    SelectNextLine	Shift+Down
                    SelectPreviousLine	Shift+Up
                    SelectNextPage	Shift+PgDown
                    SelectPreviousPage	Shift+PgUp
                    SelectStartOfLine	Shift+Home
                    SelectEndOfLine	Shift+End
                    SelectStartOfDocument	Ctrl+Shift+Home
                    SelectEndOfDocument	Ctrl+Shift+End
                    DeleteStartOfWord	Ctrl+Backspace
                    DeleteEndOfWord	Ctrl+Del
                    InsertParagraphSeparator	Enter
                    InsertLineSeparator	Shift+Enter
                    Cancel	Escape     
                       
            QKeySequence(int k1, int k2 = 0, int k3 = 0, int k4 = 0)    多个快捷键的组合（也可以单个）
                
                枚举值     Qt.Ctrl + Qt.Key_S
                      
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

