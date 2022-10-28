from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen.canvas import Canvas


class PdfGenerator:
    # Konstruktor tworzący zmienną autora oraz tytuł
    def __init__(self):
        self.list = None
        self.__author = "author"
        self.__title = f"Project ({date.today()})"

    def create_and_save_report(self, img, filepath, pagesize=A4):
        pdf_template = self.__create_pdf_template(filepath, img, pagesize)
        pdf_template.setAuthor(self.__author)
        pdf_template.setTitle(self.__title)
        pdf_template.save()

    # Metoda tworząca zawartosc pliku pdf: tytuł oraz wykres cen
    def __create_pdf_template(self, filepath, img, pagesize):
        canvas = Canvas(filepath, pagesize=pagesize)
        canvas.setFont("Times-Roman", 24)
        title = "Diagram of the Energy Cost"
        # Dostosowanie dystansu między tytułem oraz wykresem
        title_magic_offset, img_magic_offset = 100, 775
        title_x, title_y = A4[0] / 2, A4[1] - title_magic_offset
        img_x, img_y = 0, A4[1] - img_magic_offset
        # Narysowanie napisu tytułowego oraz obrazu wykresu
        canvas.drawCentredString(title_x, title_y, title)
        canvas.drawImage(img, img_x, img_y, width=A4[0]-20, height=A4[1]-20, preserveAspectRatio=True)
        return canvas

    def get_list(self, list):
        self.list = list
