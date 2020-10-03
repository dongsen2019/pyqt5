from PyQt5.Qt import *
import sys
import math

app = QApplication(sys.argv)

window = QWidget()
window.resize(500, 500)
window.move(300, 300)

w_count = 50

w_columns = 3

w_width = window.width() / w_columns
w_rows = math.ceil(w_count / w_columns)
w_height = window.height() / w_rows

print(w_width, w_height)

for i in range(w_count):
    w = QWidget(window)
    w.resize(w_width, w_height)
    row = i // w_columns
    column = i % w_columns
    w.move(w_width * column, w_height * row)
    w.setStyleSheet("background: red;"
                    "border: 1px solid yellow;")

window.show()

sys.exit(app.exec_())
