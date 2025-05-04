from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Кто лучший футболист мира','Рональдо','Месси','Меси','Мессси'))
questions_list.append(Question('Как называется комсическое измерение которое засасывает всё','Чёрная дыра','Инопланетяни','Кишкоблуд','Планета Юпитер'))
questions_list.append(Question('Как называются ресурс который не легко сломать','Обсидиан','Бедрок','Эндерняк','Паутина'))
questions_list.append(Question('Какого цвета кит','синий','красный','белый','зелёный'))
questions_list.append(Question('Кто изобрёл вакцину от оспы','Пастер','Джунгарики','Маугли','Мечников'))
questions_list.append(Question('Кто в шахматах ходит буквой г','Конь','Я','Пешка','Король'))
questions_list.append(Question('Какой вид спорта лучше всего для здоровья','Плавание','Дзюдо','Бокс','Хобихорсинг'))
questions_list.append(Question('Что падает зимой','Снег','Метеориты','Кислотные капли','Дети'))
questions_list.append(Question('Правильный ответ А','Г','Б','А','Д'))
questions_list.append(Question('Как с английского на русский язык будет window','Окно','Дверь','Заставка','Стекло'))
questions_list.append(Question('Кто по утрам встаёт раньше всех и кричит кукареку','петух','собака','человек','корова')) 
app = QApplication([])


btn_OK = QPushButton('Ответить') 
lb_Question = QLabel('Самый сложный вопрос в мире!') 


RadioGroupBox = QGroupBox("Варианты ответов")


rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')


RadioGroup = QButtonGroup() 
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)


RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?') 
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)


layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result():
    ''' показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    ''' показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False) # сняли ограничения, чтобы можно было сбросить выбор радиокнопки
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True) # вернули ограничения, теперь только одна радиокнопка может быть выбрана

def test():
    ''' временная функция, которая позволяет нажатием на кнопку вызывать по очереди
    show_result() либо show_question() '''
    if 'Ответить' == btn_OK.text():
        show_result()
    else:
        show_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')
 # проверяем, что панель ответов показывается при нажатии на кнопку
answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика \n -Всего вопросов:', window.total, '\n -Правильных ответов:')
        print('Рейтинг:', window.score / window.total * 100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
        print('Рейтинг:', window.score / window.total * 100,'%')
def next_question():
    '''задаёт следующий вопрос из списка'''
    window.total += 1 
    print('Статистика \n -Всего вопросов:', window.total, '\n -Правильных ответов:')
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]

    ask(q)
def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()
window.score = 0
window.total = 0
btn_OK.clicked.connect(click_OK)
next_question()
window.show()
app.exec()
