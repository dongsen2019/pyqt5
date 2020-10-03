from PyQt5.Qt import *


class AgeVadidator(QValidator):
    def validate(self, input_str, pos_int):
        print(input_str, pos_int)

        # 判定
        # 结果字符串, 应该全部都是由一些数字组成
        # return
        """
        如果不使用异常处理，当输入的事字母或空字符串，转为整型时就会报错
        """
        try:
            if 18 <= int(input_str) <= 180:
                return (QValidator.Acceptable, input_str, pos_int)
            elif 1 <= int(input_str) <= 17:
                return (QValidator.Intermediate, input_str, pos_int)
            else:
                return (QValidator.Invalid, input_str, pos_int)
        except:
            if len(input_str) == 0:
                return (QValidator.Intermediate, input_str, pos_int)
            return (QValidator.Invalid, input_str, pos_int)
    """
    lesson 124,125,126
    
    1.验证器：用于验证用户输入数据的合法性
    
    2.如果一个输入框设置了验证器，到时用户在文本框中输入内容时，首先会将内容传递给验证器进行验证
    validate(self, input_text, pos)
    return (QValidator.Acceptable,  input_text, pos)    验证通过
    return (QValidator.Intermediate,  input_text, pos)  暂不作判定是否通过验证
    return (QValidator.Invalid,  input_text, pos)   验证不通过
    """


    def fixup(self, p_str):
        print("xxx", p_str)
        try:
            if int(p_str) < 18:
                return "18"
            else:
                return "180"
        except:
            return "18"

    """
        3.如果输入框结束输入后, 上述的验证状态并非有效, 则会调用修复方法
        fixup(self, input_text)
        return 修正后文本
    """

# ***************以上为自定义子类***************


# ***************以下为系统给定的子类****************** 开始

class MyAgeVadidator(QIntValidator):
    def fixup(self, p_str):
        print("xxx", p_str)
        if len(p_str) == 0 or int(p_str) < 18:
        # if int(p_str) < 18 or len(p_str) == 0:
            return "18"


"QIntValidator(bottom, top, parent)  限制整型数据范围"
# ***************以上为系统给定的子类****************** 结束

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QLineEidt验证器的学习")
        self.resize(500, 500)
        self.setup_ui()

    def setup_ui(self):
        le = QLineEdit(self)
        le.move(100, 100)
        # 18 - 180
        # vadidator = AgeVadidator()
        # vadidator = QIntValidator(18, 180)
        vadidator = MyAgeVadidator(18, 180)
        le.setValidator(vadidator)

        """
        QValidator 是C++的一个抽象类, 使用前需要进行子类化操作
        
        1.可以自定义子类
        
        2.系统提供子类：
            (1) QIntValidator(bottom, top, parent)  限制整型数据范围
            (2) QDoubleValidator    浮点类型数据限制范围  !!!经测试, 无效  需要手动实现
            (3) QRegExpValidator    通过正则表达式限定
        """

        le2 = QLineEdit(self)
        le2.move(200, 200)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()


    sys.exit(app.exec_())