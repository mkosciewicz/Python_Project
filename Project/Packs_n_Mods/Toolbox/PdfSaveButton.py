import os
import sys
from PyQt5.QtWidgets import QPushButton, QFileDialog
from reportlab.lib.utils import ImageReader
from Toolbox.PdfGenerator import PdfGenerator


# klasa odpowiedzialna za stworzenie przycsku do stworzenia pdfa z wykresem
class PdfSaveButton(QPushButton):
    def __init__(self, name, chart):
        super().__init__(name)
        self.__chart = chart

        # wywołanie klasy genrującej plik pdf
        self.__pdf_generator = PdfGenerator()
        self.clicked.connect(self.__save_btn_action)

    # metoda pobierająca obecny stan wykresu i przetwarzająca go na obraz
    def __save_btn_action(self):
        # wywołanie metody z klasy CreateChart zwracjaca wykres
        img_data = self.__chart.get_img()
        # wywołanie klasy odpwoiadza za przekształcenie go w obraz
        img = ImageReader(img_data)

        # wywołanie metody odpowiedzialnej za wybranie lokalizacji pliku
        filename = self.__prepare_file_chooser()

        # sprawdzenie czy poprawnie nadano nazwę pliku, następne wygenerowanie dokumentu
        if filename:
            self.__pdf_generator.create_and_save_report(img, filename)
        else:
            pass

    #  metoda która otwieira okno do wybrania lokalizacji i zwraca nazwę pliku nadaną przez użytkownika
    def __prepare_file_chooser(self):
        parent = None
        current_dir = os.path.dirname(sys.argv[0])
        filename, _ = QFileDialog.getSaveFileName(parent, "Save PDF report", current_dir, filter="PDF (*.pdf)")
        return filename
