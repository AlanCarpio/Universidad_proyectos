class consumo():
    def __init__(self,_nit_cliente,_id_instancia,__tiempo,__fecha_hora):
        self.__nit_cliente = _nit_cliente
        self.__id_instancia = _id_instancia
        self.__tiempo = __tiempo
        self.__fecha_hora = __fecha_hora
        pass
    def Getting_all_the_data_JSON(self):
        dic = {
            "NIT_Cliente": self.__nit_cliente,
            "ID_instancia": self.__id_instancia,
            "Tiempo": self.__tiempo,
            "Fecha_hora": self.__fecha_hora,
        }
        return dic 
    def Get_fecha(self):
        fecha_hora = self.__fecha_hora.split("-")
        fecha_hora = fecha_hora[0]+fecha_hora[1]+fecha_hora[2]
        return int(fecha_hora)
    def Get_NIT_Cliente(self):
        return self.__nit_cliente
    def Get_ID_instancia(self):
        return self.__id_instancia
    def Get_tiempo(self):
        return float(self.__tiempo)