import sys
from io import BytesIO

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class DrawDiagram(FigureCanvasQTAgg):
    __IMG_FORMAT = "png"

    def __init__(self, width=7, height=5, dpi=100):
        self.__fig = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.__fig)

        self.__axes = None
        self.__start = None
        self.__end = None

    # funkcja służąca do dodania danych do wykresu, wywołane w przycisku kraju
    def add_data_for_chart(self, x_country, price, dates, color):
        self.__dates = dates
        self.__price = price
        self.new_diagram()

        self.__fig.tight_layout()
        self.__add_plot(x_country, self.__dates, self.__price, color)

    # metoda dodająca wykres
    def __add_plot(self, x_country, dates, cost, color):

        if self.__start == None and self.__end == None:
            self.__start = self.__dates.index(self.__dates[0])
            self.__end = self.__dates.index(self.__dates[-1]) + 1

        self.xx = dates[self.__start:self.__end]
        self.yy = cost[self.__start:self.__end]

        self.new_x_axis = dates[self.__start:self.__end:2]

        self.__axes.plot(self.xx, self.yy, color, linestyle='dashed', linewidth=1,
                         marker='+', markerfacecolor='blue', markersize=4, label=x_country)
        self.__axes.legend()
        self.__axes.set_xlabel("Dates")
        self.__axes.set_ylabel("Cost of Energy")
        self.__axes.set_xticks(self.new_x_axis)
        self.__axes.grid()
        self.draw()

    def erase_old_diagram(self):
        self.__fig.clf()
        self.__axes = None
        self.new_diagram()

    def new_diagram(self):
        if self.__axes is None:
            self.__axes = self.__fig.add_subplot(111)
            self.__axes.set_title("Przebieg kosztów Energii w UE")

    # Diagram_2_img
    def get_img(self):
        img_data = BytesIO()

        self.__fig.savefig(img_data, format=self.__IMG_FORMAT)
        seek_offset = 0
        img_data.seek(seek_offset)
        return img_data

    # poniższe funkcje zwracają nam początek i koniec, wywoływane w sliderze
    def get_start(self, start):
        self.__start = start

    def get_end(self, end):
        self.__end = end + 1


# ta klasa jest niewykorzystywana niestety, ponieważ jej implementacja okazała się bardzo uciążliwa,
# zamiast niej jest metoda get_start, get_end, zostawiam w celu pokazania innej metody
# class UpdateDataFromSlider:
#     def __init__(self):
#         pass
#
#     def push_data_to_chart(self, start, end):
#         self.__start = start
#         self.__end = end
#
#         self.new_boarders = [self.__start, self.__end]
#
#     def boarder_returner(self):
#         print(self.new_boarders)
#         return self.new_boarders

# if __x_country__ == "__main__":
#     app = QApplication([])
#     pdf_app = CreateChart()
#     sys.exit(app.exec_())
