from Automata import*
from Pagina import*
import re
from tkinter import*
from tkinter import filedialog
from tkinter.messagebox import showerror, showinfo
import os
window_main = Tk()
window_main.geometry("800x400")
window_main.title("Analizador Lexico")
frame_main = Frame(window_main,width=800,height=400,relief=RAISED,bd=20)
frame_main.pack()
fondo = PhotoImage(file="fondo.gif")
label_image = Label(frame_main,image=fondo,width=800,height=400)
label_image.pack()
def Abrir_manual_usuario():
    path = "Manual_de_Usuario.pdf"
    os.system(path)
    pass
def Abrir_manual_tecnico():
    path = 'Manual_Tecnico.pdf'
    os.system(path)
    pass
def Abrir():
    filename = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
    def Analizar(ruta_archivo):
        cadena =  open(ruta_archivo, 'r').read()   
        automota1 = automota()
        automota1.analizar(cadena)
        html = pagina()
        htmlpag = html.pagina_html(automota1)
        asd = open("ht.html","w")       
        asd.write(htmlpag)
        noti = showinfo("Notificacion","Analisis hecho exitosamente \n HTML Generado")        
    def Guardar(ruta_archivo):
        text_guardar = entry.get(1.0,"end")
        with open(ruta_archivo, 'w') as f:
            f.write(text_guardar)
        f.close()
        show_asd = showinfo("Notificacion","Guardado Exitosamente")
    def Guardar_como():
        text_guardar = entry.get(1.0,"end")
        filename = filedialog.asksaveasfilename(initialdir = "/",title = "Seleccione la ruta_archivo")
        filename+=".txt"
        asd = open(filename,"w")       
        asd.write(text_guardar)
        show_asd = showinfo("Notificacion","Guardado Exitosamente")
    for iter in frame_main.winfo_children():
        iter.destroy()
    entry = Text(frame_main,height=20,width=75,relief=RAISED)
    guardar = Button(frame_main,text="Guardar",command=lambda:Guardar(ruta_archivo)).place(x = 650, y= 50)
    guardar_como = Button(frame_main,text="Guardar Como",command=Guardar_como).place(x = 650, y= 100)
    analizar = Button(frame_main,text="Analizar",command=lambda:Analizar(ruta_archivo)).place(x = 650, y= 150)
    entry.pack()
    entry.place(x=0,y=0)
    ruta_archivo = filename
    if ruta_archivo != "":  
        fichero = open(ruta_archivo, 'r')
        contenido = fichero.read()
        entry.delete(1.0, 'end')           
        entry.insert('insert', contenido)  
        fichero.close()                        
#============================================================================
menubar = Menu(window_main)
Archivo = Menu(menubar)
Ayuda = Menu(menubar)
Ayuda.add_command(label="Manual de Usuario",command=Abrir_manual_usuario)
Ayuda.add_command(label="Manual Tecnico",command=Abrir_manual_tecnico)
Archivo.add_command(label="Abrir",command=Abrir)
Archivo.add_command(label="Salir",command=window_main.destroy)
menubar.add_cascade(label="Archivo", menu=Archivo)
menubar.add_cascade(label="Ayuda", menu=Ayuda)
window_main.config(menu=menubar)
window_main.mainloop()