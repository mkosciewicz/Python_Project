import pandas as pd


class ImportData:
    def __init__(self, filepath):
        self.__filepath = filepath
        # Convert":" & " " 2 "Nth"
        self.__df = pd.read_csv(self.__filepath, na_values=(":", "Nth"))
        # List of semesters
        self.__dates = list(self.__df.columns[1:])
        # List of countries
        self.__countries = self.provide_countries_list()

    def __filter_4_names(self, countries_list):
        for a in range(0, len(countries_list)):
            countries_str_len = countries_list[a].split(" ")
            if len(countries_str_len) >= 2 and countries_str_len[1][0] == "(":
                countries_list[a] = countries_str_len[0]
        return countries_list

    def provide_countries_list(self):
        header = list(self.__df.columns)
        countries = list(self.__df[header[0]])
        countries = countries[3:]
        countries = self.__filter_4_names(countries)
        return countries

    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = {k.split("__")[-1]: v for k, v in self.__dict__.items()}
        return f"({class_name}): {attrs}"

    def get_data(self):
        return self.__df

    def get_dates(self):
        return self.__dates

    def get_countries(self):
        return self.__countries


class Country:
    def __init__(self, countries_names, data):
        self.__countries_names = countries_names
        self.__data = data.get_data()
        self.__countries_list = data.get_countries()
        self.__dates_list = data.get_dates()

    def __provide_countries_qntity(self):
        countries_qntity = self.__countries_list.index(self.__countries_names) + 3
        return countries_qntity

    def __provide_dates_qntity(self, date):
        dates_qntity = self.__dates_list.index(date) + 1
        return dates_qntity

    def provide_countries_values_by_date(self, date):
        countries_qntity = self.__provide_countries_qntity()
        dates_qntity = self.__provide_dates_qntity(date)
        values_per_day = self.__data.iloc[countries_qntity, dates_qntity]
        return values_per_day

    def provide_countries_all_data(self):
        countries_qntity = self.__provide_countries_qntity()
        country_values = list(self.__data.iloc[countries_qntity])
        country_values = country_values[1:]
        country_values = self.__convert_str_to_float(country_values)
        return country_values

    def __convert_str_to_float(self, country_values):
        make_list = list()
        for elem in country_values:
            if isinstance(elem, str):
                if "," in elem:
                    elem = float(elem.replace(",", "."))
                    make_list.append(elem)
            else:
                make_list.append(elem)

        country_values = make_list
        return country_values

