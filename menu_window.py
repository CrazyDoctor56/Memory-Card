from PyQt6.QtWidgets import (QLabel, QLineEdit, QPushButton,
                              QWidget, QVBoxLayout, QHBoxLayout)


menu_window = QWidget()

menu_v_line = QVBoxLayout()

menu_h_line_1 = QHBoxLayout()
menu_h_line_2 = QHBoxLayout()
menu_h_line_3 = QHBoxLayout()
menu_h_line_4 = QHBoxLayout()
menu_h_line_5 = QHBoxLayout()
menu_h_line_6 = QHBoxLayout()

menu_q_text_lb_1 = QLabel("Введіть текст питання")
menu_a_text_lb_1 = QLabel("Введіть текст правильної відповіді")
menu_w_text_lb_1 = QLabel("Введіть текст варіантів неправильної відповіді")
menu_w_text_lb_2 = QLabel("Введіть текст варіантів неправильної відповіді")
menu_w_text_lb_3 = QLabel("Введіть текст варіантів неправильної відповіді")


menu_q_text_input_1 = QLineEdit()
menu_a_text_input_1 = QLineEdit()
menu_w_text_input_1 = QLineEdit()
menu_w_text_input_2 = QLineEdit()
menu_w_text_input_3 = QLineEdit()


menu_btn_add = QPushButton("Додати питання")
menu_btn_clear = QPushButton("Очистити")
menu_h_line_6.addWidget(menu_btn_add)
menu_h_line_6.addWidget(menu_btn_clear)
menu_v_line.addLayout(menu_h_line_6)

menu_window.setLayout(menu_v_line)


menu_h_line_1.addWidget(menu_q_text_lb_1)
menu_h_line_1.addWidget(menu_q_text_input_1)
menu_v_line.addLayout(menu_h_line_1)

menu_h_line_2.addWidget(menu_a_text_lb_1)
menu_h_line_2.addWidget(menu_a_text_input_1)
menu_v_line.addLayout(menu_h_line_2)

menu_h_line_3.addWidget(menu_w_text_lb_1)
menu_h_line_3.addWidget(menu_w_text_input_1)
menu_v_line.addLayout(menu_h_line_3)

menu_h_line_4.addWidget(menu_w_text_lb_2)
menu_h_line_4.addWidget(menu_w_text_input_2)
menu_v_line.addLayout(menu_h_line_4)

menu_h_line_5.addWidget(menu_w_text_lb_3)
menu_h_line_5.addWidget(menu_w_text_input_3)
menu_v_line.addLayout(menu_h_line_5)




menu_back_btn = QPushButton("Назад")
menu_v_line.addWidget(menu_back_btn)


menu_window.setLayout(menu_v_line)