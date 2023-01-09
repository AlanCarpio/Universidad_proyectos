class Transicion:
    def __init__(self,_entrada,_estado,_destino) -> None:
        self.__entrada = _entrada
        self.__estado = _estado
        self.__destino = _destino
        pass
    def Get__transicion(self):
        return "{}  {}  {}".format(self.__entrada,self.__estado,self.__destino)
    def Get_entrada(self):
        return self.__entrada
    def Get_estado(self):
        return self.__estado
    def Get_destino(self):
        return self.__destino