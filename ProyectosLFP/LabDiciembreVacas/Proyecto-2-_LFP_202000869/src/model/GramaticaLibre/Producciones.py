class Producciones:
    def __init__(self,origen,destinos:list):
        self.__origen = origen
        self.__destinos = destinos
    def Get_producciones(self):
        resul = ''
        for iter in self.__destinos:
            resul += iter + ' '
        return (self.__origen,resul)
    def Get_Origen(self):
        return self.__origen
    def Get_Destinos(self):
        return self.__destinos
    