from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices
import MainWindow
import sys


class AboutAuthor(QDialog):
    """
        Класс окна c информацией об авторе

        @author Pokhodnia D. A.
        @version 1.0, 23.11.2023
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.cams = None
        self.title = "Об авторе"
        self.top = 100
        self.left = 100
        self.width = 576
        self.height = 756
        self.setStyleSheet("background-color: #FFE4C4;")
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)

        # создание надписи Автор
        self.label1 = QLabel("Автор", self)
        self.label1.setGeometry(245, 370, 81, 31)
        font1 = QFont()
        font1.setFamily("Arial")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setUnderline(True)
        self.label1.setFont(font1)

        # создание надписи Студент группы 10701222
        self.label2 = QLabel("Студент группы 10701222", self)
        self.label2.setGeometry(140, 410, 291, 41)
        font2 = QFont()
        font2.setFamily("Arial")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        font2.setUnderline(True)
        self.label2.setFont(font2)

        # создание надписи Походня Денис Александрович
        self.label3 = QLabel("Походня Денис Александрович", self)
        self.label3.setGeometry(110, 460, 361, 41)
        font3 = QFont()
        font3.setFamily("Arial")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        font3.setUnderline(True)
        self.label3.setFont(font3)

        # создание кнопки перехода на главное окно
        self.button_window1 = QPushButton('Назад', self)
        self.button_window1.setGeometry(200, 670, 161, 51)
        self.button_window1.setStyleSheet("background-color: red; color: white;border-radius: 20px;")
        self.button_window1.clicked.connect(self.close)
        font_button1 = QFont("Arial", 16)
        font_button1.setBold(True)
        font_button1.setWeight(75)
        self.button_window1.setFont(font_button1)

        # добавление фото
        self.my_photo = QLabel(self)
        self.my_photo.setGeometry(160, 20, 271, 321)
        self.my_photo.setScaledContents(True)
        pixmap = QPixmap('photo/me1.png')
        self.my_photo.setPixmap(pixmap)

        # добавление кнопки телеграмма автора
        self.button_telegram = QPushButton(self)
        self.button_telegram.setIcon(QIcon('photo/telegram.png'))
        self.button_telegram.setIconSize(QSize(111, 111))
        self.button_telegram.move(70, 530)
        self.button_telegram.setStyleSheet("""
        QPushButton{
            border-radius: 250;
            border:none;
            }
            
            QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0.2);
                }
            """)
        self.button_telegram.clicked.connect(self.open_telegram)

        # добавление кнопки перехода на почту
        self.button_google_mail = QPushButton(self)
        self.button_google_mail.setIcon(QIcon('photo/GoogleMail.png'))
        self.button_google_mail.setIconSize(QSize(111, 111))
        self.button_google_mail.move(220, 530)
        self.button_google_mail.setStyleSheet("""
                QPushButton{
                     border-radius: 250;
                     border:none;
                     }
                QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0.2);
                }
                     """
                                              )
        self.button_google_mail.clicked.connect(self.open_mail)

        # добавление кнопки перехода на git-hub автора
        self.button_git_hub = QPushButton(self)
        self.button_git_hub.setIcon(QIcon('photo/github-logo.png'))
        self.button_git_hub.setIconSize(QSize(111, 111))
        self.button_git_hub.move(370, 530)
        self.button_git_hub.setStyleSheet("""
                QPushButton{
                    border-radius: 250;
                    border:none;
                }
                QPushButton:pressed{
                background-color: rgba(0, 0, 0, 0.2);
                }
                    
                    """
                                          )
        self.button_git_hub.clicked.connect(self.open_git_hub)

    @staticmethod
    def open_telegram():
        url = QUrl("https://t.me/butfirsttea")
        QDesktopServices.openUrl(url)

    @staticmethod
    def open_git_hub():
        url = QUrl("https://github.com/DenisPokhodnia")
        QDesktopServices.openUrl(url)

    @staticmethod
    def open_mail():
        url = QUrl("https://denispokhodnia@gmail.com")
        QDesktopServices.openUrl(url)
