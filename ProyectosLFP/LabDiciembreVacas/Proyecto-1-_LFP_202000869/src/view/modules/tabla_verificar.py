from tkinter import *
from tkinter.ttk import Treeview
from tkinter import simpledialog  as MessageBox
from tkinter import messagebox
from src.controller.Validar import Validar
from src.controller.Ruta import Ruta
from src.controller.Generar_reporte import Generar_reporte
class tabla_verificar():
    def __init__(self,Master_frame,data_afd,data_gr) -> None:
        self.data_afd = data_afd
        self.data_gr = data_gr
        # Modulos Interfas AFD
        # Modulos Interfas GR
        pass
    #funciones de las interfaz de GR
    def Table_GR(self,Master_frame,data_AFD):
        #Limpiar Frame 
        for iter in Master_frame.winfo_children():
            iter.destroy()
        # Modulos Interfas AFD
        self.verificar = Button(Master_frame,text="Validar",font="calibri")
        self.Ruta = Button(Master_frame,text="Ruta",font="calibri")
        self.Button_reporte = Button(Master_frame,text="Generar Reporte",font='calibri')
        self.tabla_AFD = Treeview(Master_frame,columns=("col1","col2","col3","col5"))
        #Boton Verificar 
        self.verificar.config(command = lambda:self.Verificar_GR(self.tabla_AFD))
        self.verificar.pack()
        self.verificar.place(x= 600,y=80)
        #Boton Ruta
        self.Ruta.config(command = lambda:self.Ruta_GR(self.tabla_AFD))
        self.Ruta.pack()
        self.Ruta.place(x= 600,y=130)
        #Boton Generar Reporte
        self.Button_reporte.config(command = lambda:self.Generar_reporte_GR(self.tabla_AFD))
        self.Button_reporte.pack()
        self.Button_reporte.place(x= 600,y=180)
        # Tablas para mostrar datos de los AFD
        self.tabla_AFD.column("#0",width=60,anchor=CENTER)
        self.tabla_AFD.column("col1",width= 60,anchor=CENTER)
        self.tabla_AFD.column("col2",width= 60,anchor=CENTER)
        self.tabla_AFD.column("col3",width= 100,anchor=CENTER)
        self.tabla_AFD.column("col5",width= 80,anchor=CENTER)
            #Colocacion de texto de titulos en la tabla
        self.tabla_AFD.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla_AFD.heading("col1",text="No_terminales",anchor=CENTER)
        self.tabla_AFD.heading("col2",text="Terminales",anchor=CENTER)
        self.tabla_AFD.heading("col3",text="No Terminal Inicial",anchor=CENTER)
        self.tabla_AFD.heading("col5",text="Producciones",anchor=CENTER)
        # colocacion Tabla
        self.tabla_AFD.pack()
        self.tabla_AFD.place(x=50,y=50)
        # Imprimir Datos en la Tabla
        for iter in data_AFD.Get_data():
            AFD = self.tabla_AFD.insert("",END,text = iter.Get__Nombre(),values = (iter.Get__Estados(),iter.Get__Alfabeto(),iter.Get__Estado_inicial(),"Ent Est Des"))
            for iter2 in iter.Get_transiciones():
                self.tabla_AFD.insert(AFD,END,text="---",values=("---","---","---",iter2.Get__transicion()))
    def Verificar_GR(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        question_verificar = MessageBox.askstring(title="Evaluar",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        
        validar = Validar(resul['text'],question_verificar,self.data_afd,self.data_gr)
        validar.Validar_GR()
        pass
    def Ruta_GR(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        question_verificar = MessageBox.askstring(title="Ruta",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        ruta = Ruta(resul['text'],question_verificar,self.data_afd,self.data_gr)
        ruta.Ruta_GR()
        pass
    def Generar_reporte_GR(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        Generar = Generar_reporte(self.data_afd,self.data_gr)
        Generar.Reporte_GR(resul['text'])
    #Funciones de las interfaz de AFD
    def Verificar_AFD(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        question_verificar = MessageBox.askstring(title="Evaluar",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        
        validar = Validar(resul['text'],question_verificar,self.data_afd,self.data_gr)
        validar.Validar_AFD()
    def Ruta_AFD(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        question_verificar = MessageBox.askstring(title="Ruta",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        ruta = Ruta(resul['text'],question_verificar,self.data_afd,self.data_gr)
        ruta.Ruta_AFD()
    def Generar_reporte_AFD(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        Generar = Generar_reporte(self.data_afd,self.data_gr)
        Generar.Reporte_AFD(resul['text'])
    def Table_AFD(self,Master_frame,data_AFD):
        #Limpiar Frame 
        for iter in Master_frame.winfo_children():
            iter.destroy()
        # Modulos Interfas AFD
        self.verificar = Button(Master_frame,text="Validar",font="calibri")
        self.Ruta = Button(Master_frame,text="Ruta",font="calibri")
        self.Button_reporte = Button(Master_frame,text="Generar Reporte",font='calibri')
        self.tabla_AFD = Treeview(Master_frame,columns=("col1","col2","col3","col4","col5"))
        #Boton Verificar 
        self.verificar.config(command = lambda:self.Verificar_AFD(self.tabla_AFD))
        self.verificar.pack()
        self.verificar.place(x= 600,y=80)
        #Boton Ruta
        self.Ruta.config(command = lambda:self.Ruta_AFD(self.tabla_AFD))
        self.Ruta.pack()
        self.Ruta.place(x= 600,y=130)
        #Boton Generar Reporte
        self.Button_reporte.config(command = lambda:self.Generar_reporte_AFD(self.tabla_AFD))
        self.Button_reporte.pack()
        self.Button_reporte.place(x= 600,y=180)
        # Tablas para mostrar datos de los AFD
        self.tabla_AFD.column("#0",width=60,anchor=CENTER)
        self.tabla_AFD.column("col1",width= 60,anchor=CENTER)
        self.tabla_AFD.column("col2",width= 60,anchor=CENTER)
        self.tabla_AFD.column("col3",width= 100,anchor=CENTER)
        self.tabla_AFD.column("col4",width= 120,anchor=CENTER)
        self.tabla_AFD.column("col5",width= 80,anchor=CENTER)
            #Colocacion de texto de titulos en la tabla
        self.tabla_AFD.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla_AFD.heading("col1",text="Estados",anchor=CENTER)
        self.tabla_AFD.heading("col2",text="Alfabeto",anchor=CENTER)
        self.tabla_AFD.heading("col3",text="Estado Inicial",anchor=CENTER)
        self.tabla_AFD.heading("col4",text="Estados de Aceptacion",anchor=CENTER)
        self.tabla_AFD.heading("col5",text="Transiciones",anchor=CENTER)
        # colocacion Tabla
        self.tabla_AFD.pack()
        self.tabla_AFD.place(x=50,y=50)
        # Imprimir Datos en la Tabla
        for iter in data_AFD.Get_data():
            AFD = self.tabla_AFD.insert("",END,text = iter.Get__Nombre(),values = (iter.Get__Estados(),iter.Get__Alfabeto(),iter.Get__Estado_inicial(),iter.Get__Estado_Aceptacion(),"Ent Est Des"))
            for iter2 in iter.Get_transiciones():
                self.tabla_AFD.insert(AFD,END,text="---",values=("---","---","---","---",iter2.Get__transicion()))
    #============================================================    