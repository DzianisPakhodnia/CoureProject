from PyQt5.QtWidgets import *
import matplotlib.pyplot as plt
import AboutAuthor
import HelpWindow
import AboutProgram
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    """
        Класс главного окна

        @author Pokhodnia D. A.
        @version 1.1, 05.12.2023
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.point_text = None
        self.point_plot = None
        self.toolbar = None
        self.ax = None
        self.figure = None
        self.canvas = None
        self.new_window = None
        self.x_min = None
        self.x_max = None
        self.eps = None
        self.our_x = None
        self.title = "Вычисление корней уравнений методом простых итераций"
        self.width = 1680
        self.height = 1000
        self.setStyleSheet("background-color: #FFE4C4;")
        self.setWindowTitle(self.title)
        self.setFixedSize(self.width, self.height)
        self.__size_x = (1920 - self.width) // 2
        self.move(self.__size_x, 0)

        # создание группы кнопок
        self.group_box_button = QGroupBox(self)
        self.group_box_button.setGeometry(1300, 420, 351, 146)

        # создание кнопки: «Построить график»
        self.button_graphic = QPushButton('Построить график', self.group_box_button)
        self.button_graphic.setGeometry(5, 5, 341, 65)
        self.button_graphic.setStyleSheet("""
            QPushButton {
        background-color: #f542d7;
        color: white;
        border-radius: 25px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
                }
            """)
        self.button_graphic.clicked.connect(self.choose_function_plot)

        # создание кнопки: «Решить уравнение»
        self.button_solve = QPushButton('Решить уравнение', self.group_box_button)
        self.button_solve.setGeometry(5, 75, 341, 65)
        self.button_solve.setStyleSheet("""
            QPushButton {
        background-color: #42f545;
        color: white;
        border-radius: 25px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
                }
            """)
        self.button_solve.clicked.connect(self.choose_function_solve)

        # создание групового блока с Параметрами
        self.group_box = QGroupBox("Параметры", self)
        self.group_box.setGeometry(950, 75, 330, 491)

        # создание стиля для групового блока с Параметрами
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setItalic(True)
        self.group_box.setFont(font)

        # создание стиля надписей в груповом блоке
        font_info = QFont()
        font_info.setFamily("Arial")
        font_info.setPointSize(14)
        font_info.setBold(True)

        # создание стиля ввода текста в груповом блоке
        font_help = QFont()
        font_help.setPointSize(10)

        # создание 1-го ввода текста в груповом блоке
        self.text_edit1 = QTextEdit(self.group_box)
        self.text_edit1.setGeometry(180, 40, 123, 61)
        self.text_edit1.setPlaceholderText("Введите функцию")
        self.text_edit1.setStyleSheet("background: white;")
        self.text_edit1.setReadOnly(True)
        self.text_edit1.setFont(font_help)

        # надпись для ввода 1-го текста
        self.label1 = QLabel("f(x) = ", self.group_box)
        self.label1.setGeometry(20, 40, 131, 61)
        self.label1.setFont(font_info)

        # создание 2-го ввода текста в груповом блоке
        self.text_edit2 = QTextEdit(self.group_box)
        self.text_edit2.setGeometry(180, 130, 123, 61)
        self.text_edit2.setPlaceholderText("Введите Xmin")
        self.text_edit2.setStyleSheet("background: white;")
        self.text_edit2.setFont(font_help)

        # надпись для ввода 2-го текста
        self.label2 = QLabel("Левая\nграница", self.group_box)
        self.label2.setGeometry(20, 130, 131, 61)
        self.label2.setFont(font_info)

        # создание 3-го ввода текста в груповом блоке
        self.text_edit3 = QTextEdit(self.group_box)
        self.text_edit3.setGeometry(180, 220, 123, 61)
        self.text_edit3.setPlaceholderText("Введите Xmax")
        self.text_edit3.setStyleSheet("background: white;")
        self.text_edit3.setFont(font_help)

        # надпись для ввода 3-го текста
        self.label3 = QLabel("Правая\nграница", self.group_box)
        self.label3.setGeometry(20, 220, 131, 61)
        self.label3.setFont(font_info)

        # создание 4-го ввода текста в груповом блоке
        self.text_edit4 = QTextEdit(self.group_box)
        self.text_edit4.setGeometry(180, 310, 123, 61)
        self.text_edit4.setPlaceholderText("Введите ε = ")
        self.text_edit4.setStyleSheet("background: white;")
        self.text_edit4.setFont(font_help)

        # надпись для ввода 4-го текста
        self.label4 = QLabel("Точность", self.group_box)
        self.label4.setGeometry(20, 310, 131, 61)
        self.label4.setFont(font_info)

        # создание 5-го ввода текста в груповом блоке
        self.text_edit5 = QTextEdit(self.group_box)
        self.text_edit5.setGeometry(180, 400, 123, 61)
        self.text_edit5.setStyleSheet("background: white;")
        self.text_edit5.setPlaceholderText("Введите\nкорень = ")
        self.text_edit5.setFont(font_help)

        # надпись для ввода 5-го текста
        self.label5 = QLabel("Выбранный\nКорень", self.group_box)
        self.label5.setGeometry(20, 400, 141, 61)
        self.label5.setFont(font_info)

        # создание вывода результата корня уравнения
        self.text_root_output = QTextEdit(self)
        self.text_root_output.setGeometry(950, 580, 700, 380)
        self.text_root_output.setStyleSheet("background: white;")
        self.text_root_output.setFontPointSize(14)
        self.text_root_output.setReadOnly(True)

        # групп бокс для радиобатоон
        self.group_box_radio_button = QGroupBox("Выбор функции", self)
        self.group_box_radio_button.setGeometry(1300, 75, 351, 341)

        # создание стиля для кнопки выбора
        font_rb = QFont()
        font_rb.setFamily("Arial")
        font_rb.setPointSize(15)
        font_rb.setItalic(True)

        # создание группового блока с кнопками выбора
        self.group_box_radio_button.setFont(font_rb)
        self.layout_radio_button = QVBoxLayout(self.group_box_radio_button)

        self.radio_button1 = QRadioButton("x^3+2x+5", self)

        self.layout_radio_button.addWidget(self.radio_button1)
        self.radio_button1.clicked.connect(self.add_function1)

        self.radio_button2 = QRadioButton("e^(-x)-x^2", self)
        self.layout_radio_button.addWidget(self.radio_button2)
        self.radio_button2.clicked.connect(self.add_function2)

        self.radio_button3 = QRadioButton("x-2+sin(x)", self)
        self.layout_radio_button.addWidget(self.radio_button3)
        self.radio_button3.clicked.connect(self.add_function3)

        self.radio_button4 = QRadioButton("3x^3+5x-2", self)
        self.layout_radio_button.addWidget(self.radio_button4)
        self.radio_button4.clicked.connect(self.add_function4)

        self.radio_button5 = QRadioButton("2ln(x)+sin(x)", self)
        self.layout_radio_button.addWidget(self.radio_button5)
        self.radio_button5.clicked.connect(self.add_function5)

        # добавление копок выбора в группу
        self.group_radiobutton = QButtonGroup(self)
        self.group_radiobutton.addButton(self.radio_button1)
        self.group_radiobutton.addButton(self.radio_button2)
        self.group_radiobutton.addButton(self.radio_button3)
        self.group_radiobutton.addButton(self.radio_button4)
        self.group_radiobutton.addButton(self.radio_button5)

        for button in [self.radio_button1, self.radio_button2, self.radio_button3, self.radio_button4,
                       self.radio_button5]:
            button.setStyleSheet(
                "QRadioButton {"
                "   background-color: #F0F0F0;"
                "   color: #000000;"
                "   border: 2px solid #000000;"
                "   border-radius: 10px;"
                "   padding: 5px;"
                "   font-family: Arial;"
                "   font-size: 50px;"
                "}"
                "QRadioButton:checked {"
                "   background-color: green;"
                "   color: #FFFFFF;"
                "}"
                "QRadioButton::indicator"
                "{"
                "width : 20px;"
                "height : 20px;"
                "}"
            )

        # создание окна вывода графика
        self.label_graphic = QLabel(self)
        self.label_graphic.setGeometry(10, 30, 921, 940)

        # создание меню
        self.menubar = self.menuBar()
        font = self.menubar.font()
        font.setPointSize(15)
        self.menubar.setFont(font)

        self.menu_file = self.menubar.addMenu('Файл')
        self.exit_action = QAction('Закрыть', self.menu_file)
        self.exit_action.triggered.connect(lambda: self.close())

        self.plot_graphic = QAction('Построить график', self.menu_file)
        self.plot_graphic.triggered.connect(self.choose_function_plot)

        self.clear_graphic = QAction('Очистить график', self.menu_file)
        self.clear_graphic.triggered.connect(self.clear_graph)
        self.clear_radio_button = QAction('Очистить выбор кнопки', self.menu_file)
        self.clear_radio_button.triggered.connect(self.clear_radiobutton)
        self.clear_text_parametr = QAction('Очистить введёные параметры', self.menu_file)
        self.clear_text_parametr.triggered.connect(self.clear_parameter)
        self.clear_text_main = QAction('Очистить текст решения', self.menu_file)
        self.clear_text_main.triggered.connect(self.text_root_output.clear)

        self.clear_all_full = QAction('Очистить всё', self.menu_file)
        self.clear_all_full.triggered.connect(self.clear_graph)
        self.clear_all_full.triggered.connect(self.clear_parameter)
        self.clear_all_full.triggered.connect(self.clear_radiobutton)
        self.clear_all_full.triggered.connect(self.text_root_output.clear)

        self.menu_information = self.menubar.addMenu('Справка')
        self.menu_author = QAction('Об авторе', self.menu_information)
        self.menu_author.triggered.connect(self.button_about_author)
        self.menu_program = QAction("О программе", self.menu_information)
        self.menu_program.triggered.connect(self.button_about_program)
        self.menu_program.setFont(font)
        self.menu_author.setFont(font)
        self.menu_information.addAction(self.menu_program)
        self.menu_information.addAction(self.menu_author)

        self.help_window = self.menubar.addMenu('Помощь')
        self.window_instruction = QAction('Инструкция', self)
        self.window_instruction.triggered.connect(self.button_help_window)
        self.help_window.addAction(self.window_instruction)

        # добаввление стиля для меню
        self.exit_action.setFont(font)
        self.plot_graphic.setFont(font)
        self.clear_graphic.setFont(font)
        self.window_instruction.setFont(font)
        self.clear_radio_button.setFont(font)
        self.clear_text_parametr.setFont(font)
        self.clear_text_main.setFont(font)
        self.clear_all_full.setFont(font)

        # добавление всех действий в меню
        self.menu_file.addAction(self.plot_graphic)
        self.menu_file.addAction(self.clear_graphic)
        self.menu_file.addAction(self.clear_radio_button)
        self.menu_file.addAction(self.clear_text_parametr)
        self.menu_file.addAction(self.clear_text_main)
        self.menu_file.addAction(self.clear_all_full)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.exit_action)

        self.plot_start_graphic()

    # функция выбора уравнения и её построение с окном ошибки
    def choose_function_plot(self):
        try:
            self.x_min = float(self.text_edit2.toPlainText())
            self.x_max = float(self.text_edit3.toPlainText())
            if self.radio_button1.isChecked():
                self.plot_function(self.x_min, self.x_max, lambda x: x ** 3 + 2 * x + 5)
            elif self.radio_button2.isChecked():
                self.plot_function(self.x_min, self.x_max, lambda x: np.exp(-x) - x ** 2)
            elif self.radio_button3.isChecked():
                self.plot_function(self.x_min, self.x_max, lambda x: x - 2 + np.sin(x))
            elif self.radio_button4.isChecked():
                self.plot_function(self.x_min, self.x_max, lambda x: 3 * x ** 3 + 5 * x - 2)
            elif self.radio_button5.isChecked():
                if self.x_min <= 0:
                    self.x_min = 1e-25
                self.plot_function(self.x_min, self.x_max, lambda x: 2 * np.log(x) + np.sin(x))
            else:
                raise ValueError()

        except ValueError:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Выберите функцию и введите \n   правильные параметры!!!")
            font_error = QFont()
            font_error.setPointSize(12)
            font_error.setFamily("Arial")
            msg_box.setFont(font_error)
            msg_box.exec_()

    # функция для решения выбранного уравнения с окном ошибки
    def choose_function_solve(self):
        try:
            self.eps = float(self.text_edit4.toPlainText())
            self.our_x = float(self.text_edit5.toPlainText())
            self.text_root_output.clear()
            if self.radio_button1.isChecked():
                if not (-2.5 <= self.our_x <= 5):
                    raise ValueError()
                self.simple_iteration(self.our_x, self.eps, lambda x: -(2 * x + 5) ** (1 / 3))
            elif self.radio_button2.isChecked():
                self.simple_iteration(self.our_x, self.eps, lambda x: np.sqrt(np.exp(-x)))
            elif self.radio_button3.isChecked():
                self.simple_iteration(self.our_x, self.eps, lambda x: 2 - np.sin(x))
            elif self.radio_button4.isChecked():
                if not (-1 <= self.our_x <= 1.3):
                    raise ValueError()
                self.simple_iteration(self.our_x, self.eps, lambda x: (2 - 3 * x ** 3) / 5)
            elif self.radio_button5.isChecked():
                if self.our_x <= 0:
                    raise ValueError()
                self.simple_iteration(self.our_x, self.eps, lambda x: np.exp(-np.sin(x) / 2) if x > 0 else np.nan)

        except ValueError:
            msg_box = QMessageBox(self)
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Ошибка")
            msg_box.setText("Выберите функцию и введите \n   правильно параметры!!!")
            font_error = QFont()
            font_error.setPointSize(12)
            font_error.setFamily("Arial")
            msg_box.setFont(font_error)
            msg_box.exec_()

    # построение начального графика
    def plot_start_graphic(self):
        self.figure = plt.figure(figsize=(12, 9), dpi=85)
        self.ax = self.figure.add_subplot(111)
        self.ax.set_xlim([-10, 10])
        self.ax.set_ylim([-5, 5])
        self.ax.axhline(y=0, color='#000000')
        self.ax.axvline(x=0, color='#000000')
        self.ax.set_xlabel('X', fontsize=15, fontweight='bold')
        self.ax.set_ylabel('Y', fontsize=15, fontweight='bold')
        self.ax.plot(0, 0, 'ko')
        self.ax.text(0, 0, 'O(0,0)', color='black', fontsize=16, verticalalignment='bottom')
        self.ax.grid(True)
        self.figure.tight_layout(pad=1)

        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.label_graphic)

        vbox = QVBoxLayout()
        vbox.addWidget(self.toolbar)
        vbox.addWidget(self.canvas)
        self.label_graphic.setLayout(vbox)

    # функция вычисления корней уравнений методом простых итераций
    def simple_iteration(self, x, eps, function):
        rez = function(x)
        iter_count = 0

        if hasattr(self, 'point_text') and self.point_text is not None:
            self.point_text.remove()

        if hasattr(self, 'point_plot') and self.point_plot is not None:
            self.point_plot.remove()

        while abs(rez - x) > eps:
            rez = x
            x = function(x)
            self.text_root_output.insertPlainText(f"№{iter_count + 1}. Корень уравнения равен: {x}\n")
            iter_count += 1

        self.text_root_output.insertPlainText(f"Ответ: {x}.\nКоличество произведенных итераций: {iter_count}\n")
        self.point_plot = self.ax.plot(x, 0, 'ro')[0]
        self.point_text = self.ax.text(x, 0, f'A({x:.3f},0)', color='red', fontsize=16, verticalalignment='bottom')
        self.canvas.draw()

        return x

    # функция построения графика
    def plot_function(self, x_min, x_max, function):
        self.clear_graph()
        self.ax.axvline(x=x_min, color='red', linestyle='dashed')
        self.ax.axvline(x=x_max, color='red', linestyle='dashed')
        self.ax.set_xlabel('X', fontsize=15, fontweight='bold')
        self.ax.set_ylabel('Y', fontsize=15, fontweight='bold')
        x = np.linspace(x_min, x_max, 5000)
        y = function(x)

        self.ax.autoscale()
        self.ax.plot(x, y)
        self.canvas.draw()

    # функция очистки графика
    def clear_graph(self):
        self.ax.clear()
        self.ax.axhline(y=0, color='#000000')
        self.ax.axvline(x=0, color='#000000')
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.plot(0, 0, 'ko')
        self.ax.text(0, 0, 'O(0,0)', color='black', fontsize=16, verticalalignment='bottom')
        self.ax.grid(True)
        self.ax.set_xlim([-10, 10])
        self.ax.set_ylim([-5, 5])
        self.canvas.draw()

    # функция очистки кнопок выбора
    def clear_radiobutton(self):
        self.group_radiobutton.setExclusive(False)
        self.radio_button1.setChecked(False)
        self.radio_button2.setChecked(False)
        self.radio_button3.setChecked(False)
        self.radio_button4.setChecked(False)
        self.radio_button5.setChecked(False)
        self.group_radiobutton.setExclusive(True)

    # функция очистки параметров
    def clear_parameter(self):
        self.text_edit1.clear()
        self.text_edit2.clear()
        self.text_edit3.clear()
        self.text_edit4.clear()
        self.text_edit5.clear()
        self.text_edit5.clear()

    # функция добавления уравнения в 1-й текст
    def add_function1(self):
        self.text_edit1.clear()
        self.text_edit1.append("x^3-2x+3")

    # функция добавления уравнения в 2-й текст
    def add_function2(self):
        self.text_edit1.clear()
        self.text_edit1.append("e^(-x)-x^2")

    # функция добавления уравнения в 3-й текст
    def add_function3(self):
        self.text_edit1.clear()
        self.text_edit1.append("x-2+sin(1/x)")

    # функция добавления уравнения в 4-й текст
    def add_function4(self):
        self.text_edit1.clear()
        self.text_edit1.append("3x^3+5x-2")

    # функция добавления уравнения в 5-й текст
    def add_function5(self):
        self.text_edit1.clear()
        self.text_edit1.append("2ln(x)+sin(x)")

    # функция открывания окна об авторе
    def button_about_author(self):
        self.new_window = AboutAuthor.AboutAuthor()
        self.new_window.setWindowModality(Qt.ApplicationModal)
        self.new_window.show()

    # функция открывания окна с инструкцией
    def button_help_window(self):
        self.new_window = HelpWindow.HelpWindow()
        self.new_window.setWindowModality(Qt.ApplicationModal)
        self.new_window.show()

    # функция открывания окна об программе
    def button_about_program(self):
        self.new_window = AboutProgram.AboutProgram()
        self.new_window.setWindowModality(Qt.ApplicationModal)
        self.new_window.show()
