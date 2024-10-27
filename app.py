from random import choice, shuffle
from PyQt6.QtWidgets import QApplication

# General of programm


app = QApplication([])

from main_window import *
from menu_window import *

class Question:
    def __init__(self, question_text, answer_text, wrong:tuple):
        self.question_text = question_text
        self.answer_text = answer_text

        self.wrong_answers = wrong

q1 = Question("Яблуко", "Apple", ("Application", "ape", "pineapple"))
q2 = Question("Дім", "Home", ("Horse", "hore", "homee"))
q3 = Question("Миша", "Rat", ("Red", "Person", "comp"))
q4 = Question("Машина", "Car", ("Rar", "Gar", "Park"))


questions_list = [q1, q2, q3, q4]
r_b_list = [rb_answer_1, rb_answer_2, rb_answer_3, rb_answer_4]


def new_question():
    global random_question
    random_question = choice(questions_list)
    shuffle(r_b_list)
    
    question_lb.setText(random_question.question_text)

    r_b_list[0].setText(random_question.answer_text)

    for i in range(3):
        r_b_list[i + 1].setText(random_question.wrong_answers[i])

new_question()


def check_result():
    correct_answer_lb.setText(random_question.answer_text)
    radio_btn_group.setExclusive(False)

    for btn in r_b_list:
        if btn.isChecked():
            btn.setChecked(False)
            if btn.text() == random_question.answer_text:
                result_lb.setText("Правильно")
                
                break

    else:
        result_lb.setText("Неправильно")

    radio_btn_group.setExclusive(True)

def change_box():
    if btn.text() == "Відповісти":

        radio_btn_box.hide()
        answer_box.show()

        btn.setText("Наступне питання")
        check_result()

    elif btn.text() == "Наступне питання":
        radio_btn_box.show()
        answer_box.hide()

        btn.setText("Відповісти")

        new_question()


btn.clicked.connect(change_box)

def open_menu():
    window.hide()
    menu_window.show()

def close_menu():
    window.show()
    menu_window.hide()


menu_btn.clicked.connect(open_menu)
menu_back_btn.clicked.connect(close_menu)

def clear_menu():
    menu_w_text_input_1.clear()
    menu_w_text_input_2.clear()
    menu_w_text_input_3.clear()
    menu_a_text_input_1.clear()
    menu_q_text_input_1.clear()


menu_btn_clear.clicked.connect(clear_menu)

def add_question():
    new_q = Question(
        menu_q_text_input_1.text(),
        menu_a_text_input_1.text(), 
        (
            
            menu_w_text_input_1.text(),
            menu_w_text_input_2.text(),
            menu_w_text_input_3.text()


        )
    )

    questions_list.append(new_q)
    clear_menu()

menu_btn_add.clicked.connect(add_question)





window.show()

app.exec()