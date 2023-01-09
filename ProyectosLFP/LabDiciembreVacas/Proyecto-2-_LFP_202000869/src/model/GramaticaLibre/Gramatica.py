class Gramatica():
    def __init__(self,nombre,no_terminales,terminales,nti,producciones:list) -> None:
        self.__nombre = nombre
        self.__no_terminales = no_terminales
        self.__terminales = terminales
        self.__nti = nti
        self.__producciones = producciones
        pass
    def Get_DatosGramatica(self):
        return (self.__nombre,self.__no_terminales,self.__terminales,self.__nti,self.__producciones)
        
    