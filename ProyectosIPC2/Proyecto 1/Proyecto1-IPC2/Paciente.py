
class paciente(object):
    def __init__(self,_Nombre,_Edad,_Periodo,_m,_lista) -> None:
        self.__Nombre = _Nombre
        self.__Edad = _Edad
        self.__Periodo = _Periodo
        self.__m = _m
        self.__lista = _lista
        self.__contador_periodo = 0
        self.__n = 0
        self.__n1 = 0
        self.__estado = ""
        self.__imprimir = 0
        pass
    def get_lista(self):
        return self.__lista
    def get_m(self):
        return int(self.__m)
    def insertar_lista(self,lista):
        self.__lista.append(lista)
    def get_nombre(self):
        return self.__Nombre
    def get_edad(self):
        return self.__Edad
    def get_periodo(self):
        return self.__Periodo
    def get_rejilla(self):
        return self.__m
    def aumentar_contador(self,number):
        self.__contador_periodo+=number
    def get_contador(self):
        return self.__contador_periodo
    #==================================
    def set_imprimir(self):
        self.__imprimir = 1
    def get_imprimir(self):
        return self.__imprimir    
    #==================================    
    def set_n(self,n):
        self.__n =  n
    def set_n1(self,n1):
        self.__n1 =  n1
    def set_estado(self,estado):
        self.__estado =  estado
    def get_n(self):
        return self.__n 
    def get_n1(self):
        return self.__n1 
    def get_estado(self):
        return self.__estado            
        