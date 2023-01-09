from asyncore import write
import os
import sys
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo
from tkinter.ttk import Treeview
import xml.etree.ElementTree as ET
from tkinter import *
from xmlrpc.client import Boolean 
from Nodo import *
from Paciente import paciente
Pacientes = []
#================================= Busqueda de Datos en el XML=========================
def cargar_archivo():
  try:  
    ruta = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
    tree = ET.parse(ruta)
    root = tree.getroot()
    for raiz in root.findall("paciente"):
      datospersonales = raiz.findall("datospersonales")
      periodo = raiz.find("periodos").text
      m = raiz.find("m").text
      for datos in datospersonales:
        nombre = datos.find("nombre").text
        edad =  datos.find("edad").text
      lista2 = []
      lista2.append([])
      for i in range (int(m)):
        lista2[0].append([])
        for j in range (int(m)):
          lista2[0][i].append(0)
      for celda in raiz.iter("celda"):
        f = (int(celda.get("f")))
        c = (int(celda.get("c")))
        lista2[0][f][c] = 1
      ObjP = paciente(nombre,edad,periodo,m,lista2)
      Pacientes.append(ObjP)
    mb = showinfo("Notificacion","Datos Cargados Exitosamente")
  except FileNotFoundError:
    mberror = showerror("Notificacion","Seleccione un Archivo")
    return    
