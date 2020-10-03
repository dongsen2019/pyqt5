from PyQt5.Qt import *


class MyTextEdit(QTextEdit):
    def mousePressEvent(self, me):
        print(me.pos())
        link_str = self.anchorAt(me.pos())
        if len(link_str) > 0:
            QDesktopServices.openUrl(QUrl(link_str))
        return super().mousePressEvent(me)
    """
    anchorAt(QPoint) -> str     返回位置pos处的锚点的引用，如果该点处不存在锚点，则返回空字符串
    QDesktopServices.openUrl(QUrl(urlString))       打开指定链接地址
    """


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QTextEdit的学习")
        self.resize(500, 500)
        self.setup_ui()

    def text_change(self):
        print("文本内容发生了改变")
    def selection_change(self):
        print("文本选中的内容发生了改变")
    def copy_a(self, yes):
        print("复制是否可用", yes)

    """
    信号:
    
    textChanged()   文本内容发生改变时, 发射的信号
    selectionChanged()          选中内容发生改变时, 发射的信号
    cursorPositionChanged()     光标位置发生改变时, 发射的信号
    currentCharFormatChanged(QTextCharFormat)       当前的字符格式发生改变时, 发射的信号
    copyAvailable(bool yes)     复制可用时
    redoAvailable(bool available)   重做可用时
    undoAvailable(bool available)   撤销可用时
    """

    def setup_ui(self):
        te = MyTextEdit("xxx", self)
        self.te = te
        te.move(50, 50)
        te.resize(300, 300)
        te.setStyleSheet("background-color: cyan;")

        te.textChanged.connect(self.text_change)
        # te.selectionChanged.connect(self.selection_change)
        te.copyAvailable.connect(self.copy_a)

        test_btn = QPushButton(self)
        test_btn.move(10, 10)
        test_btn.setText("测试按钮")
        test_btn.pressed.connect(self.btn_test)

        # self.占位文本的提示()
        # self.文本内容的设置()
        # tlf = QTextListFormat()
        # tlf.setIndent(3)
        # tlf.setNumberPrefix("<<")
        # tlf.setNumberSuffix("<<")
        # tlf.setStyle(QTextListFormat.ListDecimal)
        # tl = te.textCursor().createList(tlf)
        te.textCursor().insertTable(5, 3)
        # te.insertHtml("xxx " * 300 + "<a name='lk' href='#itlike'>撩课</a>" + "aaa" * 200)
        te.insertHtml("xxx " * 300 + "<a href='http://www.itlike.com'>撩课</a>" + "aaa" * 200)

    def btn_test(self):
        # self.te.setText("")
        # self.te.clear()
        """143. 清空 clear()"""
        # QTextDocument
        # print(self.te.document())
        """
        144.
        打印文本文档，每个文本编辑器都关联着一个不可视化的文本文档对象
        te.document() -> QTextDocument  获取文本文档
        """
        # QTextCursor
        # print(self.te.textCursor())
        """
        te.textCursor() 文本光标的获取
        """
        self.字体设置()

        pass
    def 打开超链接(self):
        pass

    def tab功能测试(self):
        # self.te.setTabChangesFocus(True)
        print(self.te.tabStopDistance())
        print(self.te.tabStopWidth())
        self.te.setTabStopDistance(100)

        """
        173. tab控制
        setTabChangesFocus(bool)
            控制Tab键位的功能, 是否是改变焦点
            默认是False
        setTabStopDistance(p_float)
            制表位的距离
            默认80(像素)
        setTabStopWidth(p_int)
            经测试, 同 setTabStopDistance 一样
        tabStopDistance(self) -> float
            获取距离
        tabStopWidth() -> int
            获取宽度
        """

        pass
    def 只读设置(self):
        print(self.te.isReadOnly())
        self.te.setReadOnly(True)
        self.te.insertPlainText("itlike")
        print(self.te.isReadOnly())
        """
        172. 只读设置
        setReadOnly(self, bool)
        isReadOnly() -> bool
        
        使得编辑器变为浏览器
        
        只限制用户键盘鼠标操作，不限制代码操作
        """
        pass
    def 滚动到锚点(self):
        self.te.scrollToAnchor("lk")

        "scrollToAnchor(p_str)  滚动到p_str名称的锚点位置"

        """
        171.
        !!!注意:
        锚点设置    <a name="锚点名称" href="#锚点内容"> xxx </a>
        """
        pass
    def 常用编辑操作(self):
        # self.te.copy()    复制
        # self.te.paste()   粘贴
        # self.te.selectAll()   全选
        # self.te.setFocus()    设置焦点
        # QTextDocument.FindBackward    从右往左 往回查找
        print(self.te.find("xx", QTextDocument.FindBackward | QTextDocument.FindCaseSensitively | QTextDocument.FindWholeWords))
        self.te.setFocus()

        """
        170.
        find(str, options: Union[QTextDocument.FindFlags, QTextDocument.FindFlag] = QTextDocument.FindFlags()) -> bool
            QTextDocument.FindBackward
                向后搜索而不是向前搜索。
            QTextDocument.FindCaseSensitively
                默认情况下，查找工作区不区分大小写。
                指定此选项会将行为更改为区分大小写的查找操作。
            QTextDocument.FindWholeWords
                使查找匹配仅完整的单词。
        """
        pass
    def 字符设置(self):
        tcf = QTextCharFormat()
        tcf.setFontFamily("宋体")
        tcf.setFontPointSize(20)
        tcf.setFontCapitalization(QFont.Capitalize)
        tcf.setForeground(QColor(100, 200, 150))
        self.te.setCurrentCharFormat(tcf)
        """
        169.
        QTextCharFormat()   文本字符格式类
            类常用功能及其作用
                字体
                    统一设置
                        setFont(QFont)
                        font() -> QFont
                    字体家族
                        setFontFamily(family_str)
                        fontFamily() -> str
                    字体大小
                        setFontPointSize(float)
                        fontPointSize() -> float
                    字体粗细
                        setFontWeight(int)
                        fontWeight() -> int
                    字体上划线
                        setFontOverline(bool)
                        fontOverline() -> bool
                    字体中划线
                        setFontStrikeOut(bool)
                        fontStrikeOut() -> bool
                    字体下划线
                        setFontUnderline(bool)
                        fontUnderline() -> bool
                    字体大小写
                        setFontCapitalization(QFont.Capitalization)
                        fontCapitalization() -> QFont.Capitalization
                            QFont.MixedCase
                                这是正常的文本呈现选项，不应用大写更改。
                            QFont.AllUppercase
                                这会改变要以全大写类型呈现的文本。
                            QFont.AllLowercase
                                这会改变要以全小写类型呈现的文本。
                            QFont.SmallCaps
                                这会改变要以小型大写字母呈现的文本。
                            QFont.Capitalize
                                这会将要呈现的文本更改为每个单词的第一个字符作为大写字符。
                颜色
                    setForeground(QColor(100, 200, 150))
                超链接
                    setAnchorHref("http://www.itlike.com")
                    anchorHref() -> str
            
        API：
            setCurrentCharFormat(QTextCharFormat)
            设置当前字符格式    
                
            mergeCurrentCharFormat(QTextCharFormat)
            合并当前字符格式
            
            currentCharFormat() -> QTextCharFormat
        """

        tcf2 = QTextCharFormat()
        tcf2.setFontOverline(True)
        # self.te.setCurrentCharFormat(tcf2)
        self.te.mergeCurrentCharFormat(tcf2)

        pass
    def 颜色设置(self):
        self.te.setTextBackgroundColor(QColor(200, 10, 10))
        self.te.setTextColor(QColor(10, 200, 10))
        """
        168.
        背景颜色        
        setTextBackgroundColor(QColor)      将当前格式的文本背景颜色设置为指定颜色
        textBackgroundColor() -> QColor     获取颜色
        
        文本颜色    
        setTextColor(QColor)        将当前格式的文本颜色设置为指定颜色
        textColor() -> QColor       获取颜色
        """
        pass
    def 字体设置(self):
        # QFontDialog.getFont()
        # self.te.setFontFamily("幼圆")
        # self.te.setFontWeight(QFont.Black)
        # self.te.setFontItalic(True)
        # self.te.setFontPointSize(30)
        # self.te.setFontUnderline(True)

        font = QFont()
        font.setStrikeOut(True)
        self.te.setCurrentFont(font)

        """
        167.
        通过 QFontDialog.getFont() 获取对话框    查看可用的字体
        setFontFamily(family_str)       字体家族
        字体样式:
            字体粗细
                setFontWeight(int)
                    QFont.Thin
                    QFont.ExtraLight
                    QFont.Light
                    QFont.Normal
                    QFont.Medium
                    QFont.DemiBold
                    QFont.Bold
                    QFont.ExtraBold
                    QFont.Black
                    从小到大不断加粗
                    
            获取字体粗细  fontWeight()
            
            字体斜体
                setFontItalic(bool) 设置字体为斜体
                fontItalic()
        
        字体尺寸    setFontPointSize(float)     设置字体尺寸
                   fontPointSize()             获取字体尺寸
        
        字体下划线       setFontUnderline(bool)   设置下划线
                        fontUnderline()          获取字体是否设置了下划线
        
        统一设置QFont   setCurrentFont(QFont)
                       currentFont() -> QFont     
                       字体格式对象，通过对象方法设置各个样式，再将该对象传递给setCurrentFont(QFont)函数完成字体设置
        """
    def 对齐方式(self):
        self.te.setAlignment(Qt.AlignCenter)

        """
        166.
        setAlignment(Qt.Alignment)
            常用有效对齐是
                Qt.AlignLeft
                Qt.AlignRight
                Qt.AlignCenter
        
        应用场景    设置当前段落的对齐方式
        """
        pass
    def 光标设置(self):
        # print(self.te.cursorWidth())
        print(self.te.cursorRect(self.te.textCursor()))
        if self.te.overwriteMode():
            self.te.setOverwriteMode(False)
            self.te.setCursorWidth(1)
        else:
            self.te.setOverwriteMode(True)
            self.te.setCursorWidth(10)
        """
        165.
        光标宽度    setCursorWidth(int)
        获取光标宽度  cursorWidth()
        一般是结合覆盖模式来做, 标识光标的宽度, 给用户以提醒当下为覆盖模式
        
        cursorRect() -> QRect   光标矩形 显示光标的位置和尺寸
        """
    def 覆盖模式的设置(self):
        self.te.setOverwriteMode(True)
        print(self.te.overwriteMode())
        """
        164.
        setOverwriteMode(bool)
        作用相当于insert，切换覆盖模式, 输入内容会覆盖后续内容
        """
    def 软换行模式(self):
        # self.te.setLineWrapMode(QTextEdit.NoWrap)
        # self.te.setLineWrapMode(QTextEdit.FixedPixelWidth)
        self.te.setLineWrapMode(QTextEdit.FixedColumnWidth)
        self.te.setLineWrapColumnOrWidth(8)

        self.te.setWordWrapMode(QTextOption.WordWrap)
        """
        163.
        软换行模式   API :
        setLineWrapMode(QTextEdit.LineWrapMode)
            设置软换行模式
        lineWrapMode() -> QTextEdit.LineWrapMode
            获取软换行模式
            
            QTextEdit.LineWrapMode:
                    QTextEdit.NoWrap
                        没有软换行, 超过宽度后, 会产生水平滚动条
                    QTextEdit.WidgetWidth
                        以控件的宽度为限制
                        但会保持单词的完整性
                    QTextEdit.FixedPixelWidth
                        填充像素宽度  配合:
                                            setLineWrapColumnOrWidth(int)
                                            lineWrapColumnOrWidth() -> int
                    QTextEdit.FixedColumnWidth
                        填充列的宽度  配合:
                                            setLineWrapColumnOrWidth(int)
                                            lineWrapColumnOrWidth() -> int           
        setWordWrapMode(self, QTextOption.WrapMode)
            设置单词换行模式
        wordWrapMode(self) -> QTextOption.WrapMode
            获取单词换行模式

            QTextOption.WrapMode
                        QTextOption.NoWrap
                            文本根本没有包装。
                        QTextOption.WordWrap
                            保持单词完整性
                        QTextOption.ManualWrap
                            与QTextOption.NoWrap相同
                        QTextOption.WrapAnywhere
                            宽度够了之后, 随意在任何位置换行
                        QTextOption.WrapAtWordBoundaryOrAnywhere
                            尽可能赶在单词的边界, 否则就在任意位置换行			
        应用场景
            设置当用户输入内容过多时, 是否进行软换行, 以及如何进行软换行
        """
        pass
    def 自动格式化(self):
        QTextEdit
        self.te.setAutoFormatting(QTextEdit.AutoBulletList)
        """
        162.
        
        setAutoFormatting(QTextEdit.AutoFormatting)
        QTextEdit.AutoFormatting:
        
        QTextEdit.AutoNone
            不要做任何自动格式化。
        QTextEdit.AutoBulletList
            自动创建项目符号列表（例如，当用户在最左侧列中输入星号（'*'）时，或在现有列表项中按Enter键。
        QTextEdit.AutoAll
            应用所有自动格式。目前仅支持自动项目符号列表。
        """
    def 开始和结束操作(self):
        tc = self.te.textCursor()

        tc.beginEditBlock()
        tc.insertText("123")
        tc.insertBlock()
        tc.insertText("456")
        tc.insertBlock()
        tc.endEditBlock()
        """
        160.
        介于beginEditBlock()和endEditBlock()之间的所有操作，从撤消/重做的角度显示为单个操作。
        """

        tc.insertText("789")
        tc.insertBlock()

        pass
    def 位置相关(self):
        tc = self.te.textCursor()
        print("是否在段落的结尾:", tc.atBlockEnd())
        print("是否在段落的开始:", tc.atBlockStart())
        print("是否在文档的结尾:", tc.atEnd())
        print("是否在文档的开始:", tc.atStart())

        print("在第几列", tc.columnNumber())
        print("光标位置", tc.position())
        print("在文本块(段落)中的位置", tc.positionInBlock())

        pass
    def 文本字符的删除(self):
        tc = self.te.textCursor()
        # tc.deleteChar()
        tc.deletePreviousChar()
        self.te.setFocus()
        """
        158.
        deleteChar()
            如果没有选中文本, 删除文本光标后一个字符
            如果有选中文本, 则删除选中文本
        deletePreviousChar()
            如果没有选中文本, 删除文本光标前一个字符
            如果有选中文本, 则删除选中文本
        """
        pass
    def 文本的其他操作(self):
        tc = self.te.textCursor()
        # print(tc.selectionStart())
        # print(tc.selectionEnd())
        """
        157.
        选中的位置获取
        selectionStart() -> int     获取选中内容的起始位置
        selectionEnd() -> int       获取选中内容的结束位置
        """
        # tc.clearSelection()
        # self.te.setTextCursor(tc)
        "clearSelection()   取消文本的选中(需要反向设置)"
        # print(tc.hasSelection())
        "hasSelection() -> bool     是否有选中文本"
        tc.removeSelectedText()
        "removeSelectedText()   移除选中的文本(也可以移除表格中的内容)"
        self.te.setFocus()
        pass
    def 文本选中内容的获取(self):
        tc = self.te.textCursor()
        # print(tc.selectedText())
        QTextDocumentFragment
        # print(tc.selection().toPlainText())
        print(tc.selectedTableCells())
        """
        156.
        selectedText() -> str   获取当前选中的文本内容
        selection() -> QTextDocumentFragment    选中的文本片段句子
        selection().toPlainText()   将选中的文本片段转化为普通文本
        selectedTableCells() -> (int firstRow, int numRows, int firstColumn, int numColumns)    选中的表格单元
                                    选择的首行       选中几行    选中的首列           选中几列
        """
        pass
    def 文本选中和清空(self):
        tc = self.te.textCursor()
        "获取文本光标"

        tc.setPosition(6, QTextCursor.KeepAnchor)
        """
        155.
        setPosition(self, int, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor)
        设置光标位置和移动模式QTextCursor.MoveMode:
        
        QTextCursor.MoveAnchor
            将锚点移动到与光标本身相同的位置。
        QTextCursor.KeepAnchor
            将锚固定在原处。
        """

        tc.movePosition(QTextCursor.Up, QTextCursor.KeepAnchor, 1)
        """
        155.
        movePosition(self, QTextCursor.MoveOperation, mode: QTextCursor.MoveMode = QTextCursor.MoveAnchor, n: int = 1)
        QTextCursor.MoveOperation:
        
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
        """
        tc.select(QTextCursor.WordUnderCursor)
        """
        select(QTextCursor.SelectionType)   需要反向设置
        """
        self.te.setTextCursor(tc)
        """
        setPosition(int pos, QTextCursor.MoveMode=MoveAnchor)
            设置光标位置
            需要反向设置回去
        """

        self.te.setFocus()
        pass
    def 内容和格式的获取(self):
        tc = self.te.textCursor()
        "tc.currentList() ----> QTextList"
        "tc.block() ----> QTextBlock"
        # print(tc.block().text())
        "154.文本块的内容"
        # print(tc.blockNumber())
        "块的编号"
        print(tc.currentList().count())
        "当前所在文本列表的条目数"

        """
        154.
        获取内容和格式相关   API
        block() -> QTextBlock
            获取光标所在的文本块
        blockFormat() -> QTextBlockFormat
            获取光标所在的文本块格式
        blockCharFormat() -> QTextCharFormat
            获取光标所在的文本块字符格式
        blockNumber() -> int
            获取光标所在的文本块编号
        charFormat() -> QTextCharFormat
            获取文本字符格式
        currentFrame() -> QTextFrame
            获取当前所在的框架
        currentList() -> QTextList 
            获取当前所在的文本列表
        currentTable() -> QTextTable 
            获取当前的表格
        应用场景
            通过文本光标获取当前所在的内容和格式信息
        """

        pass
    def 格式设置和合并(self):
        tc = self.te.textCursor()
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")
        tcf.setFontPointSize(30)
        tcf.setFontOverline(True)
        tcf.setFontUnderline(True)
        "设置QTextCharFormat格式"
        tc.setCharFormat(tcf)
        """
        153.
        setCharFormat(QTextCharFormat)
        将光标的当前字符格式设置为给定格式。如果光标有选择，则给定格式应用于当前选择
        """

        tcf2 = QTextCharFormat()
        tcf2.setFontStrikeOut(True)
        # tc.setCharFormat(tcf2)
        tc.mergeCharFormat(tcf2)
        """
        mergeBlockCharFormat(QTextCharFormat)   合并当前块的char格式
        mergeBlockFormat(QTextBlockFormat)  合并当前块的格式
        mergeCharFormat(QTextCharFormat)    合并当前字符格式
        """

        return None
        tbf = QTextBlockFormat()
        tbf.setAlignment(Qt.AlignCenter)    # 段落居中
        tbf.setIndent(2)    # 2个Tab缩进
        "设置文本块格式"
        tc.setBlockFormat(tbf)
        """
        setBlockFormat(QTextBlockFormat)
        设置当前块的块格式（或选择中包含的所有块）以进行格式化
        """

        return None
        tcf = QTextCharFormat()
        tcf.setFontFamily("幼圆")    # 字体类型
        tcf.setFontPointSize(30)    # 字体大小
        tcf.setFontOverline(True)   # 上划线
        tcf.setFontUnderline(True)  #下划线
        "设置文本字符格式"
        tc.setBlockCharFormat(tcf)
        """
        setBlockCharFormat(QTextCharFormat) 
        设置要格式化的当前块（或选择中包含的所有块）的块char 格式
        """

        pass
    def 光标插入内容(self):
        tc = self.te.textCursor()
        tff = QTextFrameFormat()
        tff.setBorder(10)
        "设置边框宽度"
        tff.setBorderBrush(QColor(100, 50, 50))
        "设置边框颜色"
        tff.setRightMargin(50)
        "设置右边距"
        tc.insertFrame(tff)
        """
        152.
        插入框架    insertFrame(QTextFrameFormat) -> QTextFrame
        """

        doc = self.te.document()
        QTextFrame
        root_frame = doc.rootFrame()
        "获取文本编辑控件的文本文档根框架"
        root_frame.setFrameFormat(tff)
        "设置根框架的格式"

        return None
        tc = self.te.textCursor()
        tbf = QTextBlockFormat()
        tcf = QTextCharFormat()
        tcf.setFontFamily("隶书")
        tcf.setFontItalic(True)
        tcf.setFontPointSize(60)
        tbf.setAlignment(Qt.AlignRight)
        "对齐方式"
        tbf.setRightMargin(100)
        "右边距"
        # tbf.setIndent(3)
        "设置3个缩进"
        tc.insertBlock(tbf, tcf)
        self.te.setFocus()
        """
        151.
        插入文本块:
        insertBlock()   插入一个空的文本块   
        insertBlock(QTextBlockFormat)   插入文本块的同时, 设置文本块格式   
        insertBlock(QTextBlockFormat, QTextCharFormat )     插入文本块的同时, 设置文本块格式和文本字符格式
        """

        return None
        tc = self.te.textCursor()
        # tc.insertTable(5, 3)
        "149. 插入表格"
        "insertTable(int rows, int columns) -> QTextTable 在光标处插入表格"
        ttf = QTextTableFormat()
        ttf.setAlignment(Qt.AlignRight)
        """
        tff.setAlignment(self, Union[Qt.Alignment, Qt.AlignmentFlag])    对齐方式
        
        水平:
        Qt.AlignLeft
        Qt.AlignRight
        Qt.AlignHCenter
        Qt.AlignJustify     此处同左对齐
        
        垂直:
        Qt.AlignTop
        Qt.AlignBottom
        Qt.AlignVCenter
        Qt.AlignBaseline
        
        Qt.AlignCenter:
        等同于    Qt.AlignHCenter | Qt.AlignVCenter
        垂直和水平都居中
        """

        ttf.setCellPadding(6)
        ttf.setCellSpacing(13)
        "setCellPadding(self, p_float)  内边距"
        "setCellSpacing(self, p_float)  外边距"
        QTextLength
        ttf.setColumnWidthConstraints((QTextLength(QTextLength.PercentageLength, 50), QTextLength(QTextLength.PercentageLength, 40), QTextLength(QTextLength.PercentageLength, 10)))
        """
        150. 列宽约束
        setColumnWidthConstraints(self, Iterable[QTextLength])  注意第一参数需要是可迭代对象(元组，列表)
        
        QTextLength(QTextLength.Type, float)
        QTextLength.Type:
        FixedLength = 1     固定长度
        PercentageLength = 2    百分比
        VariableLength = 0  可变长度
        """
        QTextTable
        # print(tc.insertTable(5, 3, ttf))
        table = tc.insertTable(5, 3, ttf)
        """
        149. 
        insertTable(int rows, int columns, QTextTableFormat) -> QTextTable 
        在光标处插入几行几列且 表格格式为 QTextTableFormat 的表格
        """
        # table.appendColumns(2)
        """
        QTextTable中的方法，追加2列
        """

        return None
        tc = self.te.textCursor()
        # tl = tc.insertList(QTextListFormat.ListCircle)
        # tl = tc.insertList(QTextListFormat.ListDecimal)
        # tl = tc.createList(QTextListFormat.ListDecimal)
        tlf = QTextListFormat()
        tlf.setIndent(3)
        tlf.setNumberPrefix("<<")
        tlf.setNumberSuffix("<<")
        tlf.setStyle(QTextListFormat.ListDecimal)
        tl = tc.createList(tlf)
        print(tl)
        QTextList
        """
        148.
        插入列表
            insertList(QTextListFormat) -> QTextList 
                在当前位置插入一个新块，并使其成为具有给定格式的新创建列表的第一个列表项。返回创建的列表
            insertList(QTextListFormat.Style) -> QTextList 
                在当前位置插入一个新块，并使其成为具有给定格式的新创建列表的第一个列表项。返回创建的列表
            createList(QTextListFormat) -> QTextList 
                创建并返回具有给定格式的新列表，并使当前段落的光标位于第一个列表项中
            createList(QTextListFormat.style ) -> QTextList 
                创建并返回具有给定格式的新列表，并使当前段落的光标位于第一个列表项中
        补充
        QTextListFormat()   文本列表格式类
            setIndent(int)
            # 设置缩进距离
            setNumberPrefix(str)
            # 设置 数字形式 列表标签的前缀
            setNumberSuffix(str)
            # 设置 数字形式 列表标签的后缀
            setStyle(QTextListFormat.Style)
            设置列表的样式枚举值 ————> QTextListFormat.Style
        QTextListFormat.Style
            QTextListFormat.ListDisc
                一个圆圈
            QTextListFormat.ListCircle
                一个空的圆圈
            QTextListFormat.ListSquare
                一个方块
            QTextListFormat.ListDecimal
                十进制值按升序排列
            QTextListFormat.ListLowerAlpha
                小写拉丁字符按字母顺序排列
            QTextListFormat.ListUpperAlpha
                大写拉丁字符按字母顺序排列
            QTextListFormat.ListLowerRoman
                小写罗马数字（仅支持最多4999项）
            QTextListFormat.ListUpperRoman
                大写罗马数字（仅支持最多4999项）
        """
        return None

        tc = self.te.textCursor()
        # tdf = QTextDocumentFragment.fromHtml("<h1>xxx</h1>")
        tdf = QTextDocumentFragment.fromPlainText("<h1>xxx</h1>")
        tc.insertFragment(tdf)
        "147. 此方法为类方法:  "
        "QTextDocumentFragment.fromHtml(str)   引入富文本字符串"
        "QTextDocumentFragment.fromPlainText(str)   引入纯文本字符串"

        return None

        tc = self.te.textCursor()
        tif = QTextImageFormat()
        "146. 创建文本图片格式"
        tif.setName("E:\pycharm\source/rose.png")
        "设置图片路径"
        tif.setWidth(100)
        "设置图片宽度"
        tif.setHeight(100)
        "设置图片高度"
        tc.insertImage(tif)
        "插入带有设置为对象tif格式图片"
        # tc.insertImage(tif, QTextFrameFormat.FloatRight)
        "QTextFrameFormat.FloatRight    图片浮动靠右"
        # tc.insertImage("xx.jpg")
        "直接插入该路径的图片（过期但可用）"

        return None
        QTextCursor
        tcf = QTextCharFormat()
        "145. "
        "创建文本字符格式"
        tcf.setToolTip("撩课学院网址")
        "设置本文的贴士"
        tcf.setFontFamily("隶书")
        "设置字体"
        tcf.setFontPointSize(66)
        "设置字体尺寸"
        tc = self.te.textCursor()
        """
        获取文本光标(与鼠标光标不同，鼠标光标请见04-QWidget-鼠标相关操作)
        """
        tc.insertText("itlike.com", tcf)
        "在光标处插入文本，并使用对象tcf文本字符格式"

        tc.insertHtml("<a href='http://www.itlike.com'> 撩课 </a>")
        "插入富文本"

        pass

    def 文本内容的设置(self):
        # 设置普通文本内容
        # self.te.setPlainText("<h1>ooo</h1>")
        # self.te.insertPlainText("<h1>ooo</h1>")
        # print(self.te.toPlainText())
        """
        142.文本的设置-上

        setPlainText(str)   设置普通文本(纯文本)
        insertPlainText(str)    在光标处插入普通文本
        toPlainText() -> str    将文本框的内容转换为普通文本
        """
        # 富文本的操作
        # self.te.setHtml("<h1>ooo</h1>")
        # self.te.insertHtml("<h6>社会我顺哥</h6>")
        # print(self.te.toHtml())
        # self.te.setText("<h1xxx>ooo</h1xxx>")
        # self.te.append("<h3>ooo</h3>")
        """
        142.文本的设置-上
        
        setHtml(str)    设置HTML富文本
        insertHtml(str) 插入富文本（在光标处）
        toHtml() -> str 将文本框的内容转换为富文本
        设置文本(自动判定)      setText(str)
        追加文本                append(str) 【无论光标在何处，都会在最后新的段落插入文本】
        清空                      clear()
        """

        pass

    def 占位文本的提示(self):
        self.te.setPlaceholderText("请输入你的个人简介")
        print(self.te.placeholderText())
        """
        141.占位文本的设置
        
        setPlaceholderText(str)     设置占位文本
        placeholderText() -> str    占位文本的获取
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
