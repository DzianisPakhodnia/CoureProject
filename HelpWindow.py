import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
import MainWindow


class HelpWindow(QMainWindow):
    """
        Класс окна c инструкцией

        @author Pokhodnia D. A.
        @version 1.0, 23.11.2023
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.title = "Инструкция"
        self.width = 700
        self.height = 400
        self.setStyleSheet("background-color: #FFE4C4;")
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setWindowTitle('Окно помощи')

        # создание надписи: Инструкция пользования программы
        self.text_label = QLabel("Инструкция пользования программы", self)
        self.text_label.setStyleSheet("font-family: Arial; font-size: 26px; font-weight: bold;")
        self.text_label.setGeometry(105, 5, 490, 65)

        # создание блока надписей
        self.info_group_box = QGroupBox(self)
        self.info_group_box.setGeometry(30, 80, 661, 211)
        self.layout_info = QVBoxLayout(self.info_group_box)
        self.text_label1 = QLabel("1. Выберите график функции и нажмите на него", self)
        self.text_label1.setStyleSheet("font-family: Arial; font-size: 20px;")
        self.layout_info.addWidget(self.text_label1)
        self.text_label2 = QLabel("2. Введите границы графика", self)
        self.text_label2.setStyleSheet("font-family: Arial; font-size: 20px;")
        self.layout_info.addWidget(self.text_label2)

        self.text_label3 = QLabel("3. Нажмите кнопку «Построить график»", self)
        self.text_label3.setStyleSheet("font-family: Arial; font-size: 20px;")
        self.layout_info.addWidget(self.text_label3)

        self.text_label4 = QLabel("4. Анализируем график и вводим приблизительный корень уравнения", self)
        self.text_label4.setStyleSheet("font-family: Arial; font-size: 20px;")
        self.layout_info.addWidget(self.text_label4)

        self.text_label5 = QLabel("5. Вводим значение точности вычислений", self)
        self.text_label5.setStyleSheet("font-family: Arial; font-size: 20px;")
        self.layout_info.addWidget(self.text_label5)

        self.text_label6 = QLabel("6. Нажимаем кнопку «Решить уравнение» и получаем решение", self)
        self.text_label6.setStyleSheet("font-family: Arial; font-size: 20px;")
        self.layout_info.addWidget(self.text_label6)

        self.button_exit = QPushButton('Назад', self)
        self.button_exit.setGeometry(244, 300, 211, 81)
        self.button_exit.setStyleSheet("background-color: red; color: white;border-radius: 20px;font-family:"
                                       "Arial; font-size: 16pt; font-weight: bold; ")
        self.button_exit.clicked.connect(self.close)
