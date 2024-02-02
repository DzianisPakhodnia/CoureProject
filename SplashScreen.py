from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import MainWindow
import sys


class SplashScreen(QMainWindow):
    """
        Класс начального экрана

        @author Pokhodnia D. A.
        @version 1.0, 21.11.2023
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cams = None
        self.title = "Начальный экран"
        self.width = 937
        self.height = 700
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.setStyleSheet("background-color: #FFE4C4;")

        # создание времени в 60 секунд
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.close)
        self.timer.start(60000)

        # создание кнопки Далее
        self.button_window1 = QPushButton('Далее', self)
        self.button_window1.move(70, 610)
        self.button_window1.setFixedSize(341, 61)
        self.button_window1.setStyleSheet("background-color: blue; color: white;border-radius: 20px;"
                                          "font-family: Arial; font-size: 16pt; font-weight: bold; ")
        font_button1 = QFont("Arial", 16)
        font_button1.setBold(True)
        font_button1.setWeight(75)
        self.button_window1.setFont(font_button1)
        self.button_window1.clicked.connect(self.close_splash_screen)

        # создание кнопки Выхода
        self.button_window2 = QPushButton('Выход', self)
        self.button_window2.move(500, 610)
        self.button_window2.setFixedSize(341, 61)
        self.button_window2.setStyleSheet("background-color: red; color: white;border-radius: 20px;font-family: "
                                          "Arial; font-size: 16pt; font-weight: bold; ")
        self.button_window2.clicked.connect(self.close)

        # создание надписи БНТУ
        self.label1 = QLabel("Белорусский национальный технический университет", self)
        self.label1.setGeometry(220, 20, 461, 41)
        self.label1.setAlignment(Qt.AlignCenter)
        font1 = QFont("Arial", 10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label1.setFont(font1)

        # создание надписи ФИТР
        self.label2 = QLabel("Факультет информационных технологий и робототехники", self)
        self.label2.setGeometry(160, 70, 611, 41)
        self.label2.setAlignment(Qt.AlignCenter)
        font2 = QFont("Arial", 12)
        font2.setBold(True)
        font2.setWeight(75)
        self.label2.setFont(font2)

        # создание надписи имени Кафедры
        self.label3 = QLabel("Кафедра программного обеспечивание информационных технологий систем и технологий", self)
        self.label3.setGeometry(90, 130, 771, 41)
        font3 = QFont("Arial", 10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label3.setFont(font3)

        # создание надписи Курсовая работа
        self.label4 = QLabel("Курсовая работа", self)
        self.label4.setGeometry(320, 200, 301, 41)
        self.label4.setAlignment(Qt.AlignCenter)
        font4 = QFont("Arial", 18)
        font4.setBold(True)
        font4.setWeight(75)
        self.label4.setFont(font4)

        # создание надписи по дисциплине
        self.label5 = QLabel("по дисциплине:", self)
        self.label5.setGeometry(270, 250, 141, 41)
        font5 = QFont("Arial", 10)
        font5.setBold(True)
        font5.setWeight(75)
        self.label5.setFont(font5)

        # создание надписи Языки программирования
        self.label6 = QLabel("Языки программирования", self)
        self.label6.setGeometry(410, 250, 241, 41)
        font6 = QFont("Arial", 11)
        font6.setWeight(75)
        self.label6.setFont(font6)

        # создание надписи Вычисление корней уравнений методом простых итераций
        self.label7 = QLabel("Вычисление корней уравнений методом простых итераций", self)
        self.label7.setGeometry(160, 300, 701, 51)
        font7 = QFont("Arial", 12)
        font7.setBold(True)
        font7.setWeight(75)
        self.label7.setFont(font7)

        # создание надписи Выполнил: Студент ...
        self.label8 = QLabel("Выполнил: Студент группы 10701222", self)
        self.label8.setGeometry(550, 370, 321, 20)
        font8 = QFont("Arial", 10)
        font8.setBold(True)
        font8.setWeight(75)
        self.label8.setFont(font8)

        # создание надписи ФИО автора
        self.label9 = QLabel("Походня Денис Александрович", self)
        self.label9.setGeometry(550, 410, 321, 20)
        font9 = QFont("Arial", 10)
        font9.setBold(True)
        font9.setWeight(75)
        self.label9.setFont(font9)

        # создание надписи Преподаватель: к.ф.-м.н., доц
        self.label10 = QLabel("Преподаватель: к.ф.-м.н., доц", self)
        self.label10.setGeometry(550, 460, 321, 31)
        font10 = QFont("Arial", 10)
        font9.setBold(True)
        font10.setWeight(75)
        self.label10.setFont(font10)

        # создание надписи Сидорик Валерий Владимирович
        self.label11 = QLabel("Сидорик Валерий Владимирович", self)
        self.label11.setGeometry(550, 510, 321, 16)
        font11 = QFont("Arial", 10)
        font11.setWeight(75)
        self.label11.setFont(font11)

        # создание надписи Минск, 2023
        self.label12 = QLabel("Минск, 2023", self)
        self.label12.setGeometry(380, 560, 151, 41)
        font12 = QFont("Arial", 12)
        font12.setWeight(75)
        self.label12.setFont(font12)

        # вставка картинки
        self.label13 = QLabel(self)
        self.label13.setGeometry(140, 360, 221, 191)
        self.pix = QPixmap("photo/iteration.png")
        self.label13.setPixmap(self.pix)
        self.label13.setScaledContents(True)

        self.show()

    def close_splash_screen(self):
        self.cams = MainWindow.MainWindow()
        self.cams.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SplashScreen()
    sys.exit(app.exec_())
