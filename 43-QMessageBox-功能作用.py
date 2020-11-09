from PyQt5.Qt import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QMessageBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        # QMessageBox.about(self, "xx1", "xx2")
        # QMessageBox.aboutQt(self, "xx1")
        result = QMessageBox.question(self, "xx1", "xx2", QMessageBox.Ok | QMessageBox.Discard, QMessageBox.Discard)
        print(result, "xxx")

        """
        静态方法    (阻塞式)
            about(QWidget, str, str)
            aboutQt(QWidget, title: str = '')
            critical(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton
            information(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton
            question(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.StandardButtons(QMessageBox.Yes|QMessageBox.No), defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton
            warning(QWidget, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.Ok, defaultButton: QMessageBox.StandardButton = QMessageBox.NoButton) -> QMessageBox.StandardButton
        """

        return None
        mb = QMessageBox(self)
        # mb = QMessageBox(QMessageBox.Warning, "xx1", "<h2>xx2</h2>",QMessageBox.Ok | QMessageBox.Discard, self)
        """
        对话框各个位置的设置示意图见Xmind

        构造函数
            QMessageBox(parent: QWidget = None)
                QMessageBox(QMessageBox.Icon, str, str, buttons: Union[QMessageBox.StandardButtons, QMessageBox.StandardButton] = QMessageBox.NoButton, parent: QWidget = None, flags: Union[Qt.WindowFlags, Qt.WindowType] = Qt.Dialog|Qt.MSWindowsFixedSizeDialogHint)
                    第一参数 QMessageBox.Icon ：
                        QMessageBox.NoIcon          消息框没有任何图标。
                        QMessageBox.Question        一个图标，表示该消息正在提问。
                        QMessageBox.Information     一个图标，表示该消息没有任何异常。
                        QMessageBox.Warning         一个图标，表示该消息是一个警告，但可以处理。
                        QMessageBox.Critical        一个图标，表示该消息代表一个严重问题。

                    第二参数 str-->窗口标题

                    第三参数 str-->主标题

                    第四参数 buttons-->弹出对话框的按钮

                    第五参数 父控件
        """
        # mb.setModal(False)
        # mb.setWindowModality(Qt.NonModal)
        "设置非模态的两种方法"

        mb.setWindowTitle("消息提示")
        "对话框标题      setWindowTitle(str)"

        # mb.setIcon(QMessageBox.Information)
        """
        图标设置
            标准图标
                setIcon(QMessageBox.Icon)   icon(self) -> QMessageBox.Icon
                QMessageBox.NoIcon          消息框没有任何图标。
                QMessageBox.Question        一个图标，表示该消息正在提问。
                QMessageBox.Information     一个图标，表示该消息没有任何异常。
                QMessageBox.Warning         一个图标，表示该消息是一个警告，但可以处理。
                QMessageBox.Critical        一个图标，表示该消息代表一个严重问题。
        """

        mb.setIconPixmap(QPixmap("xxx.png").scaled(50, 50))
        "自定义图标      setIconPixmap(QPixmap)      iconPixmap(self) -> QPixmap"

        # mb.setTextFormat(Qt.PlainText)
        """
        setTextFormat(self, Qt.TextFormat)      textFormat()
            Qt.TextFormat
                    PlainText
                    RichText
                    AutoText
        """

        mb.setText("<h3>文件内容已经被修改</h3>")
        """
        主要标题
            setText(str)    text()
        """

        mb.setInformativeText("<h4>是否直接关闭, 不保存?</h4>")
        "提示文本   setInformativeText(str)     informativeText() -> str"

        mb.setCheckBox(QCheckBox("下次不再提醒", mb))
        "复选框    setCheckBox(self, QCheckBox)    checkBox(self) -> QCheckBox"

        mb.setDetailedText("<h4>你修改的内容是给每一行代码加了一个分号</h4>")
        "详细文本(不支持富文本)   setDetailedText(self, str)      detailedText() -> str"

        # mb.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        """
        QMessageBox.ButtonRole
            InvalidRole     该按钮无效。
            AcceptRole      单击该按钮将使对话框被接受（例如，确定）。
            RejectRole      单击该按钮会导致拒绝对话框（例如取消）。
            DestructiveRole 单击该按钮会导致破坏性更改（例如，对于Discarding Changes）并关闭对话框。
            ActionRole      单击该按钮将导致更改对话框中的元素。
            HelpRole        可以单击该按钮以请求帮助。
            YesRole         按钮是一个“是”的按钮。
            NoRole          按钮是一个“否”按钮。
            ApplyRole       该按钮应用当前更改。
            ResetRole       该按钮将对话框的字段重置为默认值。
        
        QMessageBox.StandardButton
            QMessageBox.Ok              使用AcceptRole定义的“确定”按钮。
            QMessageBox.Open            使用AcceptRole定义的“打开”按钮。
            QMessageBox.Save            使用AcceptRole定义的“保存”按钮。
            QMessageBox.Cancel          使用RejectRole定义的“取消”按钮。
            QMessageBox.Close           使用RejectRole定义的“关闭”按钮。
            QMessageBox.Discard         “丢弃”或“不保存”按钮，具体取决于使用DestructiveRole定义的平台。
            QMessageBox.Apply           使用ApplyRole定义的“应用”按钮。
            QMessageBox.Reset           使用ResetRole定义的“重置”按钮。
            QMessageBox.RestoreDefaults 使用ResetRole定义的“恢复默认值”按钮。
            QMessageBox.Help            使用HelpRole定义的“帮助”按钮。
            QMessageBox.SaveAll         使用AcceptRole定义的“全部保存”按钮。
            QMessageBox.Yes             使用YesRole定义的“是”按钮。
            QMessageBox.YesToAll        使用YesRole定义的“Yes to All”按钮。
            QMessageBox.No              使用NoRole定义的“否”按钮。
            QMessageBox.NoToAll         使用NoRole定义的“No to All”按钮。
            QMessageBox.Abort           使用RejectRole定义的“Abort”按钮。
            QMessageBox.Retry           使用AcceptRole定义的“重试”按钮。
            QMessageBox.Ignore          使用AcceptRole定义的“忽略”按钮。
            QMessageBox.NoButton        无按钮。
        """

        mb.addButton(QPushButton("xx1", mb), QMessageBox.YesRole)
        """
        添加按钮
            addButton(self, QAbstractButton, QMessageBox.ButtonRole)
            addButton(self, str, QMessageBox.ButtonRole) -> QPushButton
            addButton(self, QMessageBox.StandardButton) -> QPushButton
        """

        mb.addButton(QPushButton("xx2", mb), QMessageBox.NoRole)
        # btn2 = mb.addButton("xx2", QMessageBox.NoRole)
        # mb.removeButton(btn2)
        "移除按钮       removeButton(self, QAbstractButton)"

        # mb.setDefaultButton(btn2)
        """
        默认按钮
            setDefaultButton(self, QPushButton)
            setDefaultButton(self, QMessageBox.StandardButton)
            defaultButton(self) -> QPushButton
        """

        # mb.setEscapeButton(btn2)
        """
        退出按钮
            setEscapeButton(self, QAbstractButton)
            setEscapeButton(self, QMessageBox.StandardButton)
            escapeButton(self) -> QAbstractButton
            按Esc 激活的按钮
        """

        # print(btn)
        # print(btn2)
        # yes_btn = mb.button(QMessageBox.Yes)
        "1.获取按钮对象，可以用于槽函数比对"
        # no_btn = mb.button(QMessageBox.No)


        # print(yes_btn, no_btn)
        mb.setTextInteractionFlags(Qt.TextEditorInteraction)
        """
        文本交互
            setTextInteractionFlags(Qt.TextInteractionFlag)
            textInteractionFlags() -> Qt.TextInteractionFlag
        补充
            Qt.TextInteractionFlag
                Qt.NoTextInteraction	        不可能与文本进行交互。
                Qt.TextSelectableByMouse        可以使用鼠标选择文本并使用上下文菜单或标准键盘快捷键将其复制到剪贴板。
                Qt.TextSelectableByKeyboard     可以使用键盘上的光标键选择文本。显示文本光标。
                Qt.LinksAccessibleByMouse       可以使用鼠标突出显示和激活链接。
                Qt.LinksAccessibleByKeyboard    可以使用选项卡聚焦链接并使用enter激活。
                Qt.TextEditable                 该文字完全可编辑。
                Qt.TextEditorInteraction        文本编辑器的默认值。
                上条等价于   TextSelectableByMouse | TextSelectableByKeyboard | TextEditable
                Qt.TextBrowserInteraction       QTextBrowser的默认值。
                上条等价于   TextSelectableByMouse | LinksAccessibleByMouse | LinksAccessibleByKeyboard
        """

        def test(btn):
            role = mb.buttonRole(btn)
            "2.获取按钮的角色进行比对"

            if role == QMessageBox.YesRole:
                print("1")
            elif role == QMessageBox.NoRole:
                print("2")

            # print(btn)
            # if btn == yes_btn:
            #     print("点击了第1个按钮")
            # else:
            #     print("点击了第2个按钮")
            "1.获取按钮对象，可以用于槽函数比对"
        mb.buttonClicked.connect(test)
        """
        信号      buttonClicked(QAbstractButton button)
        """

        mb.open()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
