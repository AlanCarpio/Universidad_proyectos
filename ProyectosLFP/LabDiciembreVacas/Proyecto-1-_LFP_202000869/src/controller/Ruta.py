from tkinter.messagebox import showinfo
from src.model.AFD.Transicion import Transicion
import pydot
class Ruta():
    def __init__(self,nombre_focus,cadena_solicitud,data_afd,data_gr) -> None:
        self.nombre_focus = nombre_focus
        self.cadena_solicitud = cadena_solicitud
        self.data_afd = data_afd
        self.data_gr = data_gr
        
        pass
    def Ruta_grafo(self,ruta_list,list_producciones_ruta):
        
        All__ = """"""
        aceptacion = ruta_list.pop(-1)
        All__ += "{} [shape=doublecircle]\n".format(aceptacion)
        estado_inicio = """
        Inicio [shape=rarrow]
        Inicio -> {}
        """.format(ruta_list[0])
        All__ += estado_inicio
        for iter3 in ruta_list:
            if iter3 != aceptacion:
                All__ += "{} [shape=circle]\n".format(iter3)
        for iter4 in list_producciones_ruta:
            All__ += "{} -> {} [label={}]\n".format(iter4.Get_entrada(),iter4.Get_destino(),iter4.Get_estado())
        All__ = All__.strip()
        all_grafo = """
        digraph AFD {}
        layout=dot rankdir=LR shape=circle
        {}
        {}
        """.format('{',All__,"}")
        all_grafo = all_grafo.strip()
        graph = pydot.graph_from_dot_data(all_grafo)
        graph[0].write_pdf("C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-1-_LFP_202000869/Documentation/Ruta.pdf")
    def Algoritmo_Ruta(self,iter,estado_inicial,char) -> str:
        for iter2 in iter.Get_transiciones():
            if estado_inicial == iter2.Get_entrada() and char == iter2.Get_estado():
                trans = Transicion(estado_inicial,char,iter2.Get_destino())
                return (iter2.Get_destino(),trans)
        return (0,0)
    def Ruta_AFD(self):
        ruta_list = []
        list_producciones_ruta = []
        for iter in self.data_afd.Get_data():
            if iter.Get__Nombre() == self.nombre_focus:
                estado_inicial = iter.Get__Estado_inicial()
                ruta_list.append(estado_inicial)
                while len(self.cadena_solicitud) > 0:
                    char = self.cadena_solicitud[0]
                    resul = self.Algoritmo_Ruta(iter,estado_inicial,char)
                    estado_inicial = resul[0]
                    list_producciones_ruta.append(resul[1])
                    ruta_list.append(estado_inicial)
                    self.cadena_solicitud = self.cadena_solicitud[1:]
                for iter3 in iter.Get__Estado_Aceptacion().split(','):
                    if estado_inicial == iter3:
                        self.Ruta_grafo(ruta_list,list_producciones_ruta)
                        return showinfo("Notification","Cadena valida archivo PDF con la ruta Generado")
                return showinfo("Notification","Cadena invalida")

        pass
    def Ruta_GR(self,):
        ruta_list = []
        list_producciones_ruta = []
        for iter in self.data_gr.Get_data():
            if iter.Get__Nombre() == self.nombre_focus:
                estado_inicial = iter.Get__Estado_inicial()
                ruta_list.append(estado_inicial)
                while len(self.cadena_solicitud) > 0:
                    char = self.cadena_solicitud[0]
                    resul = self.Algoritmo_Ruta(iter,estado_inicial,char)
                    estado_inicial = resul[0]
                    list_producciones_ruta.append(resul[1])
                    ruta_list.append(estado_inicial)
                    self.cadena_solicitud = self.cadena_solicitud[1:]
                for iter3 in iter.Get__Estado_Aceptacion().split(','):
                    if estado_inicial == iter3:
                        self.Ruta_grafo(ruta_list,list_producciones_ruta)
                        return showinfo("Notification","Cadena valida archivo PDF con la ruta Generado")
                return showinfo("Notification","Cadena invalida")

        pass
    pass