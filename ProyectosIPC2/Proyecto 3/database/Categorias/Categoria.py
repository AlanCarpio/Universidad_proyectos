from database.Database import database
class categoria():
    def __init__(self,_ID,_nombre,_abreviatura,_cargaTrabajo) -> None:
        self.__ID = _ID
        self.__nombre = _nombre
        self.__abreviatura = _abreviatura
        self.__cargaTrabajo = _cargaTrabajo
        self.__list_configuracion = database()
        pass
    def insert_configuracion(self,dato):
        self.__list_configuracion.insert_element(dato)
    def Get_ID(self):
        return self.__ID
    def Get_list_configuracion(self):
        return self.__list_configuracion
    def Getting_all_the_data_JSON(self):
        dic = {
            "ID": self.__ID,
            "Nombre": self.__nombre,
            "Abreviatura": self.__abreviatura,
            "CargaTrabajo": self.__cargaTrabajo,
            "lista_configuracion": [],
        }
        return dic