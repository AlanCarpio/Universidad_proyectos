from database.Clientes.Clientes import clientes
from database.Database import database
from database.Recursos.Recurso import recurso
from database.Consumos.Consumo import consumo
class configuracion():
    def __init__(self) -> None:
        self.__list_recursos = database()
        self.__list_categorias = database()
        self.__list_clientes = database()
        self.__list_consumos = database()
        pass
    def insert_recursos(self,dato):
        self.__list_recursos.insert_element(dato)
    def insert_categorias(self,dato):
        self.__list_categorias.insert_element(dato)
    def insert_clientes(self,dato):
        self.__list_clientes.insert_element(dato)
    def insert_consumo(self,dato):
        self.__list_consumos.insert_element(dato)
    def Get_list_clientes(self):
        return self.__list_clientes
    def Get_list_categorias(self):
        return self.__list_categorias
    def Get_list_recursos(self):
        return self.__list_recursos
    def Get_list_consumos(self):
        return self.__list_consumos