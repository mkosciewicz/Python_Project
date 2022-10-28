import random
from PIL import Image, ImageDraw
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Toolbox.ImportData import *


# klasa tworząca obiekt przycisku
class SelectButton(QPushButton):
    def __init__(self, country_name, color, panel_4_diagram, filepath, buttons_list):
        super().__init__(country_name)
        self.__color = color
        self.country_name = country_name
        self.__panel_4_diagram = panel_4_diagram
        self.__seek_offset = 0
        self.__buttons_list = buttons_list
        self.__file = ImportData(filepath)
        self.__country = Country(country_name, self.__file)

        # Add diagram
        self.clicked.connect(self.refresh_diagram)

    # metoda dodająca wykres do obszaru
    def refresh_diagram(self):
        name = self.text()
        # sprawdzenie seek_offsetu w celu dodania/usiunięcia wykresu i ikony
        if self.__seek_offset == 0:
            # wywołanie metody dodającej ikonę do przycisku
            self.__create_and_add_icon_to_btn()
            self.__seek_offset = 1
            # wywołanie metody aktualizującej wykres
            self.__panel_4_diagram.add_data_for_chart(name, self.__country.provide_countries_all_data(),
                                                      self.__file.get_dates(),
                                                      self.__color)

        elif self.__seek_offset == 1:
            self.__create_and_add_icon_to_btn()
            self.__seek_offset = 0
            self.__buttons_list.erase_diagram()

    # metoda służącą do udpatowania wykresu, mianowicie ona dostaje listę przycisków które są kliknięte i
    # dodaje dla nich wykres
    def refresh_diagram_backup(self):
        name = self.text()
        self.__panel_4_diagram.add_data_for_chart(name, self.__country.provide_countries_all_data(),
                                                  self.__file.get_dates(), self.__color)

    # metoda zwracająca seek_offsety
    def get_seek_offset(self):
        return self.__seek_offset

    # metoda sprawdzająca seek_offset, która nastepnie dodaje lub usuwa ikonę
    def __create_and_add_icon_to_btn(self, width=40, height=5):
        if self.__seek_offset == 0:
            shape = ((0, 0), (width - 1, height - 1))
            rectangle = Image.new("RGBA", (width, height))
            rectangle_img = ImageDraw.Draw(rectangle)
            rectangle_img.rectangle(shape, fill=self.__color)
            rectangle_qt = ImageQt(rectangle)
            rectangle_pixmap = QPixmap.fromImage(rectangle_qt)
            rectangle_icon = QIcon(rectangle_pixmap)
            self.setIcon(rectangle_icon)
        else:
            shape = ((0, 0), (width - 1, height - 1))
            rectangle = Image.new("RGBA", (width, height))
            rectangle_img = ImageDraw.Draw(rectangle)
            rectangle_img.rectangle(shape, fill=self.__color)
            rectangle_qt = ImageQt(rectangle)
            rectangle_pixmap = QPixmap.fromImage(rectangle_qt)
            rectangle_icon = QIcon(None)
            self.setIcon(rectangle_icon)


# klasa tworzaca liste przycisków
class CountriesButtons(QGroupBox):
    __COLORS = ["blue", "green", "red", "magenta", "black"]

    def __init__(self, panel_4_diagram, filepath):
        super().__init__()
        self.__panel_4_diagram = panel_4_diagram
        self.__filepath = filepath
        # stworznie pustej listy na przyciski
        self.__buttons = []

        # wywpołanie klasy odczytującej dane z pliku
        self.__file = ImportData(self.__filepath)
        self.__set_grid_4_btns()

    # metoda zwracjaca ilość ilość państw
    def __provide_countries_qntity(self):
        list_of = self.__file.get_countries()
        countries_qntity = len(list_of)
        return countries_qntity

    # metoda tworząca układ (layout) przycisków
    def __set_grid_4_btns(self):
        self.__create_button()
        layout = QFormLayout()
        groupBox = QGroupBox()

        for btn in self.__buttons:
            layout.addWidget(btn)

        groupBox.setLayout(layout)

        self.scroll = QScrollArea()
        self.scroll.setWidget(groupBox)
        self.scroll.setWidgetResizable(True)
        layout = QVBoxLayout(self)
        layout.addWidget(self.scroll)
        self.setLayout(layout)

    # metoda tworząca listę obiektów przycisków państw
    def __create_button(self):
        buttons_qntity = self.__provide_countries_qntity()

        for i in range(buttons_qntity):
            colour = self.__find_rand_color()
            # Object of country
            btn = SelectButton(self.__file.get_countries()[i], colour, self.__panel_4_diagram, self.__filepath, self)
            self.__buttons.append(btn)

    def __find_rand_color(self):
        color_id = random.randint(0, len(self.__COLORS) - 1)
        color = self.__COLORS[color_id]
        return color

    def erase_diagram(self):

        self.__panel_4_diagram.erase_old_diagram()

        for btn in self.__buttons:

            if btn.get_seek_offset() == 1:
                btn.refresh_diagram_backup()

    # poniższa metoda działa identycznie jak powyższa metoda tylko ona jest stosowana dla suwaka, chcieliśmy aby inny
    # kod był czytelniejszy do innych użytkowników
    def changing_boundaries(self):
        self.__panel_4_diagram.erase_old_diagram()
        for btn in self.__buttons:
            if btn.get_seek_offset() == 1:
                btn.refresh_diagram_backup()


# # this class is serving as display, allowing to output errors(ErrorDisplay subclass)
# # or information about selected country (CountryDisplay subclass)
# class Display(QTextEdit):
#     def __init__(self):
#         super().__init__()
#         self.setReadOnly(True)
#         self.LineWrapMode()
#         self.adjustSize()
#         self.setMaximumSize(575, 40)
#
#
# class CountryDisplay(Display):
#     def __init__(self):
#         super().__init__()
#
#
# class ErrorDisplay(Display):
#     def __init__(self):
#         super().__init__()
#         self.setStyleSheet("color: red")
