from tkinter import *
from src.model.AFD.AFD import AFD
from src.model.AFD.Transicion import Transicion
from tkinter.messagebox import showinfo

class CreateNewElem():
    def __init__(self,data_AFD,data_GR) -> None:
        self.data_AFD = data_AFD
        self.data_gr = data_GR
        self.Nombre = StringVar()
        self.Estados = StringVar()
        self.Alfabeto = StringVar()
        self.Estado_inicial = StringVar()
        self.Estado_aceptacion = StringVar()
        self.Transicion = StringVar()
        self.list_transicion = []
        pass
    def EmptyVariables(self):
        self.Nombre.set('')
        self.Estados.set('')
        self.Alfabeto.set('')
        self.Estado_inicial.set('')
        self.Estado_aceptacion.set('')
        self.Transicion.set('')
        self.list_transicion = []
    def Next(self,Transicion_entry,Transicion_button):
        if self.Nombre.get() == "" or '' :
            showinfo(title="Error",message="El Campo Nombre esta vacio")
            return
        if self.Estados.get() == "" or '' :
            showinfo(title="Error",message="El Campo Estados esta vacio")
            return
        if self.Alfabeto.get() == "" or '' :
            showinfo(title="Error",message="El Campo Alfabeto esta vacio")
            return
        if self.Estado_inicial.get() == "" or '' :
            showinfo(title="Error",message="El Campo Estado inicial esta vacio")
            return
        else:
            state_estado_inicial = False
            for iter in self.Estados.get().split(','):
                if iter == self.Estado_inicial.get():
                    state_estado_inicial = True
            if state_estado_inicial:
                pass
            else:
                showinfo(title="Error",message="El estado inicial no pertenece a los estados ingresados")
                return
        if self.Estado_aceptacion.get() == "" or '' :
            showinfo(title="Error",message="El Campo Estado aceptacion esta vacio")
            return
        else:
            cont_estado_acep = len(self.Estado_aceptacion.get().split(','))
            cont = 0
            for iter in self.Estados.get().split(','):
                for iter2 in self.Estado_aceptacion.get().split(','):
                    if iter == iter2:
                        cont += 1
            if cont == cont_estado_acep:
                pass
            else:
                showinfo(title="Error",message="Algunos de los estados de aceptacion no pertenece a los estados ingresados")
                return
            
        Transicion_entry.config(state = NORMAL)
        Transicion_button.config(state = NORMAL)
    def Create_AFD(self,Master_frame):
        afd = AFD(self.Nombre.get(),self.Estados.get(),self.Alfabeto.get(),self.Estado_inicial.get(),self.Estado_aceptacion.get(),self.list_transicion)
        self.data_AFD.insert_element(afd)
        self.list_transicion = []
        showinfo(title="Alert",message='AFD Creado Correctamente')
        self.Obj_Entry_AFD(Master_frame)
        pass
    def Create_Transicion(self):
        trans_resul = self.Transicion.get()
        trans_resul = trans_resul.split(',')
        state_estado_Entrada = False
        state_estado_estado = False
        state_estado_destino = False
        for iter in self.Estados.get().split(','):
            if iter == trans_resul[0]:
                state_estado_Entrada = True
        if state_estado_Entrada:
            pass
        else:
            showinfo(title="Error",message="El estado de entrada no pertenece a los estados ingresados")
            return
        #============================================
        for iter in self.Alfabeto.get().split(','):
            if iter == trans_resul[1] or trans_resul[1] == '$':
                state_estado_estado = True
        if state_estado_estado:
            pass
        else:
            showinfo(title="Error",message="El estado  no pertenece al alfabeto")
            return
        #==========================================
        for iter in self.Estados.get().split(','):
            if iter == trans_resul[2]:
                state_estado_destino = True
        if state_estado_destino:
            pass
        else:
            showinfo(title="Error",message="El estado de destino no pertenece a los estados ingresados")
            return
        transicion = Transicion(trans_resul[0],trans_resul[1],trans_resul[2])
        self.list_transicion.append(transicion)
        showinfo("Alert","Transicion Agregada Correctamente")
        pass
    def Obj_Label_AFD(self,Master_frame):
        Nombre_Label = Label(Master_frame,text = "Nombre ")
        Estados_Label = Label(Master_frame,text="Estados (Separados por comas)")
        Alfabeto_Label = Label(Master_frame,text="Alfabeto (Separados por comas)")
        Estado_inicial_Label = Label(Master_frame,text="Estado Inicial")
        Estado_aceptacion_Label = Label(Master_frame,text="Estados de Aceptacion (Separados por comas)")
        Transicion_Label = Label(Master_frame,text="Transicion (Separados por comas)")

        Nombre_Label.pack()
        Nombre_Label.place(x=50,y=10)
        
        Estados_Label.pack()
        Estados_Label.place(x=50,y=60)

        Alfabeto_Label.pack()
        Alfabeto_Label.place(x=50,y=110)

        Estado_inicial_Label.pack()
        Estado_inicial_Label.place(x=50,y=160)

        Estado_aceptacion_Label.pack()
        Estado_aceptacion_Label.place(x=50,y=210)

        Transicion_Label.pack()
        Transicion_Label.place(x=50,y=260)
    def Obj_Entry_AFD(self,Master_frame):
        for iter in Master_frame.winfo_children():
            iter.destroy()
        self.EmptyVariables()
        self.Obj_Label_AFD(Master_frame)
        Next = Button(Master_frame,text= "Continuar",command=lambda:self.Next(Transicion_entry,Agregar_Transicion))
        Agregar_Transicion = Button(Master_frame,text='Agregar',command=self.Create_Transicion,state=DISABLED)
        Agregar_AFD = Button(Master_frame,text="Agregar AFD",command=lambda:self.Create_AFD(Master_frame))
        # Declaracion de Objetos Tipo Entrada de Texto
        Nombre_entry = Entry(Master_frame,textvariable=self.Nombre,width=10,borderwidth=3)
        Estados_entry = Entry(Master_frame,textvariable=self.Estados,width=10,borderwidth=3)
        Alfabeto_entry = Entry(Master_frame,textvariable=self.Alfabeto,width=10,borderwidth=3)
        Estado_inicial_entry = Entry(Master_frame,textvariable=self.Estado_inicial,width=10,borderwidth=3)
        Estado_aceptacion_entry = Entry(Master_frame,textvariable=self.Estado_aceptacion,width=10,borderwidth=3)
        Transicion_entry = Entry(Master_frame,textvariable=self.Transicion,width=10,state = DISABLED,borderwidth=3)
        #Colocacion en el Frame
        Nombre_entry.pack()
        Nombre_entry.place(x=400,y=10)
        
        Estados_entry.pack()
        Estados_entry.place(x=400,y=60)

        Alfabeto_entry.pack()
        Alfabeto_entry.place(x=400,y=110)

        Estado_inicial_entry.pack()
        Estado_inicial_entry.place(x=400,y=160)

        Estado_aceptacion_entry.pack()
        Estado_aceptacion_entry.place(x=400,y=210)

        Transicion_entry.pack()
        Transicion_entry.place(x=400,y=260)

        Next.pack()
        Next.place(x=500,y=210)
        
        Agregar_Transicion.pack()
        Agregar_Transicion.place(x=500,y=260)

        Agregar_AFD.pack()
        Agregar_AFD.place(x=320,y=310)

    #===================== GR =============================
    def Next_GR(self,Transicion_entry,Transicion_button):
        if self.Nombre.get() == "" or '' :
            showinfo(title="Error",message="El Campo Nombre esta vacio")
            return
        if self.Estados.get() == "" or '' :
            showinfo(title="Error",message="El Campo Estados esta vacio")
            return
        if self.Alfabeto.get() == "" or '' :
            showinfo(title="Error",message="El Campo Alfabeto esta vacio")
            return
        if self.Estado_inicial.get() == "" or '' :
            showinfo(title="Error",message="El Campo Estado inicial esta vacio")
            return
        else:
            state_estado_inicial = False
            for iter in self.Estados.get().split(','):
                if iter == self.Estado_inicial.get():
                    state_estado_inicial = True
            if state_estado_inicial:
                pass
            else:
                showinfo(title="Error",message="El estado inicial no pertenece a los estados ingresados")
                return
            
        Transicion_entry.config(state = NORMAL)
        Transicion_button.config(state = NORMAL)
    def Create_GR(self,Master_frame):
        Estado_aceptacion = ''
        for iter in self.list_transicion:
            if iter.Get_estado() == '$':
                Estado_aceptacion += iter.Get_entrada()
                Estado_aceptacion += ','
        afd = AFD(self.Nombre.get(),self.Estados.get(),self.Alfabeto.get(),self.Estado_inicial.get(),Estado_aceptacion,self.list_transicion)
        self.data_gr.insert_element(afd)
        self.list_transicion = []
        showinfo(title="Alert",message='AFD Creado Correctamente')
        self.Obj_Entry_GR(Master_frame)
        pass
    def Create_Produccion(self):
        trans_resul = self.Transicion.get()
        trans_resul = trans_resul.split(',')
        state_estado_Entrada = False
        state_estado_estado = False
        state_estado_destino = False
        for iter in self.Estados.get().split(','):
            if iter == trans_resul[0]:
                state_estado_Entrada = True
        if state_estado_Entrada:
            pass
        else:
            showinfo(title="Error",message="El estado de entrada no pertenece a los estados ingresados")
            return
        #============================================
        for iter in self.Alfabeto.get().split(','):
            if iter == trans_resul[1] or trans_resul[1] == '$':
                state_estado_estado = True
        if state_estado_estado:
            pass
        else:
            showinfo(title="Error",message="El estado  no pertenece al alfabeto")
            return
        #==========================================
        
        for iter in self.Estados.get().split(','):
            if iter == trans_resul[2] or trans_resul[2] == '':
                state_estado_destino = True
        if state_estado_destino:
            pass
        else:
            showinfo(title="Error",message="El estado de destino no pertenece a los estados ingresados")
            return
        transicion = Transicion(trans_resul[0],trans_resul[1],trans_resul[2])
        self.list_transicion.append(transicion)
        showinfo("Alert","Transicion Agregada Correctamente")
        pass
    def Obj_Label_GR(self,Master_frame):
        Nombre_Label = Label(Master_frame,text = "Nombre ")
        Estados_Label = Label(Master_frame,text="No Terminales (Separados por comas)")
        Alfabeto_Label = Label(Master_frame,text="Terminales (Separados por comas)")
        Estado_inicial_Label = Label(Master_frame,text="No Terminal Inicial")
        Transicion_Label = Label(Master_frame,text="Producciones (Separados por comas)")

        Nombre_Label.pack()
        Nombre_Label.place(x=50,y=10)
        
        Estados_Label.pack()
        Estados_Label.place(x=50,y=60)

        Alfabeto_Label.pack()
        Alfabeto_Label.place(x=50,y=110)

        Estado_inicial_Label.pack()
        Estado_inicial_Label.place(x=50,y=160)

        Transicion_Label.pack()
        Transicion_Label.place(x=50,y=210)
    def Obj_Entry_GR(self,Master_frame):
        for iter in Master_frame.winfo_children():
            iter.destroy()
        self.EmptyVariables()
        self.Obj_Label_GR(Master_frame)
        Next = Button(Master_frame,text= "Continuar",command=lambda:self.Next_GR(Transicion_entry,Agregar_Transicion))
        Agregar_Transicion = Button(Master_frame,text='Agregar',command=self.Create_Produccion,state=DISABLED)
        Agregar_AFD = Button(Master_frame,text="Agregar GR",command=lambda:self.Create_GR(Master_frame))
        # Declaracion de Objetos Tipo Entrada de Texto
        Nombre_entry = Entry(Master_frame,textvariable=self.Nombre,width=10,borderwidth=3)
        Estados_entry = Entry(Master_frame,textvariable=self.Estados,width=10,borderwidth=3)
        Alfabeto_entry = Entry(Master_frame,textvariable=self.Alfabeto,width=10,borderwidth=3)
        Estado_inicial_entry = Entry(Master_frame,textvariable=self.Estado_inicial,width=10,borderwidth=3)
        Transicion_entry = Entry(Master_frame,textvariable=self.Transicion,width=10,state = DISABLED,borderwidth=3)
        #Colocacion en el Frame
        Nombre_entry.pack()
        Nombre_entry.place(x=400,y=10)
        
        Estados_entry.pack()
        Estados_entry.place(x=400,y=60)

        Alfabeto_entry.pack()
        Alfabeto_entry.place(x=400,y=110)

        Estado_inicial_entry.pack()
        Estado_inicial_entry.place(x=400,y=160)

        Transicion_entry.pack()
        Transicion_entry.place(x=400,y=210)

        Next.pack()
        Next.place(x=500,y=160)
        
        Agregar_Transicion.pack()
        Agregar_Transicion.place(x=500,y=210)

        Agregar_AFD.pack()
        Agregar_AFD.place(x=320,y=260)