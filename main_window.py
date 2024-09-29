from PyQt6.QtWidgets import (QWidget, QLabel, QRadioButton,
                              QPushButton, QGroupBox, QButtonGroup,
                              QVBoxLayout, QHBoxLayout)

C_HEIGHT = 600
C_WIDTH = 700

window = QWidget()
window.resize(C_WIDTH, C_HEIGHT)
window.setWindowTitle("Memory Card")

question_lb = QLabel()

rb_answer_1 = QRadioButton()
rb_answer_2 = QRadioButton()
rb_answer_3 = QRadioButton()
rb_answer_4 = QRadioButton()

btn = QPushButton("Відповісти")

radio_btn_box = QGroupBox("Варіанти відповідей")
radio_btn_group = QButtonGroup()

radio_btn_group.addButton(rb_answer_1)
radio_btn_group.addButton(rb_answer_2)
radio_btn_group.addButton(rb_answer_3)
radio_btn_group.addButton(rb_answer_4)

answer_box = QGroupBox("Результат")
result_lb = QLabel("Правильно/неправильно")
correct_answer_lb = QLabel("Правильна відповідь")

main_v_line = QVBoxLayout()

radio_btn_box_v_line = QVBoxLayout()
radio_btn_box_h_line_1 = QHBoxLayout()
radio_btn_box_h_line_2 = QHBoxLayout()

radio_btn_box_h_line_1.addWidget(rb_answer_1)
radio_btn_box_h_line_1.addWidget(rb_answer_2)

radio_btn_box_h_line_2.addWidget(rb_answer_3)
radio_btn_box_h_line_2.addWidget(rb_answer_4)

radio_btn_box_v_line.addLayout(radio_btn_box_h_line_1)
radio_btn_box_v_line.addLayout(radio_btn_box_h_line_2)

radio_btn_box.setLayout(radio_btn_box_v_line)

main_v_line.addWidget(question_lb)
main_v_line.addWidget(radio_btn_box)


answer_box_v_line = QVBoxLayout()
answer_box_v_line.addWidget(result_lb)
answer_box_v_line.addWidget(correct_answer_lb)

answer_box.setLayout(answer_box_v_line)

main_v_line.addWidget(answer_box)




















main_v_line.addWidget(btn)

answer_box.hide()

window.setLayout(main_v_line)