import pydot
from tkinter import messagebox
class Generar_reporte():
    def __init__(self,data_afd,data_gr) -> None:
        self.data_afd = data_afd
        self.data_gr = data_gr
        pass
    def dat_datos_gr(self,iter):
        Transiciones = ""
        for iter_transicion in iter.Get_transiciones():
            Transiciones += "{},{},{}".format(iter_transicion.Get_entrada(),
                                                iter_transicion.Get_estado(),
                                                iter_transicion.Get_destino())
            Transiciones += "\n"
            Transiciones = Transiciones.lstrip()
        dot_datos_afd = """
        "Nombre: {Nombre}
        No terminales: {Estados}
        Terminales: {Alfabeto}
        No Terminal Inicial: {Inicial}
        Producciones:
        {Transiciones}
        "  [shape=box]
        """.format(Nombre = iter.Get__Nombre(),
                    Estados = iter.Get__Estados(),
                    Alfabeto = iter.Get__Alfabeto(),
                    Inicial = iter.Get__Estado_inicial(),
                    Transiciones = Transiciones)
        dot_datos_afd = dot_datos_afd.lstrip()
        return dot_datos_afd
    def dat_datos_afd(self,iter):
        Transiciones = """"""
        for iter_transicion in iter.Get_transiciones():
            Transiciones += "{},{},{}".format(iter_transicion.Get_entrada(),
                                                iter_transicion.Get_estado(),
                                                iter_transicion.Get_destino())
            Transiciones += "\n"
        dot_datos_afd = """
        "Nombre: {Nombre}
            Estados: {Estados}
            Alfabeto: {Alfabeto}
            Estados de Aceptacion: {Aceptacion}
            Estado inicial: {Inicial}
            Transiciones:
            {Transiciones}
        "  [shape=box]
        """.format(Nombre = iter.Get__Nombre(),
                    Estados = iter.Get__Estados(),
                    Alfabeto = iter.Get__Alfabeto(),
                    Aceptacion = iter.Get__Estado_inicial(),
                    Inicial = iter.Get__Estado_Aceptacion(),
                    Transiciones = Transiciones)
        return dot_datos_afd
    def dat_datos_grafo_afd(self,iter):
        all_estados = """"""
        estado_aceptacion_dot = """"""
        estados_generales = """"""
        all_trans = """"""
        estados = iter.Get__Estados().split(',')
        for iter3 in iter.Get__Estado_Aceptacion().split(','):
            print(iter3)
            if iter3 != '':
                estado_aceptacion_dot += "{} [shape=doublecircle]\n".format(iter3)
                estados.remove(iter3)
        for iter2 in estados:
            if iter2 != '':
                estados_generales += "{} [shape=circle]\n".format(iter2)
        estado_inicio = """
        Inicio [shape=rarrow]
        Inicio -> {}
        """.format(iter.Get__Estado_inicial())
        all_estados += estado_aceptacion_dot
        all_estados += estados_generales
        all_estados += estado_inicio
        for iter4 in iter.Get_transiciones():
            if iter4.Get_estado() != '$':
                all_trans += "{} -> {} [label={}]\n".format(iter4.Get_entrada(),iter4.Get_destino(),iter4.Get_estado())
        all_estados += all_trans
        return all_estados
    def Reporte_AFD(self,Nombre_focus):
        for iter in self.data_afd.Get_data():
            if iter.Get__Nombre() == Nombre_focus:
                datos_afd = self.dat_datos_afd(iter)
                grafo = self.dat_datos_grafo_afd(iter)
                all_grafo = """
                digraph AFD {}
                layout=dot rankdir=LR shape=circle
                {}
                {}
                {}
                """.format('{',grafo,datos_afd,"}")
                all_grafo = all_grafo.strip()
                graph = pydot.graph_from_dot_data(all_grafo)
                graph[0].write_pdf("C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-1-_LFP_202000869/Documentation/Reporte_AFD.pdf")
                messagebox.showinfo(title="Alert",message='Reporte Creado Exitosamente')
    def Reporte_GR(self,Nombre_focus):              
        for iter in self.data_gr.Get_data():
            if iter.Get__Nombre() == Nombre_focus:
                datos_afd = self.dat_datos_gr(iter)
                grafo = self.dat_datos_grafo_afd(iter)
                all_grafo = """
                digraph AFD {}
                layout=dot rankdir=LR shape=circle
                {}
                {}
                {}
                """.format('{',grafo,datos_afd,"}")
                all_grafo = all_grafo.strip()
                graph = pydot.graph_from_dot_data(all_grafo)
                graph[0].write_pdf("C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-1-_LFP_202000869/Documentation/Reporte_GR.pdf")
                messagebox.showinfo(title="Alert",message='Reporte Creado Exitosamente')
                
            
