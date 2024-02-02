from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
import MainWindow
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout


class AboutProgram(QDialog):
    """
        Класс окна c информацией об программе

        @author Pokhodnia D. A.
        @version 1.0, 24.11.2023
    """

    def __init__(self, parent=None):
        super().__init__(parent)

        self.cams = None
        self.title = "О программе"
        self.width = 1145
        self.height = 593
        self.setStyleSheet("background-color: #FFE4C4;")
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # надпись: Вычисление корней уравнений методом простых итераций
        self.label = QLabel("Вычисление корней уравнений методом простых итераций", self)
        self.label.setGeometry(140, 30, 831, 41)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        # создание групового блока с информацией об программе
        self.info_group_box = QGroupBox(self)
        self.info_group_box.setGeometry(540, 100, 571, 331)
        self.layout_info = QVBoxLayout(self.info_group_box)
        self.label_main = QLabel("Программа позволяет: ", self.info_group_box)
        self.layout_info.addWidget(self.label_main)

        self.label_main.setFont(font)

        # добавление линии
        self.line_info = QFrame(self.info_group_box)
        self.line_info.setFrameShape(QFrame.HLine)
        self.line_info.setFrameShadow(QFrame.Sunken)
        self.layout_info.addWidget(self.line_info)

        self.label1 = QLabel("1. Выбирать предложенные функции", self.info_group_box)
        self.layout_info.addWidget(self.label1)
        self.label2 = QLabel("2. Вводить значения: интервал, точность,\nприблежённый корень", self.info_group_box)
        self.layout_info.addWidget(self.label2)

        self.label3 = QLabel('3. Строить график функции на\n'
                             + 'введённом интервале, и изображение найденного\n'
                             + 'корня ', self.info_group_box)
        self.layout_info.addWidget(self.label3)

        self.label4 = QLabel("4. Вычислять корень методом простых итераций", self.info_group_box)
        self.layout_info.addWidget(self.label4)

        font_info = QFont()
        font_info.setFamily("Arial")
        font_info.setPointSize(13)
        font_info.setBold(True)
        font_info.setWeight(75)

        self.label1.setFont(font_info)
        self.label2.setFont(font_info)
        self.label3.setFont(font_info)
        self.label4.setFont(font_info)

        self.label_photo = QLabel()
        self.label_photo = QLabel(self)
        self.label_photo.setGeometry(40, 100, 461, 431)
        self.pix_photo = QPixmap("photo/iteration.png")
        self.label_photo.setPixmap(self.pix_photo)
        self.label_photo.setScaledContents(True)

        # создание блока для надписи Версии
        self.version_group_box = QGroupBox(self)
        self.version_group_box.setGeometry(540, 450, 341, 81)
        self.layout_version = QVBoxLayout(self.version_group_box)
        self.label_version = QLabel("Версия ver. 1.0.0.2023", self.version_group_box)
        font_version = QFont()
        font_version.setPointSize(16)
        font_version.setItalic(True)
        font_version.setWeight(600)
        self.label_version.setFont(font_version)
        self.layout_version.addWidget(self.label_version)

        self.button_exit = QPushButton('Выход', self)
        self.button_exit.setGeometry(900, 450, 211, 81)
        self.button_exit.setStyleSheet("background-color: red; color: white;border-radius: 20px;font-family:"
                                       "Arial; font-size: 16pt; font-weight: bold; ")
        self.button_exit.clicked.connect(self.close)
