from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication,QMessageBox,QWidget,QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout
app = QApplication([])
window = QWidget()
window.setWindowTitle("Конкурс")
window.resize(500,300)

def wrong():
    win = QMessageBox()
    win.setText("Ви програли:(")
    win.exec_()

label = QLabel("Скільки років викладачу??")

def right():
    win = QMessageBox()
    win.setText("Ви виграли:)")
    win.exec_()

label = QLabel("-> Як звали першого ютуб-блогера, який набрав 100000000 підписників?")

but1 = QRadioButton("- PewDiePie")
but2 = QRadioButton("- Рет і Лінк")
but3 = QRadioButton("- SlivkiShow")
but4 = QRadioButton("- TheBrianMaps")
but5 = QRadioButton("- Mister Max")
but6 = QRadioButton("- EeOneGuy")

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
lineV = QVBoxLayout()

line1.addWidget(label, alignment = Qt.AlignCenter)

line2.addWidget(but1, alignment = Qt.AlignCenter)
line2.addWidget(but2, alignment = Qt.AlignCenter)

line3.addWidget(but3, alignment = Qt.AlignCenter)
line3.addWidget(but4, alignment = Qt.AlignCenter)

line4.addWidget(but5, alignment = Qt.AlignCenter)
line4.addWidget(but6, alignment = Qt.AlignCenter)

lineV.addLayout(line1)
lineV.addLayout(line2)
lineV.addLayout(line3)
lineV.addLayout(line4)

but1.clicked.connect(right)
but2.clicked.connect(wrong)
but3.clicked.connect(wrong)
but4.clicked.connect(wrong)
but5.clicked.connect(wrong)
but6.clicked.connect(wrong)

window.setLayout(lineV)

window.show()
app.exec_()
