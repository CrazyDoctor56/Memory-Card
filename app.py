from PyQt6.QtWidgets import QApplication

app = QApplication([])

from main_window import *

def change_box():
    if btn.text() == "Відповісти":

        radio_btn_box.hide()
        answer_box.show()

        btn.setText("Наступне питання")

    elif btn.text() == "Наступне питання":
        radio_btn_box.show()
        answer_box.hide()

        btn.setText("Відповісти")


btn.clicked.connect(change_box)















window.show()

app.exec()