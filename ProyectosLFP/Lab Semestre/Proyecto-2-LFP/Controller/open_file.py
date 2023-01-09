from tkinter import filedialog
from tkinter.messagebox import showinfo
def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
    if ruta_archivo != "":
        fichero = open(ruta_archivo, 'r')
        contenido = fichero.read()
    return [contenido,fichero,ruta_archivo]
def Guardar(ruta_archivo,entry):
    text_guardar = entry.get(1.0,"end")
    with open(ruta_archivo, 'w') as f:
        f.write(text_guardar)
    f.close()
    show_asd = showinfo("Notificacion","Guardado Exitosamente")
def Guardar_como(entry):
    text_guardar = entry.get(1.0,"end")
    filename = filedialog.asksaveasfilename(initialdir = "/",title = "Seleccione la ruta_archivo")
    filename+=".txt"
    asd = open(filename,"w")       
    asd.write(text_guardar)
    show_asd = showinfo("Notificacion","Guardado Exitosamente")
    