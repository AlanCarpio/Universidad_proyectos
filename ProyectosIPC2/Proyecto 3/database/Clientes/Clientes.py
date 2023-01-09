from database.Database import database
class clientes():
    def __init__(self,_NIT,_Nombre,_Usuario,_Password,_Direccion,_Email) -> None:
        self.__NIT = _NIT
        self.__Nombre = _Nombre
        self.__Usuario = _Usuario
        self.__Password = _Password
        self.__Direccion = _Direccion
        self.__Email = _Email
        self.__List_instancias = database()
        self.__facturas = []
        pass
    def insert_instancia(self,dato):
        self.__List_instancias.insert_element(dato)
    def Get_NIT(self):
        return self.__NIT
    def Get_List_instancias(self):
        return self.__List_instancias.Get_database()
    def Getting_all_the_data_JSON(self):
        dic = {
            "NIT": self.__NIT,
            "Nombre": self.__Nombre,
            "Usuario": self.__Usuario,
            "Password": self.__Password,
            "Direccion": self.__Direccion,
            "Email": self.__Email,
            "Instacias" : []
        }
        return dic
    def Set_facturas(self,factura):
        self.__facturas.append(factura)
    def Get_facturas(self):
        return self.__facturas