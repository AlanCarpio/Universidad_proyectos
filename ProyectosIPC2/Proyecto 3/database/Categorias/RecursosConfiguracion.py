from database.Database import database
class recursos_configuracion():
    def __init__(self,_ID,_cantidad_recurso) -> None:
        self.__ID = _ID
        self.__cantidad_recurso = _cantidad_recurso
        pass
    def Getting_all_the_data_JSON(self):
        dic = {
            "ID": self.__ID,
            "Cantidad_recursos": self.__cantidad_recurso
        }
        return dic
    def Get_ID(self):
        return self.__ID
    def Get_cantidad_recurso(self):
        return float(self.__cantidad_recurso)