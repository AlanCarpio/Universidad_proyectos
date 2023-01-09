from tkinter import filedialog
from tkinter.messagebox import showinfo
from controller.ReadFile import ReadFile
import subprocess

def OpenFile_Gra_Libre_Contx(database_AFD):
    ruta_archivo = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
    if ruta_archivo != "":
        fichero = open(ruta_archivo, 'r')
        contenido = fichero.read()
    else:    
        return showinfo(title="Alert",message="Seleccione un archivo")
    
    scanner = ReadFile(database_AFD,'',contenido)
    scanner.ReadFile_GRC()
    showinfo('Noti',"Archivo Leido Correctamente")

def OpenFile_AUTO_P(data_AUP):
    ruta_archivo = filedialog.askopenfilename(initialdir = "/",title = "Seleccione un Archivo")
    if ruta_archivo != "":
        fichero = open(ruta_archivo, 'r')
        contenido = fichero.read()
    else:    
        return showinfo(title="Alert",message="Seleccione un archivo")
    scanner = ReadFile('',data_AUP,contenido)
    scanner.ReadFile_AUP()
    showinfo('Noti',"Archivo Leido Correctamente")
def Abrir_AFD_Ayuda():
    path = "C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-1-_LFP_202000869/Documentation/AFD_Ayuda.pdf"
    subprocess.Popen([path], shell=True)
def Abrir_GR_Ayuda():
    path = "C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-1-_LFP_202000869/Documentation/GR_Ayuda.pdfF"
    subprocess.Popen([path], shell=True)