import re


class database():
    def __init__(self) -> None:
        self.__database = []
        pass
    def insert_element(self,dato):
        self.__database.append(dato)
    def extract_element(self,posicion):
        self.__database.pop(posicion)
    def empty_elements(self):
        self.__database = []
    def Get_database(self):
        return self.__database
