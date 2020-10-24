from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFontDialog的学习")
        self.resize(500, 500)

        self.setup_ui()

    def setup_ui(self):

        # fd = QFontDialog(self)
        font = QFont()
        font.setFamily("宋体")
        font.setPointSize(36)
        # # fd = QFontDialog(font, self)
        # fd = QFontDialog(self)
        """
        构造函数
            QFontDialog(parent: QWidget = None)
            QFontDialog(QFont, parent: QWidget = None)      QFont:设置对话框当前字体
        """

        # fd.setCurrentFont(font)
        """
        当前字体
            setCurrentFont(QFont)   也就是弹出字体选择对话框时，默认选择的字体
            currentFont() -> QFont
        """

        # # fd.setOption(QFontDialog.NoButtons)
        # fd.setOptions(QFontDialog.NoButtons | QFontDialog.MonospacedFonts)
        # print(fd.testOption(QFontDialog.MonospacedFonts))
        # print(fd.testOption(QFontDialog.ScalableFonts))
        """
        setOption(QFontDialog.FontDialogOption, on=True)
            on = True   设置该选项
            on = False  取消该选项

        setOptions(QFontDialog.FontDialogOption)    设置多个选项
        testOption(QFontDialog.FontDialogOption)    测试某个选项是否生效
        options() -> QFontDialog.FontDialogOption   获取当前的选项

        QFontDialog.FontDialogOption
            QFontDialog.NoButtons   不显示“ 确定”和“ 取消”按钮。（对“实时对话框”有用。）
            QFontDialog.DontUseNativeDialog     在Mac上使用Qt的标准字体对话框而不是Apple的原生字体面板。
            QFontDialog.ScalableFonts       显示可缩放字体
            QFontDialog.NonScalableFonts    显示不可缩放的字体
            QFontDialog.MonospacedFonts     显示等宽字体
            QFontDialog.ProportionalFonts   显示比例字体
        """

        btn = QPushButton(self)
        btn.setText("按钮")
        btn.move(100, 100)

        # fd.show()

        label = QLabel(self)
        label.move(200, 100)
        label.setText("社会顺哥")

        fd = QFontDialog(self)
        for child in fd.children():
            if child.inherits("QDialogButtonBox"):
                for c in child.children():
                    if c.inherits("QPushButton"):
                        if c.text().lower() == "ok":
                            c.setText("确定呀")
                        else:
                            c.setText("取消呀")
        fd.show()

        def font_sel():
            pass
        # result = QFontDialog.getFont(self)
        #     result = QFontDialog.getFont(font,self,"选择一个好看的字体")
        "result返回True或者false，表示选择确定还是取消！"
        #     if result[1]:
        #         label.setFont(result[0])
        #         label.adjustSize()
        # btn.clicked.connect(font_sel)
        """
        静态方法：
            getFont(parent: QWidget = None) -> Tuple[QFont, bool]
            getFont(QFont, parent: QWidget = None, caption: str = '', options: QFontDialog.FontDialogOption) -> Tuple[QFont, bool]
            参数
                1: 默认字体
                2. 父控件
                3. 对话框标题
                4. 选项
            返回值 (最终字体, 是否点击确认)
        """

        # def cfc(font):
        #     label.setFont(font)
        #     label.adjustSize()
        # fd.currentFontChanged.connect(cfc)
        """
        信号
            currentFontChanged(QFont)   当前字体发生改变时
            fontSelected(QFont)         最终选择字体时
        """

        # def font_sel():
        #     print("字体已经被选择", fd.selectedFont().family())

        """
        最终选中字体      selectedFont() -> QFont     QFont.family()返回字体类型
        """

        btn.clicked.connect(lambda :fd.open(font_sel))
        """
        打开对话框
            open(self)
            open(PYQT_SLOT)     打开后, 会自动连接fontSelected信号与此处指定的槽函数
            exec() -> int
        """

        # if fd.exec():
        #     print(fd.selectedFont().family())
        "通过 执行accept或是reject 所返回的值来判定是否打印字体"


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    translator = QTranslator()
    locale = QLocale.system().name()
    print(QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    translator.load('qt_%s' % locale, QLibraryInfo.location(QLibraryInfo.TranslationsPath))
    app.installTranslator(translator)

    window = Window()
    window.show()

    sys.exit(app.exec_())
