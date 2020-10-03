from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QPlainTextEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        pte = QPlainTextEdit(self)
        # pte = QTextEdit(self)
        self.pte = pte
        pte.resize(300, 300)
        pte.move(100, 100)

        test_btn = QPushButton(self)
        test_btn.move(20, 20)
        test_btn.setText("测试按钮")
        test_btn.clicked.connect(self.btn_test)

        # 展示行号
        line_num_parent = QWidget(self)
        line_num_parent.resize(30, 300)
        line_num_parent.move(70, 100)
        line_num_parent.setStyleSheet("background-color: cyan;")

        self.line_label = QLabel(line_num_parent)
        self.line_label.move(0, 6)

        # 1 - 100
        line_nums = "\n".join([str(i) for i in range(1, 101)])
        self.line_label.setText(line_nums)
        self.line_label.adjustSize()

        # self.占位提示文本()
        # self.只读设置()
        # self.格式设置()
        # self.自动换行()
        # self.覆盖模式()
        # self.Tab控制()
        # self.文本操作()
        # self.pte.setCenterOnScroll(True)


    def btn_test(self):
        # self.块的操作()
        # self.放大缩小()
        # self.光标操作()
        print(self.pte.cursorRect())
        self.信号的操作()

        # tc = QTextCursor(self.pte.document())
        # tc.setPosition(6)
        # tc.insertHtml("xxxxxx")




    def 信号的操作(self):
        # self.pte.textChanged.connect(lambda :print("内容发生了改变"))
        # self.pte.cursorPositionChanged.connect(lambda :print("光标位置改变"))
        # self.pte.blockCountChanged.connect(lambda bc:print("块的个数改变", bc))
        # self.pte.selectionChanged.connect(lambda :print("选中内容发生了改变", self.pte.textCursor().selectedText()))
        # self.pte.modificationChanged.connect(lambda val:print("修改状态发生改变", val))
        # doc = self.pte.document()
        # doc.setModified(False)
        # self.pte.updateRequest.connect(lambda rect, dy: self.line_label.move(self.line_label.x(), self.line_label.y() + dy))

        self.pte.updateRequest.connect(lambda rect, dy: print(rect, dy))

        """
        184 信号:
            textChanged()
                文本改变时
            selectionChanged()
                选中内容改变时
            modificationChanged(bool)   当编辑状态为改变时，界面一般带*，当保存后，可以通过 setmodified 设置为未改变
                编辑状态改变时
            cursorPositionChanged()
                光标位置改变时
            blockCountChanged(int)
                块的个数发生改变时
            updateRequest(QRect rect, int dy)
                内容更新请求时
            copyAvailable(bool)
                复制可用时
            redoAvailable(bool)
                重做可用时
            undoAvailable(bool)
                撤销可用时
        """

    def 光标操作(self):
        QTextCursor
        # tc = self.pte.textCursor()
        # tc.insertImage("rose.png")
        # tc.insertTable(5, 6)
        # tc = self.pte.cursorForPosition(QPoint(20, 60))
        # print(tc)
        # tc.insertText("itlike")
        # self.pte.setCursorWidth(20)

        self.pte.moveCursor(QTextCursor.End, QTextCursor.KeepAnchor)
        self.pte.setFocus()

        """
        183.
        textCursor() -> QTextCursor     获取文本光标对象
        cursorForPosition(QPoint) -> QTextCursor    获取指定位置的文本光标对象
        cursorWidth() -> int        获取文本光标宽度
        setCursorWidth(int)         设置文本光标宽度
        cursorRect() -> QRect       获取文本光标矩形
        cursorRect(QTextCursor)     获取指定光标对象的矩形
        
        
        moveCursor(QTextCursor.MoveOperation，QTextCursor.MoveMode)
            QTextCursor.MoveOperation：
                QTextCursor.NoMove
                    将光标保持在原位
                QTextCursor.Start
                    移至文档的开头。
                QTextCursor.StartOfLine
                    移动到当前行的开头。
                QTextCursor.StartOfBlock
                    移动到当前块的开头。
                QTextCursor.StartOfWord
                    移动到当前单词的开头。
                QTextCursor.PreviousBlock
                    移动到上一个块的开头。
                QTextCursor.PreviousCharacter
                    移至上一个字符。
                QTextCursor.PreviousWord
                    移到上一个单词的开头。
                QTextCursor.Up
                    向上移动一行。
                QTextCursor.Left
                    向左移动一个字符。
                QTextCursor.WordLeft
                    向左移动一个单词。
                QTextCursor.End
                    移到文档的末尾。
                QTextCursor.EndOfLine
                    移动到当前行的末尾。
                QTextCursor.EndOfWord
                    移到当前单词的末尾。
                QTextCursor.EndOfBlock
                    移动到当前块的末尾。
                QTextCursor.NextBlock
                    移动到下一个块的开头。
                QTextCursor.NextCharacter
                    移动到下一个角色。
                QTextCursor.NextWord
                    转到下一个单词。
                QTextCursor.Down
                    向下移动一行。
                QTextCursor.Right
                    向右移动一个角色。
                QTextCursor.WordRight
                    向右移动一个单词。
                QTextCursor.NextCell	
                    移动到当前表中下一个表格单元格的开头。如果当前单元格是行中的最后一个单元格，则光标将移动到下一行中的第一个单元格。
                QTextCursor.PreviousCell
                    移动到当前表内的上一个表格单元格的开头。如果当前单元格是行中的第一个单元格，则光标将移动到上一行中的最后一个单元格。
                QTextCursor.NextRow
                    移动到当前表中下一行的第一个新单元格。
                QTextCursor.PreviousRow
                    移动到当前表中上一行的最后一个单元格。
            QTextCursor.MoveMode：
                QTextCursor.MoveAnchor
                    将锚点移动到与光标本身相同的位置。
                QTextCursor.KeepAnchor
                    将锚固定在原处。
        """

        pass

    def 滚动保证光标可见(self):
        # self.pte.centerCursor()
        self.pte.ensureCursorVisible()
        self.pte.setFocus()

        """
        182.
        centerCursor()      控制光标, 尽可能保证光标在文本框中间
        
        ensureCursorVisible()   
            移动最短的位置，使光标可见
             
        setCenterOnScroll(bool)
            传递True  表示, 控制光标(包括尾部), 显示时能够展示在中间位置
            注意  必须事先设置好
            
        centerOnScroll() -> bool    滚动控件, 确保光标可见
        """

    def 放大缩小(self):
        # self.pte.zoomIn(10)
        # self.pte.zoomIn(-1)
        self.pte.zoomOut(-10)

        """
        181. 常用编辑操作:
            selectAll()
                选中所有
            copy()
                复制选中文本
            cut()
                剪切选中文本
            paste()
                粘贴文本
                canPaste() -> bool
                    判定是否可以粘贴
            clear()
                清空内容
            redo()
                重做
                isUndoRedoEnabled() -> bool
                    判定撤销重做是否可用
                setUndoRedoEnabled(bool)
                    设置撤销重做是否可用
            undo()
                撤销
            find(str, QTextDocument.FindFlags) -> bool
                QTextDocument.FindBackward
                    向后搜索而不是向前搜索。
                QTextDocument.FindCaseSensitively
                    默认情况下，查找工作区不区分大小写。
                    指定此选项会将行为更改为区分大小写的查找操作。
                QTextDocument.FindWholeWords
                    使查找匹配仅完整的单词。
            zoomIn(int range = 1)
                放大缩小
                    range > 0
                        放大
                    range < 0
                        缩小
            zoomOut(int range = 1)
                过期
                效果和上面的方法相反
        """

    def 块的操作(self):
        print(self.pte.blockCount())
        self.pte.setMaximumBlockCount(3)
        print(self.pte.toPlainText())
        """
        180. 块操作
            API
                blockCount() -> int
                    当前块个数
                maximumBlockCount() -> int
                    最大块个数
                setMaximumBlockCount(int)
                    设置最大块个数
            应用场景
                设置用户能够输入的最大块数
            案例
                测试以上API
        """

    def 文本操作(self):
        # self.pte.setPlainText("社会我顺哥, 人狠话不多")
        # self.pte.setPlainText("itlike.com")
        # self.pte.insertPlainText("itlike.com")
        # self.pte.appendPlainText("<a href='http://www.itlike.com'>撩课</a>")
        # self.pte.appendHtml("<a href='http://www.itlike.com'>撩课</a>")
        #
        # table_str = "<table border=2>" \
        #             "<tr><td>1</td><td>2</td><td>3</td></tr>" \
        #             "<tr><td>4</td><td>5</td><td>6</td></tr>" \
        #             "</table>"
        # # self.pte.setHtml(table_str)
        # self.pte.appendHtml(table_str)
        # print(self.pte.toPlainText())
        pass

        """
        179. 追加以及获取文本:
            setPlainText(text_str)
                设置普通文本内容
            insertPlainText(text_str)
                插入普通文本
            appendPlainText(text_str)
                追加普通文本
            appendHtml(html_str)
                追加HTML字符串
                注意
                    有些标签不支持
                        表格
                        列表
                        图片
                        ...
            toPlainText() -> 转换成纯文本
        """

    def Tab控制(self):
        self.pte.setTabChangesFocus(False)
        self.pte.setTabStopDistance(100)
        """
        178. Tab控制:
            setTabChangesFocus(bool)
            setTabStopDistance(distance_float)
            tabChangesFocus() -> bool
            tabStopDistance() -> float
        """

    def 覆盖模式(self):
        print(self.pte.overwriteMode())
        self.pte.setOverwriteMode(True)
        print(self.pte.overwriteMode())

        """
        178.覆盖模式：
            setOverwriteMode(bool)      设置是否为覆盖模式
            overwriteMode() -> bool     是否为覆盖模式
        """

    def 自动换行(self):
        print(self.pte.lineWrapMode())
        self.pte.setLineWrapMode(QPlainTextEdit.NoWrap)

        """
        178.
        设置文本内容超过控件宽度时, 是否进行自动换行:
            lineWrapMode() -> QPlainTextEdit.LineWrapMode
            setLineWrapMode(QPlainTextEdit.LineWrapMode)
        
        QPlainTextEdit.LineWrapMode :
            QPlainTextEdit.NoWrap
                没有软换行
            QPlainTextEdit.WidgetWidth
                超出控件宽度进行自动换行
        """

    def 格式设置(self):
        tcf = QTextCharFormat()
        tcf.setFontUnderline(True)
        tcf.setUnderlineColor(QColor(200, 100, 100))
        self.pte.setCurrentCharFormat(tcf)
        """
        177.
        字符格式的控制:
            currentCharFormat() -> QTextCharFormat
            setCurrentCharFormat(QTextCharFormat)
            mergeCurrentCharFormat(QTextCharFormat)
        """

    def 只读设置(self):
        self.pte.setReadOnly(True)
        print(self.pte.isReadOnly())

        """
        177.
        setReadOnly(bool)       设置只读
        isReadOnly() -> bool    获取是否只读
        """

    def 占位提示文本(self):
        self.pte.setPlaceholderText("请输入你的个人信息")
        print(self.pte.placeholderText())

        """
        177.
        setPlaceholderText(str)     设置占位文本
        placeholderText() -> str    获取占位文本内容
        
        """
        pass
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.setWindowIcon(QIcon("bb.png"))
    window.show()


    sys.exit(app.exec_())