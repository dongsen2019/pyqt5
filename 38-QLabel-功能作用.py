from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLabel的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # label = QLabel("社会我顺哥, 人狠话不多", self)
        """
        构造函数
            QLabel(parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
            QLabel(str, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.WindowFlags())
        """

        # label = QLabel("账号(&s):", self)
        # label = QLabel("<a href='http://www.itlike.com'>撩课</a>", self)
        # label = QLabel("123 456 789 " * 6, self)
        label = QLabel("\n".join("123456789"), self)
        label.setStyleSheet("background-color: cyan;")
        label.move(50, 100)
        label.resize(400, 300)
        # label.adjustSize()

        # label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        label.setAlignment(Qt.AlignRight)
        """
        对齐
            alignment() -> Qt.Alignment
            setAlignment(Qt.Alignment)
        """

        # label.setIndent(20)
        """
            缩进和边距
                setIndent(int)      indent() -> int     默认为左侧缩进，当右对齐时为右侧缩进
                setMargin(int)      margin() -> int
        """

        label.setMargin(20)
        "设置上下左右边距"

        # label.setTextFormat(Qt.PlainText)
        """
        文本格式
            setTextFormat(Qt.TextFormat)
            textFormat() ---> Qt.TextFormat
        Qt.TextFormat
            Qt.PlainText    文本字符串被解释为纯文本字符串。
            Qt.RichText     文本字符串被解释为富文本字符串。有关富文本的定义，请参阅支持的HTML子集。
            Qt.AutoText     自动识别是否是富文本
        """

        le1 = QLineEdit(self)
        le1.move(250, 250)

        le2 = QLineEdit(self)
        le2.move(250, 300)

        label.setBuddy(le1)
        """
        小伙伴
            buddy() -> QWidget
            setBuddy(QWidget buddy)     在标签名称中使用&+按键
            Alt + 快捷键     会作用在小伙伴身上
        """

        # label.setPixmap(QPixmap("code.png"))
        # label.adjustSize()
        label.setScaledContents(True)
        """
        内容缩放
            hasScaledContents() -> bool
            setScaledContents(bool)
            缩放内容, 适应控件大小    针对于图片有效
            根据控件的尺寸类型缩放控件中的内容
        """

        # label.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextSelectableByKeyboard | Qt.TextEditable)
        """
        文本交互标志
            setTextInteractionFlags(Qt.TextInteractionFlags flags)
            textInteractionFlags() -> Qt.TextInteractionFlags
        
        补充
            Qt.TextInteractionFlag
                Qt.NoTextInteraction            不可能与文本进行交互。
                Qt.TextSelectableByMouse        可以使用鼠标选择文本并使用上下文菜单或标准键盘快捷键将其复制到剪贴板。
                Qt.TextSelectableByKeyboard     可以使用键盘上的光标键选择文本。显示文本光标。
                Qt.LinksAccessibleByMouse       可以使用鼠标突出显示和激活链接。
                Qt.LinksAccessibleByKeyboard    可以使用选项卡聚焦链接并使用enter激活。
                Qt.TextEditable                 该文字完全可编辑。
                Qt.TextEditorInteraction        文本编辑器的默认值。      等价于  TextSelectableByMouse | TextSelectableByKeyboard | TextEditable
                Qt.TextBrowserInteraction       QTextBrowser的默认值。   等价于  TextSelectableByMouse | LinksAccessibleByMouse | LinksAccessibleByKeyboard
        """

        # label.setOpenExternalLinks(True)
        """
        外部链接
            openExternalLinks() -> bool
            setOpenExternalLinks(bool open)
        """

        label.setWordWrap(True)
        """
        单词换行
            setWordWrap(bool on)
            wordWrap() -> bool
        """

        label.setSelection(1, 2)
        """
        选中文本
            setSelection(int start, int length)
            hasSelectedText() -> bool
            selectedText() -> str
            selectionStart() -> int
        """

        # label.setText("<img src='code.png' width=60 height=60>")
        """
        文本字符串
            text() -> str
            setText(QString)
        """
        # label.setNum(888.88)
        """
        数值数据
            setNum(int num)
            setNum(double num)
        """

        # pic = QPicture()
        # painter = QPainter(pic)
        # painter.setBrush(QBrush(QColor(100, 200, 100)))
        # painter.drawEllipse(0, 0, 200, 200)
        "用画家在图片上画图"
        #
        # label.setPicture(pic)
        """
        图形图像
            setPicture(QPicture)
                picture() -> QPicture 
            setPixmap(QPixmap)
                pixmap() -> QPixmap 
        """

        # movie = QMovie("shulan.gif")
        # label.setMovie(movie)
        #
        # movie.start()
        # movie.setSpeed(1000)
        """
        动图
            setMovie(QMovie movie)      
            
            movie() -> QMovie       此类用于显示没有声音的简单动画
            常用操作
                setScaledSize(QSize)
                setPaused(bool) -> void
                setSpeed(int percentSpeed)      setSpeed(200) 200%  两倍速
                start()
                stop()
        """

        #
        # label.clear()
        "清空     clear()"

        label.setText("社会我顺哥<a href='http://www.itlike.com'>撩课</a>人狠话不多")

        # label.linkHovered.connect(lambda a: print(a))
        label.linkActivated.connect(lambda a: print(a))

        """
        信号
            linkActivated(link_str)
            linkHovered(link_str)
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())

