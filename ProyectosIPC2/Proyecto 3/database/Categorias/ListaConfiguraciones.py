
from database.Database import database
class list_configuracion():
    def __init__(self,_ID,_nombre,_descripcion) -> None:
        self.__ID = _ID
        self.__nombre = _nombre
        self.__descripcion = _descripcion
        self.__list_recursos_configuracion = database()
        pass
    def insert_recursos_configuracion(self,dato):
        self.__list_recursos_configuracion.insert_element(dato)
    def Get_ID(self):
        return self.__ID
    def Get_list_recursos_configuracion(self):
        return self.__list_recursos_configuracion
    def Getting_all_the_data_JSON(self):
        dic = {
            "ID": self.__ID,
            "Nombre": self.__nombre,
            "Descripcion": self.__descripcion,
            "lista_recursos": []
        }
        return dic
    