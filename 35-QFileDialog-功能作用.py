from PyQt5.Qt import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QFileDialog的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        result = QFileDialog.getOpenFileName(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        print(result)
        # result = QFileDialog.getOpenFileNames(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getOpenFileUrl(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getSaveFileName(self, "选择一个py文件", "./", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)", "Python文件(*.py)")
        # result = QFileDialog.getExistingDirectory(self, "选择一个py文件", "./")
        # result = QFileDialog.getExistingDirectoryUrl(self, "选择一个py文件", QUrl("./"))
        # print(result)

        """
        最简单的获取方式(静态方法)
            获取文件
                getOpenFileName(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', 
                initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str]
                    parent：父对象
                    caption：对话框名称
                    directory：默认的路径
                    filter：能够选择的文件类型
                    initialFilter：初始的选择文件类型
                    options：控制选项
                    返回元组：Tuple[str, str] ---> [打开文件的绝对路径，过滤类型]
                    
                getOpenFileNames(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', 
                initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) 
                    返回：-> Tuple[List[str], str] ---> [文件路径元组,过滤类型]
                    
                getOpenFileUrl(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', 
                initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str]
                
                getOpenFileUrls(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', 
                initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[List[QUrl], str]
                    "把路径包装成Qurl地址，以便后期用Qt操作文件"
                
                getSaveFileName(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0) -> Tuple[str, str]
                getSaveFileUrl(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '', initialFilter: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = 0, supportedSchemes: Iterable[str] = []) -> Tuple[QUrl, str]
                    "拿到保存路径把文件保存到所在路径里"
                
            获取文件夹
                getExistingDirectory(parent: QWidget = None, caption: str = '', directory: str = '', options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly) -> str
                getExistingDirectoryUrl(parent: QWidget = None, caption: str = '', directory: QUrl = QUrl(), options: Union[QFileDialog.Options, QFileDialog.Option] = QFileDialog.ShowDirsOnly, supportedSchemes: Iterable[str] = []) -> QUrl
                
                    "获取文件夹路径"
                
            补充
                过滤字符串格式     名称1(*.jpg *.png);;名称2(*.py)
        """

        def test():
            fd = QFileDialog(self, "选择一个文件", "../", "All(*.*);;Images(*.png *.jpg);;Python文件(*.py)")
            """
            QFileDialog(QWidget, Union[Qt.WindowFlags, Qt.WindowType])
            QFileDialog(parent: QWidget = None, caption: str = '', directory: str = '', filter: str = '')
            """

            # fd.fileSelected.connect(lambda file: print(file))
            "连接信号，当选择文件时发送选择文件路径的字符串"

            # fd.setAcceptMode(QFileDialog.AcceptSave)
            """
            接收模式(选择对话框为打开或保存文件)
                acceptMode() -> QFileDialog.AcceptMode
                setAcceptMode(QFileDialog.AcceptMode)

            补充
                QFileDialog.AcceptMode
                    QFileDialog.AcceptOpen      打开
                    QFileDialog.AcceptSave      保存
            """

            # fd.setDefaultSuffix("txt")
            """
            默认后缀
                setDefaultSuffix(str)
                defaultSuffix() -> str
            """

            fd.setFileMode(QFileDialog.ExistingFile)
            """
            设置文件模式
                setFileMode(QFileDialog.ExistingFile)
                fileMode() -> QFileDialog.FileMode
            补充
                QFileDialog.FileMode
                    QFileDialog.AnyFile         文件的名称，无论是否存在。(配合保存窗口使用，可以保存为任何形式的文件，如果用QFileDialog.ExistingFile，则只能保存为已经出现过的文件)
                    QFileDialog.ExistingFile    单个现有文件的名称。
                    QFileDialog.Directory       目录的名称。显示文件和目录。但是，本机Windows文件对话框不支持在目录选择器中显示文件。
                    QFileDialog.ExistingFiles   零个或多个现有文件的名称。
            """
            # fd.setNameFilter("IMG(*.jpg *.png *.jpeg)")
            # fd.setNameFilters(["All(*.*)", "Images(*.png *.jpg)", "Python文件(*.py)"])
            """
            设置名称过滤器
                setNameFilter(str)
                setNameFilters(str)
            """

            # fd.setViewMode(QFileDialog.Detail)
            "没用"

            fd.setLabelText(QFileDialog.FileName, "顺哥的文件")
            fd.setLabelText(QFileDialog.Accept, "顺哥的接受")
            fd.setLabelText(QFileDialog.Reject, "顺哥的拒绝")
            """
            设置指定角色的标签名称
                setLabelText(self, QFileDialog.DialogLabel, str)
                    QFileDialog.FileName
                    QFileDialog.Accept
                    QFileDialog.Reject
                    QFileDialog.FileType
                    QFileDialog.LookIn
            """

            # fd.currentChanged.connect(lambda path: print("当前路径字符串发生改变时", path))
            # fd.currentUrlChanged.connect(lambda url: print("当前路径QUrl发生改变时", url))
            # fd.directoryEntered.connect(lambda path: print("当前目录字符串进入时", path))
            # fd.directoryUrlEntered.connect(lambda url: print("当前目录QUrl进入时", url))
            # fd.filterSelected.connect(lambda filter: print("当前名称过滤字符串被选中时", filter))
            # fd.setFileMode(QFileDialog.ExistingFiles)
            fd.fileSelected.connect(lambda val: print("单个文件被选中-字符串", val))
            fd.filesSelected.connect(lambda val: print("多个文件被选中-列表[字符串]", val))
            fd.urlSelected.connect(lambda val: print("单个文件被选中-url", val))
            fd.urlsSelected.connect(lambda val: print("多个文件被选中-列表[url]", val))
            """
            信号
                currentChanged(path_str)            当前路径发生改变时
                currentUrlChanged(QUrl)             当前路径url发生改变时
                directoryEntered(directory_str)     打开选中文件夹时
                directoryUrlEntered(QUrl directory) 打开选中文件夹url时
                filterSelected(filter_str)          选择名称过滤器时
                fileSelected(str)                   最终选择文件时
                filesSelected([str])                选择多个文件时
                urlSelected(QUrl url)               最终选择url时
                urlsSelected(List[QUrl])            最终选择多个url时
            """

            fd.open()

        btn = QPushButton(self)
        btn.setText("测试按钮")
        btn.move(100, 100)
        btn.clicked.connect(test)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()

    sys.exit(app.exec_())
