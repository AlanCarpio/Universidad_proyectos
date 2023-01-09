from tkinter import *
from src.view.modules.Abrir_archivo import scanner_contenido_AFD,scanner_contenido_GR,Abrir_AFD_Ayuda,Abrir_GR_Ayuda
from src.view.modules.tabla_verificar import tabla_verificar
from src.view.modules.CreateNewElem import CreateNewElem
class Menu_bar_window():
    def __init__(self,Tk,Master_frame,data_AFD,data_GR) -> None:
        self.Tk = Tk
        self.Master_frame = Master_frame
        self.menu_bar = Menu(Tk)
        self.AFD = Menu(self.menu_bar)
        self.GR = Menu(self.menu_bar)
        self.Cargar_Archivo = Menu(self.menu_bar)
        self.Salir = Menu(self.menu_bar)
        self.tabla_veri = tabla_verificar(self.Master_frame,data_AFD,data_GR)
        self.CreateNewElem = CreateNewElem(data_AFD,data_GR)
    def Insert_sub_elements_bar(self,Tk,data_AFD,data_GR):
        # Sub Elementos AFD
        self.AFD.add_command(label="Crear AFD",command=lambda:self.CreateNewElem.Obj_Entry_AFD(self.Master_frame))
        self.AFD.add_command(label="Evaluar Cadena o Generar reporte",command=lambda:self.tabla_veri.Table_AFD(self.Master_frame,data_AFD))
        self.AFD.add_command(label="Ayuda",command=Abrir_AFD_Ayuda)
        # Sub Elementos GR
        self.GR.add_command(label="Crear GR",command=lambda:self.CreateNewElem.Obj_Entry_GR(self.Master_frame))
        self.GR.add_command(label="Evaluar Cadena o Generar reporte",command=lambda:self.tabla_veri.Table_GR(self.Master_frame,data_GR))
        self.GR.add_command(label="Ayuda",command=Abrir_GR_Ayuda)
        # Sub Elementos Cargar
        self.Cargar_Archivo.add_command(label="Cargar AFD",command=lambda:scanner_contenido_AFD(data_AFD))
        self.Cargar_Archivo.add_command(label="Cargar GR",command=lambda:scanner_contenido_GR(data_GR))
        self.Salir.add_command(label='Salir',command=self.Tk.destroy)
        #
        self.menu_bar.add_cascade(label="AFD",menu=self.AFD)
        self.menu_bar.add_cascade(label="GR",menu=self.GR)
        self.menu_bar.add_cascade(label="Cargar Archivo",menu=self.Cargar_Archivo)
        self.menu_bar.add_cascade(label="Salir",menu=self.Salir)
        Tk.config(menu = self.menu_bar)