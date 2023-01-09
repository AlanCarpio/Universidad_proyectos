class Automata():
    def __init__(self,Nombre,Alfabeto,SimbolosPila,Estados,EstadoInicial,EstadoAcepta,Transiciones:list) -> None:
        self.__Nombre = Nombre
        self.__Alfabeto = Alfabeto
        self.__SimbolosPila = SimbolosPila
        self.__Estados = Estados
        self.__EstadoInicial =EstadoInicial
        self.__EstadoAcepta = EstadoAcepta
        self.__Transiciones = Transiciones    
        pass
    def Get_info(self):
        return(self.__Nombre, #0
                self.__Alfabeto,#1
                self.__SimbolosPila,#2
                self.__Estados,#3
                self.__EstadoInicial,#4
                self.__EstadoAcepta,#5
                self.__Transiciones,)#6