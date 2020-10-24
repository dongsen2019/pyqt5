from PyQt5.Qt import *
import sys


class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("QComboBox案例")
        self.resize(500, 500)

        self.city_dic = {
            "北京": {
                "东城": "001",
                "西城": "002",
                "朝阳": "003",
                "丰台": "004"
            },
            "上海": {
                "黄埔": "005",
                "徐汇": "006",
                "长宁": "007",
                "静安": "008",
                "松江": "009"
            },
            "广东": {
                "广州": "010",
                "深圳": "011",
                "湛江": "012",
                "佛山": "013"
            }
        }

        self.setup_ui()

    def setup_ui(self):
        pro = QComboBox(self)
        pro.move(100, 100)
        city = QComboBox(self)
        city.move(200, 100)
        self.pro = pro
        self.city = city

        self.pro.currentTextChanged.connect(self.pro_change)

        self.city.currentTextChanged.connect(self.city_change)

        self.pro.addItems(self.city_dic.keys())
        # pro_cur_text = pro.currentText()
        # city.addItems(self.city_dic[pro_cur_text].keys())

    def pro_change(self, pro_str):
        citys = pro_str
        self.city.blockSignals(True)
        self.city.clear()
        self.city.blockSignals(False)

        for k, v in self.city_dic[citys].items():
            self.city.addItem(k, v)

        # city.addItems(self.city_dic[city_str].keys())

    def city_change(self, city_str):
        print(self.city.itemData(self.city.currentIndex()))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()

    sys.exit(app.exec_())
