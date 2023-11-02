from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from random import randint

def click():
    num = randint(1,10)
    numser.setText(str(num))
    num2 = randint(1,10)
    numser2.setText(str(num2))
    if num2 == num:
        text.setText('Win')
    else:
        text.setText('lose')

   




app = QApplication([])
main_win = QWidget()


main_win.setWindowTitle('Лотерея')
main_win.resize(400,200)
main_win.move(600,200)
win = ''

text = QLabel(f'{win}Натисніть, щоб взяти участь')
numser = QLabel('?')
numser2 = QLabel('?')
buttom = QPushButton('Випрубувати удачу')


line = QVBoxLayout()
line.addWidget(text,alignment=Qt.AlignCenter)
line.addWidget(numser,alignment=Qt.AlignCenter)
line.addWidget(numser2,alignment=Qt.AlignCenter)
line.addWidget(buttom,alignment=Qt.AlignCenter)
main_win.setLayout(line)

buttom.clicked.connect(click)



main_win.show()
app.exec()