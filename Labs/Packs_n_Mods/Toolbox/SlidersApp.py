from PyQt5.QtWidgets import QWidget, QSlider, QGridLayout, QLabel
from PyQt5.Qt import Qt
from Diagram.DrawDiagram import DrawDiagram


class SlidersApp(QWidget):
    def __init__(self, chart_panel, data, list_of_buttons, parent=None):
        super().__init__(parent)

        self.__chart = chart_panel
        self.__buttons = list_of_buttons
        self.__data = data
        self.__min_val = self.__get_index_values()[0]
        self.__max_val = self.__get_index_values()[-1]

        self.__validate_args(self.__min_val, self.__max_val)
        # self.__width_height = width_height

        self.__create_view(self.__get_data()[0], self.__get_data()[-1])

    def __get_data(self):
        return self.__data

    def __get_index_values(self):
        data = self.__get_data()
        index = []
        for count, value in enumerate(data):
            index.append(count)
        return index

    def get_curr_dates_range(self):
        up_list = []
        i = 0
        for date in self.__get_data():
            if i == 1:
                up_list.append(date)
                if self.__get_values()[0] == date:
                    i -= 1

            if i == 0:
                if self.__get_values()[1] == date:
                    up_list.append(date)
                    i += 1

        return up_list

    def __get_values(self):
        values = self.__top_slider.value(), self.__bottom_slider.value()
        return values

    def __validate_args(self, min_val, max_val):
        if min_val >= max_val:
            raise Exception("Incorrect initial value of DoubleSlider (max_val cannot be lower or equal to min_val).")

    def __create_view(self, min_val, max_val):
        self.__top_slider = self.__create_top_slider()
        self.__top_slider_position = (0, 0)
        self.__bottom_slider = self.__create_bottom_slider()
        self.label = QLabel(str(f'Od: {min_val}'), self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignRight)
        self.label2 = QLabel(str(f'Do: {max_val}'), self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignRight)

        layout = QGridLayout()
        layout.setSpacing(5)
        layout.addWidget(self.__top_slider, 0, 0)
        layout.addWidget(self.__bottom_slider, 1, 0)
        layout.addWidget(self.label, 0, 1)
        layout.addWidget(self.label2, 1, 1)

        # self.setMinimumWidth(self.__width_height)
        # self.setMaximumWidth(self.__width_height)
        # self.setMaximumHeight(self.__width_height)

        self.setLayout(layout)

    def __create_top_slider(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val)
        slider.setMaximum(self.__max_val - 1)

        slider.setValue(self.__min_val)
        slider.valueChanged.connect(self.__handle_top_change)
        slider.valueChanged.connect(self.__update_label)

        return slider

    def __create_bottom_slider(self):
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(self.__min_val + 1)
        slider.setMaximum(self.__max_val)

        slider.setValue(self.__max_val)
        slider.valueChanged.connect(self.__handle_bottom_change)
        slider.valueChanged.connect(self.__update_label2)
        # slider.valueChanged.connect(DrawDiagram.erase_old_diagram)

        return slider

    def __handle_top_change(self):
        left_value = self.__top_slider.value()
        right_value = self.__bottom_slider.value()

        # wywołanie metody wykresu zwracająca początek przedziału czasu dla wykresu
        self.__chart.get_start(left_value)
        # wywołanie metody panelu przycisku która została opisana w pliku list_of_countries.py
        self.__buttons.changing_boundaries()

        if left_value >= right_value:
            self.__bottom_slider.setValue(left_value + 1)

        return left_value

    def __handle_bottom_change(self):
        left_value = self.__top_slider.value()
        right_value = self.__bottom_slider.value()

        if right_value <= left_value:
            self.__top_slider.setValue(right_value - 1)

        # metoda wykresu która zwraca koniec przedziłu dla wykresu
        self.__chart.get_end(right_value)
        # metoda listy przycisków która po przesunieciu slidera zaktualizuje pole wykresu
        self.__buttons.changing_boundaries()
        return right_value

    def __update_label(self, value):

        self.label.setText(str(f'Od: {self.__get_data()[value]}'))

    def __update_label2(self, value):

        self.label2.setText(str(f'Do: {self.__get_data()[value]}'))
