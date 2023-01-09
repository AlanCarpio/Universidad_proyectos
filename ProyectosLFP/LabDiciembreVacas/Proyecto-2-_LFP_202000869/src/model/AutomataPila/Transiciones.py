class Transiciones():
    def __init__(self,Entrada,Destino,Estados:list) -> None:
        self.__Entrada = Entrada
        self.__Destino = Destino
        self.__Estados = Estados
        pass
    def Get_Transiciones(self):
        return "{} {} {} {} {}".format(self.__Entrada,self.__Estados[0],self.__Estados[1],self.__Destino,self.__Estados[2])
    def Get_All(self):
        return (self.__Entrada,self.__Destino,self.__Estados)
    