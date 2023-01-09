import re
class instancias():
    def __init__(self,_ID,_ID_configuracion,_nombre,_fecha_inicial,_estado,_fecha_final) -> None:
        self.__ID = _ID
        self.__ID_configuracion = _ID_configuracion
        self.__nombre = _nombre
        self.__fecha_inicial = _fecha_inicial
        self.__estado = _estado
        self.__fecha_final = _fecha_final
        pass
    def Getting_all_the_data_JSON(self):
        dic = {
            "ID": self.__ID,
            "ID_configuracion": self.__ID_configuracion,
            "Nombre": self.__nombre,
            "Fecha_inicial": self.__fecha_inicial,
            "Estado": self.__estado,
            "Fecha_final": self.__fecha_final,
        }
        return dic
    def Get_ID(self):
        return self.__ID
    def Get_estado(self):
        return self.__estado
    def Set_estado(self,estado):
        self.__estado = estado
    def Set_fecha_final(self,fecha):
        self.__fecha_final = fecha
    def Get_fecha_final(self):
        resulfecha = re.sub("-","/",self.__fecha_final)
        resulfecha = resulfecha.split('/')
        resulfecha = resulfecha[2]+resulfecha[1]+resulfecha[0]
        return int(resulfecha)
    def Get_ID_configuracion(self):
        return self.__ID_configuracion