#===================================================================================
def pacientes(frame_pacientes):
  contpaciimpri = 0
  def imprimir_datos(arbol,size_canvas,frame_tablero):
    cursor = arbol.focus()
    dic = arbol.item(cursor)
    if len(Pacientes) == 0:
      s = showerror("Error","Cargue un Archivo")
      return
    if dic["text"] == "":
      mb = showerror("Error","Seleccione un Paciente")
      return
    for lol in Pacientes:
      if dic["text"] == lol.get_nombre():
        if int(lol.get_imprimir()) == 1:
          imprimirnoti = showinfo("Notificacion","A este paciente ya se ah hecho una simulacion")
          return
        lista = ListaEnlazada(lol.get_m()) 
        #============ LLenado de datos =========================
        if int(lol.get_periodo()) == lol.get_contador():
          comprobar_matriz(lol)
          lol.set_imprimir()
          generarxml = Button(frame_pacientes,text="Generar XML",command=archivo_salida,state="normal",foreground="red",font="Arial",relief=RAISED,bd=3).place(x=420,y=300)
          error = showinfo("Notificacion","Ya no hay mas periodos a evaluar")
          return
        lol.aumentar_contador(1)
        paciente_Entry.set("Periodo: {}".format(lol.get_contador()))
        
        w = lol.get_m()
        u = (size_canvas/w)
        tablero.delete(ALL)
        for x in range(lol.get_m()):
          for y in range(lol.get_m()):
            lista.insertar(lol.get_lista()[lol.get_contador()][x][y])
            if lol.get_lista()[lol.get_contador()][x][y] == 1:
              color = "green"
            else:
              color = "blue"
            tablero.create_rectangle(y*u,x*u,(y+2)*u,(x+2)*u,fill=color)
            frame_tablero.update()
        
        lista.comprobacion(lol.get_m(),lol)
  def comprobar_matriz(iter):
    bolan = False
    for i in range(len(iter.get_lista())):
      if i!=0:
        if i==1 and iter.get_lista()[0] == iter.get_lista()[i]:
          enfermedad__entry.set("Estado de la Enfermedad:{}".format("Mortal"))
          n__entry.set("N:{}".format(i))
          iter.set_estado("Mortal")
          iter.set_n(i)
          return
    bolan = True
    if bolan == True:
      for w in range(len(iter.get_lista())):
        for y in range(w,len(iter.get_lista())):
          if w!=y:
            if iter.get_lista()[w] == iter.get_lista()[y] and w==y-1:
              enfermedad__entry.set("Estado de la Enfermedad:{}".format("Mortal"))
              n__entry.set("N:{}".format(w))
              n1__entry.set("N1:{}".format(1))
              iter.set_estado("Mortal")
              iter.set_n(w)
              iter.set_n1(1)
              return
            elif iter.get_lista()[w] == iter.get_lista()[y]:
              enfermedad__entry.set("Estado de la Enfermedad:{}".format("Grave"))
              n__entry.set("N:{}".format(w))
              n1__entry.set("N1:{}".format(y))
              iter.set_estado("Grave")
              iter.set_n(w)
              iter.set_n1(y)
              return    
    enfermedad__entry.set("Estado de la Enfermedad:{}".format("Leve"))
    iter.set_estado("Leve")
  def seleccionar_paciente(arbol,analizar):
    cursor = arbol.focus()
    dic = arbol.item(cursor)
    if len(Pacientes) == 0:
      s = showerror("Error","Cargue un Archivo")
      return
    if dic["text"] == "":
      mb = showerror("Error","Seleccione un Paciente")
      return
    for iter in Pacientes:
      if dic["text"] == iter.get_nombre():
        lista = ListaEnlazada(iter.get_m()) 
        w = iter.get_m()
        u = (size_canvas/w)
        tablero.delete(ALL)
        for x in range(iter.get_m()):
          for y in range(iter.get_m()):
            lista.insertar(iter.get_lista()[0][x][y])
            if iter.get_lista()[0][x][y] == 1:
              color = "green"
            else:
              color = "blue"
            tablero.create_rectangle(y*u,x*u,(y+2)*u,(x+2)*u,fill=color)
            frame_tablero.update()
        lista.comprobacion(iter.get_m(),iter)
        enfermedad__entry.set("Estado de la Enfermedad:{}".format(""))
        paciente_Entry.set("Periodo: {}".format(iter.get_contador())) 

    analizar = Button(frame_pacientes,text="Analizar",command=lambda:imprimir_datos(tabla,size_canvas,frame_tablero),state="normal",foreground="red",font="Arial",relief=RAISED,bd=3).place(x=420,y=520)
  def archivo_salida():
    root = ET.Element("Pacientes")
    for iter in Pacientes:
      if iter.get_imprimir() == 1:
        paciente = ET.Element("Paciente")
        #=======================================================
        datosperso = ET.SubElement(paciente,"Datospersonales")
        nombre = ET.SubElement(datosperso,"Nombre")
        nombre.text = str(iter.get_nombre())
        edad = ET.SubElement(datosperso,"Edad")
        edad.text = str(iter.get_edad())
        #=======================================================
        periodos = ET.SubElement(paciente,"Periodos")
        periodos.text = str(iter.get_periodo())
        m = ET.SubElement(paciente,"m")
        m.text = str(iter.get_m())
        #=======================================================
        resultado = ET.SubElement(paciente,"Resultado_del_simulador")
        estado = ET.SubElement(resultado,"Estado")
        estado.text = str(iter.get_estado())
        n = ET.SubElement(resultado,"n")
        n.text = str(iter.get_n())
        n1 = ET.SubElement(resultado,"n1")
        n1.text = str(iter.get_n1())
        #=======================================================
        root.append(paciente)
    arbol = ET.ElementTree(root)
    arbol.write("Pacientes.xml")
    
    
    
    pass
  for widget in frame_pacientes.winfo_children():
    widget.destroy()
  frame_tablero = Frame(frame_pacientes,width=600,height=350)
  frame_tablero.pack()
  frame_tablero.place(x=0 ,y= 250)
  size_canvas = 300
  tablero = Canvas(frame_tablero,width=size_canvas,height=size_canvas,highlightbackground="black")
  tablero.pack()
  tablero.place(x=25,y=25)
  tabla = Treeview(frame_pacientes,columns=("col1","col2","col3"))
  tabla.pack()
  tabla.place(x=0,y=0)
  tabla.column("#0",width=150)
  tabla.column("col1",width=80,anchor=CENTER)
  tabla.column("col2",width=80,anchor=CENTER)
  tabla.column("col3",width=80,anchor=CENTER)
  tabla.heading("#0",text="Nombre", anchor=CENTER)
  tabla.heading("col1",text="Edad", anchor=CENTER)
  tabla.heading("col2",text="Periodos", anchor=CENTER)
  tabla.heading("col3",text="Rejilla", anchor=CENTER)
  for delete1 in tabla.get_children():
    tabla.delete(delete1)
  for ite in Pacientes:
    tabla.insert("",END,text=ite.get_nombre(),values=(ite.get_edad(),ite.get_periodo(),ite.get_rejilla()))
  paciente_Entry = StringVar()
  enfermedad__entry = StringVar()
  n__entry = StringVar()
  n1__entry = StringVar()
  paciente_Entry.set("Periodo: {}".format(""))
  enfermedad__entry.set("Estado de la Enfermedad:{}".format(""))
  n__entry.set("N:{}".format(""))
  n1__entry.set("N1:{}".format(""))
  label_pacientes = Label(frame_pacientes,text="Simulador de Tejidos",font="Arial",foreground="red").place(x=200,y=230)
  label_selecionar = Label(frame_pacientes,text="Seleccione un \n Paciente de la tabla",font=("Arial",12),foreground="red").place(x=425,y= 20)
  analizar = Button(frame_pacientes,text="Analizar",command=lambda:imprimir_datos(tabla,size_canvas,frame_tablero),state="disabled",foreground="red",font="Arial",relief=RAISED,bd=3).place(x=420,y=520)
  seleccionar = Button(frame_pacientes,text="Seleccionar Paciente",command=lambda:seleccionar_paciente(tabla,analizar)).place(x=425,y=100)
  periodos_entry = Entry(frame_pacientes,textvariable=paciente_Entry,state="disabled",relief=RAISED,bd=3,width=10,font=("Arial",11)).place(x=420,y= 480)
  enfermedad_entry = Entry(frame_pacientes,textvariable=enfermedad__entry,state="disabled",relief=RAISED,bd=3,width=27,font=("Arial",8)).place(x=400,y= 390)
  n_entry = Entry(frame_pacientes,textvariable=n__entry,state="disabled",relief=RAISED,bd=3,width=10,font=("Arial",8)).place(x=420,y= 420)
  n1_entry = Entry(frame_pacientes,textvariable=n1__entry,state="disabled",relief=RAISED,bd=3,width=10,font=("Arial",8)).place(x=420,y= 450)
  generarxml = Button(frame_pacientes,text="Generar XML",command=archivo_salida,state="disabled",foreground="red",font="Arial",relief=RAISED,bd=3).place(x=420,y=300)
  frame_pacientes.pack()
#===============================Menu Principal======================================
def regresar():
  for widget in frame_pacientes.winfo_children():
    widget.destroy()
  frame_pacientes.pack()
  imagen_label = Label(frame_pacientes,image=celula)
  imagen_label.pack()
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
VentanaMenu = Tk()
VentanaMenu.geometry("650x650")
VentanaMenu.title("Simulador de tejido")
celula = PhotoImage(file="celula2.gif")
resource_path("celula2.gif")
frame_pacientes = Frame(VentanaMenu,width=600,height=600,relief=RAISED,bd=20)
imagen_label = Label(frame_pacientes,image=celula)
imagen_label.pack()
frame_pacientes.pack()
menubar = Menu(VentanaMenu)
filemenu = Menu(menubar)
filemenu.add_command(label="Cargar Archivo",command=cargar_archivo)
filemenu.add_command(label="Pagina de Inicio",command=regresar)
filemenu.add_command(label="Pacientes",command=lambda:pacientes(frame_pacientes))
menubar.add_cascade(label="Opciones", menu=filemenu)
VentanaMenu.config(menu=menubar)
VentanaMenu.mainloop()