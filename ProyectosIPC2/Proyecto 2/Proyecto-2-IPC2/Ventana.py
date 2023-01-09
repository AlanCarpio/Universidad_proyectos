from tkinter import*
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo
from tkinter.ttk import Treeview
from CargarA import cargar_archivo 
from ListasEnlazadas import*
from simulacion import*
class Windown_Main():
    windown_main = Tk()
    frame_main = Frame(windown_main,width=1000,height=400,relief=RAISED,bd=20)
    menubar = Menu(windown_main)
    Archivo = Menu(menubar)
    Options = Menu(menubar)
    CA = cargar_archivo()
    lista_empresa = CA.listaEmpre
    lista_config = CA.listaconfigInicial

     #==========================String Var =====================================
    id_empresa = StringVar()
    nombre_empresa = StringVar()
    abre_empresa = StringVar()
    id_punto = StringVar()
    nombre_punto = StringVar()
    direccion_punto = StringVar()
    id_escri = StringVar()
    identificacion_escri = StringVar()
    encargado_escri = StringVar()
    id_trac = StringVar()
    nombre_trac = StringVar()
    tiempo_trac = StringVar()
    temporal_punto = None
    temporal_punto_confi = None
    ##lista_escritorio = ListaSimple()
    ##lista_punto = None
    ##lista_trac = None
    def cargarConfi(self):
        try:
            filename = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
            bol = self.CA.cargar_confi(filename)
            if bol:
                info = showinfo("Noti","Archivo Cargado Exitosamente")
            else:
                pass
        except:
            pass
    def cargarPrueba(self):
        try:
            filename = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
            bol = self.CA.cargar_prueba(filename)
            if bol:
                info = showinfo("Noti","Archivo Cargado Exitosamente")
            else:
                pass
        except:
            pass
    def limpiar(self):
        self.lista_config.eliminar()
        self.lista_empresa.eliminar()
        info = showinfo("Noti","Limpiesa del sistema hecha Exitosamente")
    #================================= Funcion Agregar Empresa==============================
    def Agregar_empresa(self):
        empresa = self.CA.empresa_configuracion(self.id_empresa.get(),self.nombre_empresa.get(),self.abre_empresa.get(),self.lista_punto,self.lista_trac)
        self.lista_empresa.insertar_Empresa(empresa)
        info = showinfo("Notification","Empresa Agregada Exitosamente")
        self.Agregar_Empresa()
        pass
    def verificar_empresa(self):
        if self.id_empresa.get() == " " or self.nombre_empresa.get() == "" or self.abre_empresa.get() == "":
            info = showerror("Error","No deje casillas en blanco")
            return
        else:
            lista_punto = ListaSimple()
            lista_trac = ListaSimple()
            self.lista_punto = lista_punto
            self.lista_trac = lista_trac
            siguiente_punto = Button(self.frame_main,text="Siguiente",command=self.verificar_punto).place(x= 600,y=110)
            Entry_punto_id = Entry(self.frame_main,textvariable=self.id_punto,width=10).place(x=140,y= 110)
            Entry_punto_nombre = Entry(self.frame_main,textvariable=self.nombre_punto,width=15).place(x=290,y= 110)
            Entry_punto_abre = Entry(self.frame_main,textvariable=self.direccion_punto,width=15).place(x=480,y= 110)
            pass
        siguiente_empresa = Button(self.frame_main,text="Siguiente",command=self.verificar_empresa,state=DISABLED).place(x= 600,y=50)
        Entry_empresa_id = Entry(self.frame_main,textvariable=self.id_empresa,width=10,state=DISABLED).place(x=140,y= 50)
        Entry_empresa_nombre = Entry(self.frame_main,textvariable=self.nombre_empresa,width=15,state=DISABLED).place(x=290,y= 50)
        Entry_empresa_abre = Entry(self.frame_main,textvariable=self.abre_empresa,width=15,state=DISABLED).place(x=480,y= 50)
    def verificar_punto(self):
        if self.id_punto.get() == "" or self.nombre_punto.get() == "" or self.direccion_punto.get() == "":
            info = showerror("Error","No deje casillas en blanco")
            return
        else:
            lista_escritorio = ListaSimple()
            self.lista_escritorio = lista_escritorio
            Entry_punto_id = Entry(self.frame_main,textvariable=self.id_punto,width=10,state=DISABLED).place(x=140,y= 110)
            Entry_punto_nombre = Entry(self.frame_main,textvariable=self.nombre_punto,width=15,state=DISABLED).place(x=290,y= 110)
            Entry_punto_abre = Entry(self.frame_main,textvariable=self.direccion_punto,width=15,state=DISABLED).place(x=480,y= 110)
            Entry_Escritorio_id = Entry(self.frame_main,textvariable=self.id_escri,width=10).place(x=140,y= 170)
            Entry_Escritorio_nombre = Entry(self.frame_main,textvariable=self.identificacion_escri,width=15).place(x=300,y= 170)
            Entry_Escritorio_abre = Entry(self.frame_main,textvariable=self.encargado_escri,width=15).place(x=480,y= 170)
            Agregar_escri_but = Button(self.frame_main,text="Agregar Escritorio",command=self.Agregar_escritorio).place(x= 600,y=170)
            siguiente_punto = Button(self.frame_main,text="Siguiente",state=DISABLED,command=self.verificar_punto).place(x= 600,y=110)
            
        pass
    def Agregar_escritorio(self):
        if self.id_escri.get() == "" or self.identificacion_escri.get() == "" or self.encargado_escri.get() == "":
            info = showerror("Error","No deje casillas en blanco")
            return
        else:
            escri = self.CA.empresa_configuracion.listEscri_confi(self.id_escri.get(),self.identificacion_escri.get(),self.encargado_escri.get())
            self.lista_escritorio.insertar_Empresa(escri)
            info = showinfo("Notification","Escritorio Agregado Exitosamente")
            Agregar_punto_but = Button(self.frame_main,text="Agregar Nuevo Punto",command=self.nuevo_punto).place(x= 720,y=170)
            Agregar_siguiente_but = Button(self.frame_main,text="Siguiente",command=self.siguiente_escritorios).place(x= 860,y=170)
            
            pass
        pass
        pass
    def nuevo_punto(self):
        punto = self.CA.empresa_configuracion.listPuntos_confi(self.id_punto.get(),self.nombre_punto.get(),self.direccion_punto.get(),self.lista_escritorio)
        self.lista_punto.insertar_Empresa(punto)
        info = showinfo("Notification","Punto Agregado Exitosamente")
        self.id_escri.set("")
        self.identificacion_escri.set("")
        self.encargado_escri.set("")
        self.id_punto.set("")
        self.nombre_punto.set("")
        self.direccion_punto.set("")
        Entry_punto_id = Entry(self.frame_main,textvariable=self.id_punto,width=10).place(x=140,y= 110)
        Entry_punto_nombre = Entry(self.frame_main,textvariable=self.nombre_punto,width=15).place(x=290,y= 110)
        Entry_punto_abre = Entry(self.frame_main,textvariable=self.direccion_punto,width=15).place(x=480,y= 110)
        siguiente_punto = Button(self.frame_main,text="Siguiente",command=self.verificar_punto).place(x= 600,y=110)
        Entry_Escritorio_id = Entry(self.frame_main,textvariable=self.id_escri,width=10,state=DISABLED).place(x=140,y= 170)
        Entry_Escritorio_nombre = Entry(self.frame_main,textvariable=self.identificacion_escri,width=15,state=DISABLED).place(x=300,y= 170)
        Entry_Escritorio_abre = Entry(self.frame_main,textvariable=self.encargado_escri,width=15,state=DISABLED).place(x=480,y= 170)
        Agregar_escri_but = Button(self.frame_main,text="Agregar Escritorio",state=DISABLED,command=self.Agregar_escritorio).place(x= 600,y=170)
        Agregar_punto_but = Button(self.frame_main,text="Agregar Nuevo Punto",state=DISABLED,command=self.nuevo_punto).place(x= 720,y=170)
        Agregar_siguiente_but = Button(self.frame_main,text="Siguiente",state=DISABLED,command=self.siguiente_escritorios).place(x= 860,y=170)
    def siguiente_escritorios(self):
        punto = self.CA.empresa_configuracion.listPuntos_confi(self.id_punto.get(),self.nombre_punto.get(),self.direccion_punto.get(),self.lista_escritorio)
        self.lista_punto.insertar_Empresa(punto)
        
        info = showinfo("Notification","Punto Agregado Exitosamente")
        
        Entry_transaccion_id = Entry(self.frame_main,textvariable=self.id_trac,width=10).place(x=140,y= 230)
        Entry_transaccion_nombre = Entry(self.frame_main,textvariable=self.nombre_trac,width=15).place(x=290,y= 230)
        Entry_transaccion_abre = Entry(self.frame_main,textvariable=self.tiempo_trac,width=15).place(x=510,y= 230)
        Entry_Escritorio_id = Entry(self.frame_main,textvariable=self.id_escri,width=10,state=DISABLED).place(x=140,y= 170)
        Entry_Escritorio_nombre = Entry(self.frame_main,textvariable=self.identificacion_escri,width=15,state=DISABLED).place(x=300,y= 170)
        Entry_Escritorio_abre = Entry(self.frame_main,textvariable=self.encargado_escri,width=15,state=DISABLED).place(x=480,y= 170)
        Agregar_escri_but = Button(self.frame_main,text="Agregar Escritorio",state=DISABLED,command=self.Agregar_escritorio).place(x= 600,y=170)
        Agregar_punto_but = Button(self.frame_main,text="Agregar Nuevo Punto",state=DISABLED,command=self.nuevo_punto).place(x= 720,y=170)
        Agregar_siguiente_but = Button(self.frame_main,text="Siguiente",state=DISABLED,command=self.siguiente_escritorios).place(x= 860,y=170)
        Agregar_transaccion_but = Button(self.frame_main,text="Agregar Transaccion",command=self.Agregar_Trac).place(x= 630,y=230)
    def Agregar_Trac(self):
        if self.id_trac.get() == " " or self.nombre_trac.get() == "" or self.tiempo_trac.get() == "":
            info = showerror("Error","No deje casillas en blanco")
            return
            
        else:
            trac = self.CA.empresa_configuracion.listTracc_config(self.id_trac.get(),self.nombre_trac.get(),int(self.tiempo_trac.get()))
            self.lista_trac.insertar_Empresa(trac)
            
            agregar_empresa = Button(self.frame_main,text="Agregar Empresa",font='Helvetica 12 bold',command=self.Agregar_empresa).place(x= 320,y=280)
            info = showinfo("Notification","Transaccion Agregado Exitosamente")
    def Agregar_Empresa(self):
        self.windown_main.geometry("1000x400")
        self.frame_main.config(width=1000,height=400)
        self.id_empresa.set("")
        self.nombre_empresa.set("")
        self.abre_empresa.set("")
        self.id_punto.set("")
        self.nombre_punto.set("")
        self.direccion_punto.set("")
        self.id_escri.set("")
        self.identificacion_escri.set("")
        self.encargado_escri.set("")
        self.id_trac.set("")
        self.nombre_trac.set("")
        self.tiempo_trac.set("")
        for gadgets in self.frame_main.winfo_children():
            gadgets.destroy()
        #================== Botones ==========================================
        siguiente_empresa = Button(self.frame_main,text="Siguiente",command=self.verificar_empresa).place(x= 600,y=50)
        siguiente_punto = Button(self.frame_main,text="Siguiente",state=DISABLED,command=self.verificar_punto).place(x= 600,y=110)
        Agregar_escri_but = Button(self.frame_main,text="Agregar Escritorio",state=DISABLED,command=self.Agregar_escritorio).place(x= 600,y=170)
        Agregar_punto_but = Button(self.frame_main,text="Agregar Nuevo Punto",state=DISABLED,command=self.nuevo_punto).place(x= 720,y=170)
        Agregar_siguiente_but = Button(self.frame_main,text="Siguiente",state=DISABLED,command=self.siguiente_escritorios).place(x= 860,y=170)
        Agregar_transaccion_but = Button(self.frame_main,text="Agregar Transaccion",state=DISABLED,command=self.Agregar_Trac).place(x= 630,y=230)
        agregar_empresa = Button(self.frame_main,text="Agregar Empresa",font='Helvetica 12 bold',state=DISABLED,command=self.Agregar_empresa).place(x= 320,y=280)
        #==============================Entry=======================================
        Entry_empresa_id = Entry(self.frame_main,textvariable=self.id_empresa,width=10).place(x=140,y= 50)
        Entry_empresa_nombre = Entry(self.frame_main,textvariable=self.nombre_empresa,width=15).place(x=290,y= 50)
        Entry_empresa_abre = Entry(self.frame_main,textvariable=self.abre_empresa,width=15).place(x=480,y= 50)
        #=============== Punto========================================================
        Entry_punto_id = Entry(self.frame_main,textvariable=self.id_punto,width=10,state=DISABLED).place(x=140,y= 110)
        Entry_punto_nombre = Entry(self.frame_main,textvariable=self.nombre_punto,width=15,state=DISABLED).place(x=290,y= 110)
        Entry_punto_abre = Entry(self.frame_main,textvariable=self.direccion_punto,width=15,state=DISABLED).place(x=480,y= 110)
        #===================Escritorio =============================================
        Entry_Escritorio_id = Entry(self.frame_main,textvariable=self.id_escri,width=10,state=DISABLED).place(x=140,y= 170)
        Entry_Escritorio_nombre = Entry(self.frame_main,textvariable=self.identificacion_escri,width=15,state=DISABLED).place(x=300,y= 170)
        Entry_Escritorio_abre = Entry(self.frame_main,textvariable=self.encargado_escri,width=15,state=DISABLED).place(x=480,y= 170)
        #===================transaccion =============================================
        Entry_transaccion_id = Entry(self.frame_main,textvariable=self.id_trac,width=10,state=DISABLED).place(x=140,y= 230)
        Entry_transaccion_nombre = Entry(self.frame_main,textvariable=self.nombre_trac,width=15,state=DISABLED).place(x=290,y= 230)
        Entry_transaccion_abre = Entry(self.frame_main,textvariable=self.tiempo_trac,width=15,state=DISABLED).place(x=510,y= 230)
        #============================ Labels ==========================================
        Label01 = Label(self.frame_main,text="Empresa",font='Helvetica 12 bold').place(x=5,y=50)
        Label02 = Label(self.frame_main,text="ID",font='Helvetica 8 bold').place(x=120,y=50)
        Label03 = Label(self.frame_main,text="Nombre",font='Helvetica 8 bold').place(x=220,y=50)
        Label04 = Label(self.frame_main,text="Abreviatura",font='Helvetica 8 bold').place(x=400,y=50)
        #=============== Punto========================================================
        Label05 = Label(self.frame_main,text="Punto",font='Helvetica 12 bold').place(x=5,y=110)
        Label06 = Label(self.frame_main,text="ID",font='Helvetica 8 bold').place(x=120,y=110)
        Label07 = Label(self.frame_main,text="Nombre",font='Helvetica 8 bold').place(x=220,y=110)
        Label08 = Label(self.frame_main,text="Dirrecion",font='Helvetica 8 bold').place(x=400,y=110)
        #===================Escritorio =============================================
        Label09 = Label(self.frame_main,text="Escritorio",font='Helvetica 12 bold').place(x=5,y=170)
        Label010 = Label(self.frame_main,text="ID",font='Helvetica 8 bold').place(x=120,y=170)
        Label011 = Label(self.frame_main,text="Identificacion",font='Helvetica 8 bold').place(x=215,y=170)
        Label012 = Label(self.frame_main,text="Encargado",font='Helvetica 8 bold').place(x=400,y=170)
        #===================transaccion =============================================
        Label013 = Label(self.frame_main,text="transaccion",font='Helvetica 12 bold').place(x=5,y=230)
        Label014 = Label(self.frame_main,text="ID",font='Helvetica 8 bold').place(x=120,y=230)
        Label015= Label(self.frame_main,text="Nombre",font='Helvetica 8 bold').place(x=220,y=230)
        Label016 = Label(self.frame_main,text="tiempoAtencion",font='Helvetica 8 bold').place(x=400,y=230)

        pass
    #===============================================================================
    def verificar_Empresa(self,tabla):
        cursor = tabla.focus()
        dic = tabla.item(cursor)
        if dic["text"] == "":
            mb = showerror("Error","Seleccione una Empresa")
            return
        temp = self.lista_config.primero
        while temp != None:
            if temp.dato.id_empresa == dic["text"]:
                self.temporal_punto = dic["text"]
                verificar_punto = Button(self.frame_main,text="Aplicar prueba punto",command=lambda:self.verificar_Punto(tabla)).place(x= 180, y = 300)
                return
                pass
            temp = temp.siguiente
        mb = showerror("Error","Esta empresa no tiene una prueba")
        
    def verificar_Punto(self,tabla):
        cursor = tabla.focus()
        dic = tabla.item(cursor)
        if dic["text"] == "":
            mb = showerror("Error","Seleccione un Punto")
            return
        temp = self.lista_empresa.primero
        #=============================================
        while temp != None:
            if temp.dato.get_id() == self.temporal_punto:
                #====================================
                temp2 = temp.dato.get_punto().primero
                while temp2 != None:
                    if temp2.dato.get_id() == dic["text"]:
                        #============================
                        temp3 = self.lista_config.primero
                        while temp3 != None:
                            if temp3.dato.id_empresa == self.temporal_punto:
                                if temp3.dato.id_punto == dic["text"]:
                                    #=== temp2.dato.listescritorios , temp3.dato.listEscriActivos
                                    temp4 = temp2.dato.listescritorios.primero
                                    while temp4 != None:
                                        temp5 = temp3.dato.listEscriActivos.primero
                                        while temp5 != None:
                                            if temp4.dato.get_id() == temp5.dato.id:
                                                temp4.dato.estado = True
                                            temp5 = temp5.siguiente
                                        temp4 = temp4.siguiente
                                    pass
                            temp3 = temp3.siguiente
                        #============================
                    temp2 = temp2.siguiente
                #=========================================
            temp = temp.siguiente
        #====================================================
        self.mostrarEmpresas()
    def seleccionar_Escritorio(self,tabla):
        try:
            cursor = tabla.focus()
            dic = tabla.item(cursor)
            list_dic = dic["text"].split(" ")
            if dic["values"][2] == "Inactivo":
                mb = showerror("Error","Este escritorio esta Inactivo no se puede iniciar la simulacion")
                return
            resul = self.lista_empresa.busquedaEmpresa(list_dic[1],list_dic[2],list_dic[0],self.lista_config)
            simula = Simulacion()
            simula.Atencion_clientes(resul[0],resul[1],resul[2])
        except IndexError:
            pass
          
    def mostrarEmpresas(self):
        self.windown_main.geometry("900x400")
        self.frame_main.config(width=900,height=400)
        for iter in self.frame_main.winfo_children():
            iter.destroy()
        label01 = Label(self.frame_main,text="Datos Empresa",font='Helvetica 10 bold').place(x=100,y= 10)
        label01 = Label(self.frame_main,text="Datos Prueba",font='Helvetica 10 bold').place(x=500,y= 10)
        verificar_punto = Button(self.frame_main,text="Aplicar prueba punto",state=DISABLED).place(x= 180, y = 300)
        seleccionar_escritorio = Button(self.frame_main,text="Seleccionar Escritorio",command=lambda:self.seleccionar_Escritorio(tabla)).place(x= 340, y = 300)
        Verificar_empresa = Button(self.frame_main,text="Verificar Empresa",command=lambda:self.verificar_Empresa(tabla)).place(x= 50, y = 300)
        tabla = Treeview(self.frame_main,columns=("col1","col2","col3"))
        tabla.pack()
        tabla.place(x=0,y=40)
        tabla.column("#0",width=75)
        tabla.column("col1",width=120,anchor=CENTER)
        tabla.column("col2",width=120,anchor=CENTER)
        tabla.column("col3",width=60,anchor=CENTER)
        tabla.heading("#0",text="ID", anchor=CENTER)
        tabla.heading("col1",text="Nombre", anchor=CENTER)
        tabla.heading("col2",text="Abreviatura", anchor=CENTER)
        tabla.heading("col3",text="Estado", anchor=CENTER)
        for delete1 in tabla.get_children():
            tabla.delete(delete1)
        temp2 = self.lista_empresa.primero
        while temp2 != None:
            id = tabla.insert("",END,text=temp2.dato.get_id(),values=(temp2.dato.get_nombre(),temp2.dato.get_abre()))
            temp3 = temp2.dato.get_punto().primero
            while temp3 != None:
                id2 = tabla.insert(id,END,text=temp3.dato.get_id(),values=(temp3.dato.get_nombre(),temp3.dato.get_direc()))
                temp4 = temp3.dato.listescritorios.primero
                while temp4 != None:
                    if temp4.dato.estado == True:
                        temporal = "Activo"
                    else: 
                        temporal = "Inactivo"
                    tabla.insert(id2,END,text=[temp4.dato.get_id(),temp2.dato.get_id(),temp3.dato.get_id()],values=(temp4.dato.identificacion,temp4.dato.encargado,temporal))
                    temp4 = temp4.siguiente
                temp3 = temp3.siguiente
            temp2 = temp2.siguiente
        #========================================= Datos Prueba ===================================================
        tabla1 = Treeview(self.frame_main,columns=("col1","col2"))
        tabla1.pack()
        tabla1.place(x=440,y=40)
        tabla1.column("#0",width=150)
        tabla1.column("col1",width=80,anchor=CENTER)
        tabla1.column("col2",width=80,anchor=CENTER)
        tabla1.heading("#0",text="ID configInicial", anchor=CENTER)
        tabla1.heading("col1",text="ID Empresa", anchor=CENTER)
        tabla1.heading("col2",text="ID Punto ", anchor=CENTER)
        
        for delete1 in tabla1.get_children():
            tabla1.delete(delete1)
        temp2 = self.lista_config.primero
        while temp2 != None:
            id = tabla1.insert("",END,text=temp2.dato.id,values=(temp2.dato.id_empresa,temp2.dato.id_punto))
            temp4 = temp2.dato.listEscriActivos.primero
            id2 = tabla1.insert(id,END,text="Escritorios")
            while temp4 != None:
                tabla1.insert(id2,END,text=temp4.dato.id)
                temp4 = temp4.siguiente
            temp3 = temp2.dato.listclientes.primero
            id3 = tabla1.insert(id,END,text="Clientes")
            while temp3 != None:
                tabla1.insert(id3,END,text=temp3.dato.dpi)
                temp3 = temp3.siguiente
            temp2 = temp2.siguiente
        
    def ejecutar_ventana(self):
        #***********************Menu Bar******************************#
        self.Archivo.add_command(label="Cargar Archivo de Entrada",command=self.cargarConfi)
        self.Archivo.add_command(label="Cargar Archivo de Prueba",command=self.cargarPrueba)
        self.Options.add_command(label="Agregar Empresa",command=self.Agregar_Empresa)
        self.Options.add_command(label="Limpiar Sistema",command=self.limpiar)
        self.Options.add_command(label="Mostrar Datos",command=self.mostrarEmpresas)
        self.menubar.add_cascade(label="Archivo", menu=self.Archivo)
        self.menubar.add_cascade(label="Options", menu=self.Options)
        self.windown_main.config(menu= self.menubar)
        ###############################################################
        
        self.windown_main.title("Proyecto 2")
        self.frame_main.pack()
        self.windown_main.geometry("1000x400")
        self.windown_main.mainloop()