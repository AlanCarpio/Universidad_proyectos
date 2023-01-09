from tkinter import *
from tkinter.ttk import Treeview
from tkinter import simpledialog  as MessageBox
from tkinter import messagebox

from controller.AutomataPila.Mostrar import Mostrar
from controller.AutomataPila.Validar import Validar
from controller.AutomataPila.Ruta import Ruta
from controller.AutomataPila.RutaPasada import RutaPasada
from view.modules.SubWindowRuta import SubWindowRuta
from view.modules.SubWindowRutaPasada import SubWindowRutaPasada
from view.modules.SubwindowArbol import SubwindowArbol
class Table():
    def __init__(self,Master_frame,MasterWindow,data_AUP,data_GRC) -> None:
        self.MasterWindow = MasterWindow
        self.data_AUP = data_AUP
        self.data_GRC = data_GRC
        self.Master_frame = Master_frame
        # Modulos Interfas AFD
        # Modulos Interfas GR
        pass
    #funciones de las interfaz de GRC
    def Table_GRC(self):
        #Limpiar Frame 
        for iter in self.Master_frame .winfo_children():
            iter.destroy()
        # Modulos Interfas AFD
        self.Button_reporte = Button(self.Master_frame ,text="Generar Arbol",foreground='blue',font='calibri',height=5,width=20,border=3)
        self.tabla_AFD = Treeview(self.Master_frame ,columns=("col1","col2","col3","col5"))
        #Boton Generar Reporte
        self.Button_reporte.config(command = lambda:self.Arbol_GRC(self.tabla_AFD))
        self.Button_reporte.pack()
        self.Button_reporte.place(x= 490,y=90)
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
        for iter in self.data_GRC:
            resul = iter.Get_DatosGramatica()
            AFD = self.tabla_AFD.insert("",END,text = resul[0],values = (resul[1],resul[2],resul[3],"_ _ _ _"))
            OrigenAnterior = ''
            for iter2 in resul[4]:
                Tabla_insert = ''
                resul2 = iter2.Get_producciones()
                if resul2[0] == OrigenAnterior:
                    Tabla_insert = '|'
                    pass
                else:
                    OrigenAnterior = resul2[0]
                    Tabla_insert = resul2[0]
                self.tabla_AFD.insert(AFD,END,text="---",values=("---","---","---","{} {}".format(Tabla_insert,resul2[1])))
    def Arbol_GRC(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione una Gramatica")
        SubwindowArbol(resul['text'],self.data_GRC)
    #Funciones de las interfaz de AUP
    def Table_AUP(self):
        #Limpiar Frame 
        for iter in self.Master_frame.winfo_children():
            iter.destroy()
        # Modulos Interfas AFD
        self.verificar = Button(self.Master_frame,text="Validar",font="calibri")
        self.Ruta = Button(self.Master_frame,text="Ruta",font="calibri")
        self.RutaPaso = Button(self.Master_frame,text="Ruta Paso a Paso",font="calibri")
        self.RutaPasa = Button(self.Master_frame,text="Ruta Pasada",font="calibri")
        self.Button_reporte = Button(self.Master_frame,text="Generar Reporte",font='calibri')
        self.tabla_AFD = Treeview(self.Master_frame,columns=("col1","col2","col3","col4","col5",'col6'))
        #Boton Verificar 
        self.verificar.config(command = lambda:self.Verificar_AUP(self.tabla_AFD))
        self.verificar.pack()
        self.verificar.place(x= 650,y=50)
        #Boton Ruta
        self.Ruta.config(command = lambda:self.Ruta_AUP(self.tabla_AFD))
        self.Ruta.pack()
        self.Ruta.place(x= 650,y=100)
        #Boton Ruta Paso a Paso
        self.RutaPaso.config(command = lambda:self.Ruta_AUP_Paso_Paso(self.tabla_AFD))
        self.RutaPaso.pack()
        self.RutaPaso.place(x= 650,y=150)
        #Boton Generar Reporte
        self.Button_reporte.config(command = lambda:self.Generar_reporte_AUP(self.tabla_AFD))
        self.Button_reporte.pack()
        self.Button_reporte.place(x= 650,y=200)
        #
        self.RutaPasa.config(command = lambda:self.RutaPasada_AUP(self.tabla_AFD))
        self.RutaPasa.pack()
        self.RutaPasa.place(x= 650,y=250)
        # Tablas para mostrar datos de los AFD
        self.tabla_AFD.column("#0",width=60,anchor=CENTER)
        self.tabla_AFD.column("col1",width= 60,anchor=CENTER)
        self.tabla_AFD.column("col2",width= 60,anchor=CENTER)
        self.tabla_AFD.column("col3",width= 100,anchor=CENTER)
        self.tabla_AFD.column("col4",width= 100,anchor=CENTER)
        self.tabla_AFD.column("col5",width= 120,anchor=CENTER)
        self.tabla_AFD.column("col6",width= 100,anchor=CENTER)
            #Colocacion de texto de titulos en la tabla
        self.tabla_AFD.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla_AFD.heading("col1",text="Estados",anchor=CENTER)
        self.tabla_AFD.heading("col2",text="Alfabeto",anchor=CENTER)
        self.tabla_AFD.heading("col3",text="Simbolos Pila",anchor=CENTER)
        self.tabla_AFD.heading("col4",text="Estado Inicial",anchor=CENTER)
        self.tabla_AFD.heading("col5",text="Estados Aceptacion",anchor=CENTER)
        self.tabla_AFD.heading("col6",text="Transiciones",anchor=CENTER)
        # colocacion Tabla
        self.tabla_AFD.pack()
        self.tabla_AFD.place(x=25,y=50)
        # Imprimir Datos en la Tabla
        for iter in self.data_AUP:
            resul = iter.Get_info()
            AFD = self.tabla_AFD.insert("",END,text = resul[0],values = (resul[3],resul[1],resul[2],resul[4],resul[5],"- - - - -"))
            for iter2 in resul[6]:
                self.tabla_AFD.insert(AFD,END,text="---",values=("---","---","---","---","---",iter2.Get_Transiciones()))
                pass
    #============================================================    
    def Verificar_AUP(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        question_verificar = MessageBox.askstring(title="Evaluar",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        validar = Validar(resul['text'],question_verificar,self.data_AUP)
        validar.Validar_AUP()
        
    def Ruta_AUP(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AFD")
        question_verificar = MessageBox.askstring(title="Ruta",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        ruta = Ruta(resul['text'],question_verificar,self.data_AUP)     
        mensaje = ruta.Ruta_AUP()
        messagebox.showinfo('Notificacion',mensaje[0])
    def Ruta_AUP_Paso_Paso(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AUP")
        question_verificar = MessageBox.askstring(title="Ruta",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        ruta = Ruta(resul['text'],question_verificar,self.data_AUP)     
        list_ruta = ruta.Ruta_AUP()
        
        sub = SubWindowRuta(resul['text'],self.data_AUP,list_ruta[1],list_ruta[0])
    def RutaPasada_AUP(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AUP")
        question_verificar = MessageBox.askstring(title="Ruta",prompt="Ingrese una cadena")
        if question_verificar == None:
            return messagebox.showerror("Error","Ingrese una Cadena")
        ruta = Ruta(resul['text'],question_verificar,self.data_AUP)     
        list_ruta = ruta.Ruta_AUP()
        sub = SubWindowRutaPasada(resul['text'],self.data_AUP,list_ruta[1],list_ruta[0])
        
        
    def Generar_reporte_AUP(self,tabla):
        dato = tabla.focus()
        resul = tabla.item(dato)
        if resul['text'] == '' or resul['text'] == ' ':
            return messagebox.showerror("Error","Seleccione un AUP")
        mostrar = Mostrar(resul['text'],self.data_AUP)
        mostrar.MostrarInfoAuto()
        
    