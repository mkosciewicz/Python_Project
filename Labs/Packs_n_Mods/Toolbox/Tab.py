from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget


class Tab(QWidget):
    def __init__(self, diagram, map):
        super().__init__()
        self.__diagram = diagram
        self.__map = map

        self.layout = QVBoxLayout(self)
        # Object_create
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(100, 100)

        self.tabs.addTab(self.tab1, "Wykres")
        self.tabs.addTab(self.tab2, "Map")

        self.tab1.layout = QVBoxLayout()
        # ustawienie w pierwszej karcie wykeresu
        self.tab1.layout.addWidget(self.__diagram)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout()
        # ustawienie w drugiej karcie mapy
        self.tab2.layout.addWidget(self.__map)
        self.tab2.setLayout(self.tab2.layout)
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
