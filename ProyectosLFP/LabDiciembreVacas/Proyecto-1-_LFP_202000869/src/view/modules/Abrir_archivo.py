
from tkinter import filedialog
from tkinter.messagebox import showinfo
from src.controller.Read_file import Read_File
import subprocess

def scanner_contenido_AFD(database_AFD):
    ruta_archivo = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
    if ruta_archivo != "":
        fichero = open(ruta_archivo, 'r')
        contenido = fichero.read()
    else:    
        return showinfo(title="Alert",message="Seleccione un archivo")
    
    scanner = Read_File(contenido)
    scanner.scanner_AFD(database_AFD)
    showinfo('Noti',"Archivo Leido Correctamente")

def scanner_contenido_GR(database_GR):
    ruta_archivo = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
    if ruta_archivo != "":
        fichero = open(ruta_archivo, 'r')
        contenido = fichero.read()
    else:    
        return showinfo(title="Alert",message="Seleccione un archivo")
    scanner = Read_File(contenido)
    scanner.scanner_GR(database_GR)
    showinfo('Noti',"Archivo Leido Correctamente")
def Abrir_AFD_Ayuda():
    path = "C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-1-_LFP_202000869/Documentation/AFD_Ayuda.pdf"
    subprocess.Popen([path], shell=True)
def Abrir_GR_Ayuda():
    path = "C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-1-_LFP_202000869/Documentation/GR_Ayuda.pdfF"
    subprocess.Popen([path], shell=True)