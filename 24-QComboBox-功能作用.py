from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QComboBox的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        cb = QComboBox(self)
        """
        构造出一个空白的下拉列表控件
        后续通过操作数据的方法设置数据列表
        
        构造函数    QComboBox(parent: QWidget = None)
        """
        cb.addItems(["abc", "123", "456"])
        cb.addItem(QIcon("xxx.jpg"), "撩课", {"name": "itlike"})
        cb.resize(100, 60)

        btn = QPushButton(self)
        btn.move(100, 100)
        btn.setText("测试按钮")
        # btn.clicked.connect(lambda :print(cb.count()))
        # btn.clicked.connect(lambda :print(cb.currentIndex()))
        # btn.clicked.connect(lambda :print(cb.currentText()))
        # btn.clicked.connect(lambda :print(cb.currentData()))
        # btn.clicked.connect(lambda : btn.setIcon(cb.itemIcon(cb.currentIndex())))
        # btn.clicked.connect(lambda   _,  idx = cb.count()-1:print(cb.itemIcon(idx), cb.itemText(idx), cb.itemData(idx)))
        "_   忽略传递的第一参数"

        """
        获取相关数据:
            count() -> int
            itemIcon(int index) -> QIcon
            itemText(int index) -> str
            itemData(int index) -> Any
            currentIndex() -> int
            currentText() -> str
        """
        # btn.clicked.connect(lambda :cb.addItem("it"))
        # btn.clicked.connect(lambda :cb.clear())
        # btn.clicked.connect(lambda :cb.clearEditText())
        # btn.clicked.connect(lambda :cb.showPopup())
        btn.clicked.connect(lambda :cb.setCurrentIndex(2))
        """
        清空  
            clear()     移除所有项目
            clearEditText()     清除组合框中用于编辑的行编辑内容
        """

        cb.setEditable(True)
        """
        可编辑
            setEditable(bool editable)
            isEditable()
        """

        cb.setMaxCount(6)
        # cb.setMaxVisibleItems(3)
        """
        限制数据内容显示等限制
            setMaxCount(int max)
            maxCount() 
            setMaxVisibleItems(int maxItems)
            maxVisibleItems()
        """

        # cb.setDuplicatesEnabled(True)
        cb.setDuplicatesEnabled(True)

        """
        可重复
            setDuplicatesEnabled(bool enable)
            duplicatesEnabled()
        """

        cb.setCompleter(QCompleter(["123", "abc", "aaa", "bbb"]))
        """
        完成器
            setCompleter(QCompleter completer)
            completer() -> QCompleter
        """

        # cb.activated[str].connect(lambda val:print("条目被激活", val))

        # cb.currentIndexChanged[str].connect(lambda val:print("当前索引发生改变", val))
        # cb.currentTextChanged.connect(lambda val:print("当前文本发生改变", val))
        # cb.editTextChanged.connect(lambda val:print("当前编辑文本发生改变", val))
        # cb.highlighted[int].connect(lambda val:print("高亮发生改变", val))
        cb.highlighted[str].connect(lambda val:print("高亮发生改变", val))

        """
        信号
            activated(int index)    某个条目被选中时    必须是用户交互, 造成的值改变才会发射这个信号
            activated(QString text) 某个条目被选中时    必须是用户交互, 造成的值改变才会发射这个信号
            currentIndexChanged(int index)  当前选中的索引发生改变时    用户交互和代码控制
            currentIndexChanged(QString text)   当前选中的索引发生改变时    用户交互和代码控制
            currentTextChanged(QString text)    当前的文本内容发生改变时
            editTextChanged(QString text)       编辑的文本发生改变时
            highlighted(int index)      高亮
            highlighted(QString text)   高亮
        """

        # cb.setFrame(False)

        """
        有框架
            setFrame(bool)
            hasFrame()
        """

        cb.setIconSize(QSize(60, 60))
        """
        图标尺寸
            setIconSize(QSize)
            iconSize()
        """

        # cb.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        """
        尺寸调整策略
            setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy policy)
                QComboBox.AdjustToContents	    组合框将始终根据内容进行调整
                QComboBox.AdjustToContentsOnFirstShow     组合框将在第一次显示时调整其内容。
                QComboBox.AdjustToMinimumContentsLength   请改用AdjustToContents或AdjustToContentsOnFirstShow。
                QComboBox.AdjustToMinimumContentsLengthWithIcon    组合框将调整为minimumContentsLength加上图标的空间。出于性能原因，请在大型模型上使用此策略。
            sizeAdjustPolicy() -> QComboBox.SizeAdjustPolicy
            setMinimumContentsLength(int characters)
            minimumContentsLength() -> int
        """

        # cb.addItem("xx1")
        # cb.addItem("xx2")
        # cb.addItem(QIcon("xxx.png"), "xx3")
        # cb.addItems(["1", "2", "3"])
        # cb.addItems(("1", "2", "3"))
        # cb.addItems("123")

        """
        添加条目项
            addItem(str, userData: Any = None)
            addItem(QIcon, str, userData: Any = None)
            addItems(Iterable[str])
        """

        # cb.insertItem(1, "xxx")
        # cb.insertItem(1, QIcon("xxx.png"), "xxx")
        # cb.insertItems(1, ("1", "a", "b"))

        """
        插入条目项
            insertItem(int index, str, userData: Any = None)
            insertItem(int index, QIcon, str, userData: Any = None)
            insertItems(int index, Iterable[str])
        """

        # cb.setItemIcon(2, QIcon("xxx.jpg"))
        # cb.setItemText(2, "社会顺")
        """
        设置条目项
            setItemIcon(int index, QIcon)
            setItemText(int index, str)
            setItemData(int index, Any, role: int = Qt.UserRole)
        """

        # # cb.removeItem(2)
        """
            删除条目项   removeItem(int index)
        """

        # cb.insertSeparator(2)
        """
            插分割线    insertSeparator(int index)
        """

        #
        # # cb.setCurrentIndex(1)
        # cb.setCurrentText("社会顺")

        # cb.setEditable(True)
        # cb.setEditText("itlike")
        """
        设置当前编辑文本
            setCurrentIndex(int index)
            setCurrentText(QString  text)
            setEditText(QString text)       结合设置可被编辑    setEditable(bool)
        """

        # cb.resize(400, 30)
        # print(QAbstractItemModel.__subclasses__())
        "打印所有抽象模型的子类"
        # model = QStandardItemModel()  创建标准模型
        #
        # item1 = QStandardItem("item1")    创建标准项目
        # item2 = QStandardItem("item2")
        # item22 = QStandardItem("item22")
        # item2.appendRow(item22)   为项目添加子项目
        # model.appendRow(item1)    为模型添加项目
        # model.appendRow(item2)
        # cb.setModel(model)        设置模型
        #
        # cb.setView(QTreeView(cb)) 设置树视图

        """
        模型操作
            setModel(QAbstractItemModel model)
            setModelColumn(int visibleColumn)
            setRootModelIndex(QModelIndex index)
            model()
            modelColumn()
            rootModelIndex()
            
        视图操作
            setView(QAbstractItemView *itemView)
            view()
        """


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
