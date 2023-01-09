from msilib import Table
from Controller.open_file import abrir_archivo, Guardar,Guardar_como
from tkinter import*
from tkinter import filedialog
from tkinter.messagebox import askquestion, showerror, showinfo
from Controller.Analizador_lexico import scanner
from Controller.analizador_sintactico import parser
from Controller.create_html_css import create
from View.table import Tables
import subprocess

analisis_sictactico = parser()
analisis_lexico = scanner()
def Abrir_manual_usuario():
    path = "C:/Users/Krpi/Documents/Python/Proyecto-2-LFP/documentation/Manual_de_Usuario.pdf"
    subprocess.Popen([path], shell=True)

    pass
    
def Abrir_manual_tecnico():
    path = "C:/Users/Krpi/Documents/Python/Proyecto-2-LFP/documentation/Manual_Tecnico.pdf"
    subprocess.Popen([path], shell=True)

    pass
def nuevo(ruta):
    askQuestion = askquestion("Alert","Desea guardar los cambios antes de limpiar el editor")
    if askQuestion == "yes":    
        Guardar(ruta,entry)
        entry.delete(1.0, 'end')
    else:
        entry.delete(1.0, 'end')
    guardar.config(state=DISABLED)

    pass
def table_tokens_general():
    tabla = Tables(analisis_lexico,analisis_sictactico)
    tabla.placement_and_options()
    pass
def Analizar():
    cadena = entry.get(1.0,"end")
    analisis_lexico.analisis_lexico(cadena)
    datos_HTML = analisis_lexico.Get_data_HTML()
    datos_tokens = analisis_lexico.Get_data_tokens()              #datos de analisis lexico
    datos_tokens_malos = analisis_lexico.Get_data_tokens_malos().data
    analisis_sictactico.analisis_sintactico(datos_HTML,datos_tokens)
    datos_token_sin = analisis_sictactico.Get_tokens_sintactico()
    datos_tokens_malos_sin = analisis_sictactico.Get_tokens_malos_sintactico().data
    if len(datos_tokens_malos) != 0 or len(datos_tokens_malos_sin) != 0:
        alert = showerror("Alert","Se han detectado errores lexicos o sintacticos")
    else:
        Create = create(datos_HTML,datos_token_sin)
        Create.create_html()
        Create.create_css()
        noti = showinfo("Notification","Archivos Creados Exitosamente")

    pass
def Abrir():       
    for iter in frame_main.winfo_children(): #Limpiar Frame Main
        iter.pack_forget()
        iter.place_forget()
    #Abrir Archivo
    contenido = abrir_archivo()
    guardar_como.config(command=lambda:Guardar_como(entry))
    guardar.config(command=lambda:Guardar(contenido[2],entry),state=NORMAL) #configuracion de botones
    Nuevo.config(command=lambda:nuevo(contenido[2]))
    analizar.config(command=Analizar)
    entry.place(x=0,y=0)
    guardar.place(x = 650, y= 50)       #colocacion de botones
    guardar_como.place(x = 650, y= 100)
    analizar.place(x = 650, y= 150)
    Nuevo.place(x= 650, y = 200)
    entry.delete(1.0, 'end')           
    entry.insert('insert', contenido[0])  #insercion de contenido en el Text
    contenido[1].close()                        
#============================================================================
window_main = Tk()
window_main.geometry("800x400")
window_main.title("Main_windown")
frame_main = Frame(window_main,width=800,height=400,relief=RAISED,bd=20)
frame_main.pack()
guardar = Button(frame_main,text="Guardar")
guardar_como = Button(frame_main,text="Guardar Como")
analizar = Button(frame_main,text="Analizar")
Nuevo = Button(frame_main,text="Nuevo")
entry = Text(frame_main,height=20,width=75,relief=RAISED)
menubar = Menu(window_main)
Archivo = Menu(menubar)
Ayuda = Menu(menubar)


Ayuda.add_command(label="Manual de Usuario",command=Abrir_manual_usuario)
Ayuda.add_command(label="Manual Tecnico",command=Abrir_manual_tecnico)
Archivo.add_command(label="Abrir",command=Abrir)
Archivo.add_command(label="Tablas Tokens",command=table_tokens_general)
Archivo.add_command(label="Salir",command=window_main.destroy)
menubar.add_cascade(label="Archivo", menu=Archivo)
menubar.add_cascade(label="Ayuda", menu=Ayuda)
window_main.config(menu=menubar)
