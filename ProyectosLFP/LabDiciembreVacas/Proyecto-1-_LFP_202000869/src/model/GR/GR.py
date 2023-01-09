from src.model.database import database
from src.model.GR.Produccion import Produccion
class GR():
    def __init__(self,_Nombre,_Estados,_Alfabeto,_Estado_inicial,_Estado_Aceptacion,list_data:list) -> None:
        self.__Nombre = _Nombre
        self.__Estados = _Estados
        self.__Alfabeto = _Alfabeto
        self.__Estado_inicial = _Estado_inicial
        self.__Estado_Aceptacion = _Estado_Aceptacion
        self.__Transiciones = list_data
        pass
    def Get_transiciones(self):
        return self.__Transiciones
    def Get__Nombre(self):
        return self.__Nombre
    def Get__Estados(self):
        return self.__Estados
    def Get__Alfabeto(self):
        return self.__Alfabeto
    def Get__Estado_inicial(self):
        return self.__Estado_inicial
    def Get__Estado_Aceptacion(self):
        return self.__Estado_Aceptacion