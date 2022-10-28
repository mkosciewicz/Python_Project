from PyQt5.QtWidgets import QGroupBox, QGridLayout
from Toolbox.PdfSaveButton import PdfSaveButton


# klasa tworząca ukłąd przycisków do wczytania pliku i eksportowania wykresu do pdfa
class ButtonsProvider(QGroupBox):
    def __init__(self, diagram, map, importfile):
        super().__init__()
        self.__diagram = diagram
        self.__map = map
        self.__importfile = importfile
        # użycie metody tworzącaj układ
        self.__prepare_buttons()

    def __prepare_buttons(self):
        self.__create_button()
        # ustawienie przycisków jako grid
        layout = QGridLayout()
        # dodanie widgetów
        layout.addLayout(self.__importfile_btn, 0, 0, 1, 1)
        layout.addWidget(self.__pdf4diagram_btn, 0, 1, 1, 1)
        layout.addWidget(self.__pdf4map_btn, 0, 2, 1, 1)

        self.setLayout(layout)

    def __create_button(self):
        # stworzenie/wywołanie obiektów dodanych do widgetu
        self.__pdf4diagram_btn = PdfSaveButton("Save DIAGRAM", self.__diagram)
        self.__pdf4map_btn = PdfSaveButton("Save MAP", self.__diagram)
        self.__importfile_btn = self.__importfile
