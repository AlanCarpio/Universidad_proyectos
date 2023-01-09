
from tkinter.messagebox import showerror
class Nodo:
    def __init__(self,_dato) -> None:
        self.dato = _dato
        self.siguiente = None
class ListaSimple:
    def __init__(self) -> None:  
        self.primero = None
        self.final = None
        self.temp = None
    def insertar_Empresa(self,empresa):
        nodo = Nodo(empresa)
        if self.primero:
            self.temp.siguiente = nodo
            self.final = nodo
            self.temp = self.final
        else:
            self.primero = nodo
            self.final = nodo
            self.temp = self.primero  
    def eliminar(self):
        temp2 = self.primero
        while temp2 != None:
            temp3 = temp2.siguiente
            self.primero = None
            temp2 = temp3
    def obtener_primer(self):
        temp = self.primero
        self.primero = self.primero.siguiente
        return temp

    #============================ Busqueda ===============================
    def busquedaescriPrueba(self,idescri,lol):
        temp = self.primero
        while temp!=None:
            if temp.dato.id == idescri:
                lol.estado = True
            temp = temp.siguiente
    def busquedaescri(self,dat):
        temp = self.primero
        while temp!=None:
            if temp.dato.get_id() == dat:
                return temp.dato.encargado
            temp = temp.siguiente
    def busquedaPunto2(self,dat):
        temp = self.primero
        while temp!=None:
            if temp.dato.get_id() == dat:
                return temp.dato.listescritorios
            temp = temp.siguiente
    def busquedaPrueba(self,dat):
        temp = self.primero
        while temp!=None:
            if temp.dato.id_empresa == dat:
                return [temp.dato.id_punto,temp.dato.listEscriActivos,temp.dato.listclientes]
            temp = temp.siguiente
        return True 
    def busquedaEmpresa(self,id_empre,id_punto,id_escri,listprueba):
        temp = self.primero
        while temp!=None:
            if temp.dato.get_id() == id_empre:
                escri_punto_empre = temp.dato.get_punto().busquedaPunto2(id_punto)
                encargado_escri = escri_punto_empre.busquedaescri(id_escri)
                print(encargado_escri)
                list_trac = temp.dato.get_trac()
            temp = temp.siguiente
        temp2 = listprueba.primero
        while temp2 != None:
            if temp2.dato.id_empresa == id_empre:
                if temp2.dato.id_punto == id_punto:
                    list_clientes = temp2.dato.listclientes
                    break
            temp2 = temp2.siguiente
        return [list_clientes,list_trac,encargado_escri]
            
