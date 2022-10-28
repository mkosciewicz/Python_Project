import sys

# from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout  # Importing a basic class of "window"

from Map.MapApp import *
from Toolbox.ImportFile import ImportFile
from Toolbox.CountriesButtons import *
from Toolbox.ImportData import ImportData
from Toolbox.SlidersApp import SlidersApp
from Toolbox.ButtonsProvider import ButtonsProvider
from Toolbox.Tab import Tab
from Diagram.DrawDiagram import DrawDiagram


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        width = 1368
        height = 786
        self.__start_date = None
        self.__end_date = None
        # self.__rep = CountryDisplay()
        # self.__err = ErrorDisplay()
        # self.__display = None
        # self.__list_A = []
        # self.__list_B = []

        title = "Koszt Energii Elektrycznej w UE"

        # Window size
        self.resize(width, height)
        self.setWindowTitle(title)
        # self.setWindowIcon(QtGui.QIcon("lightning.jpg"))
        self.__prepare_window()

    # metoda tworząca obiekty do dodania do obszaru
    def __prepare_window(self):
        self.__name = "Choose a file"

        self.__importfile = ImportFile(self.__name)
        self.__diagram = DrawDiagram()

        self.__filepath = self.__importfile.the_choosen_one

        self.__button_panel = CountriesButtons(self.__diagram, self.__filepath)
        self.__map = MapApp("./Packs_n_Mods/Map/file4map.geojson")
        self.__map2 = MapPanel("./Packs_n_Mods/Map/file4map.geojson")
        self.__buttons = ButtonsProvider(self.__diagram, self.__map2, self.__importfile)

        og_slider_data = ImportData(self.__filepath)
        slider_data = og_slider_data.get_dates()
        self.__slider = SlidersApp(self.__diagram, slider_data, self.__button_panel)
        self.__tab = Tab(self.__diagram, self.__map)

        # wywołanie metody dodającej widgety
        self.__adding_widgets()

    def __adding_widgets(self):
        main_layout = QGridLayout()

        main_layout.addWidget(self.__tab, 0, 0, 1, 9)
        main_layout.addWidget(self.__buttons, 2, 0, 1, 9)
        main_layout.addWidget(self.__button_panel, 0, 10, 3, 2)
        main_layout.addWidget(self.__slider, 1, 0, 1, 9)

        self.setLayout(main_layout)
        self.show()

    # def refresh_view(self):
    #     self.__adding_widgets()
    #     self.__list_A.clear()
    #
    #     for country in self.__list_B:
    #         if country.get_status():
    #             self.__list_A.append(country)

    #     # checks whether map or chart is chosen and puts the correct one inside main_window chart field
    #     if self.__view == "Chart":
    #         self.show_chart()
    #         self.__pdf_button.update_pdf_data(self.__chart, self.__start_date, self.__end_date, self.__short_list)
    #     elif self.__view == "Map":
    #         self.show_map()
    #
    #     # sets correct color for map/chart button and refreshes displayed chart/map
    #     self.__chart_button.check_color()
    #     self.__map_button.check_color()
    #     self.__layout.addWidget(self.__chart, 2, 0, 14, 22)
    # # metoda służąca do dodania widgetów do obszaru


def main():
    app = QApplication([])
    main_window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
