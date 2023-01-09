from tkinter import *
from view.modules.OpenFile import OpenFile_Gra_Libre_Contx,OpenFile_AUTO_P
from view.modules.Table import Table
from view.modules.Counter5secundsExit import Exit
class MenuBar():
    def __init__(self,Tk,Master_frame,data_GRC,data_AUP) -> None:
        self.data_GRC = data_GRC
        self.data_AUP = data_AUP
        self.Tk = Tk
        self.Master_frame = Master_frame
        self.menu_bar = Menu(Tk)
        self.GramaticaLibreContexto = Menu(self.menu_bar)
        self.AutomataPila = Menu(self.menu_bar)
        self.Tabla = Table(Master_frame,Tk,self.data_AUP,self.data_GRC)
        self.Salir = Menu(self.menu_bar)
        #self.tabla_veri = tabla_verificar(self.Master_frame,data_AFD,data_GR)
        #self.CreateNewElem = CreateNewElem(data_AFD,data_GR)
    def Insert_sub_elements_bar(self):
        # Sub Elementos AFD
        self.GramaticaLibreContexto.add_command(label="Cargar Archivo",command=lambda:OpenFile_Gra_Libre_Contx(self.data_GRC))
        self.GramaticaLibreContexto.add_command(label="Mostrar Informacion",command=self.Tabla.Table_GRC)
        self.GramaticaLibreContexto.add_command(label="Ayuda")
        # Sub Elementos GR
        self.AutomataPila.add_command(label="Cargar Archivo",command=lambda:OpenFile_AUTO_P(self.data_AUP))
        self.AutomataPila.add_command(label="Mostrar Informacion",command=self.Tabla.Table_AUP)
        self.AutomataPila.add_command(label="Ayuda")
        # sub elemento salir
        self.Salir.add_command(label='Salir',command=lambda:Exit(self.Tk,self.Master_frame))
        # Sub Elementos Cargar
        #
        self.menu_bar.add_cascade(label="Gramatica Libre de Contexto",menu=self.GramaticaLibreContexto)
        self.menu_bar.add_cascade(label="Automata de Pila",menu=self.AutomataPila)
        self.menu_bar.add_cascade(label="Salir",menu=self.Salir)
        self.Tk.config(menu = self.menu_bar)