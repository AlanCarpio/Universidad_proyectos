from tkinter import *
from src.view.modules.menu_bar import Menu_bar_window
from src.model.database import database
class Main_window():
    def __init__(self) -> None:
        #Base de datos para los AFD
        self.database_AFD = database()
        #Base de datos para los GR
        self.database_GR = database()
        self.main_window = Tk()
        self.frame_main = Frame(self.main_window,height=350,width=800)
        self.curso = Label(self.frame_main,text="Lenguajes Formales de la Programacion, Seccion: N",font="calibri 18 bold")
        self.nombre = Label(self.frame_main,text="Alan Misael Carpio Garcia",font="calibri 18 bold")
        self.carnet = Label(self.frame_main,text="202000869",font="calibri 18 bold")
        self.Menu_bar = Menu_bar_window(self.main_window,self.frame_main,self.database_AFD,self.database_GR)
        
        
        pass
    def Iniciar_ventana(self) -> None:
        # Menu Bar
        self.Menu_bar.Insert_sub_elements_bar(self.main_window,self.database_AFD,self.database_GR)
        self.main_window.geometry("800x350")
        self.main_window.title("Proyecto 1")
        self.frame_main.pack()
        self.frame_main.place(x=0,y=0)
        self.curso.pack()
        self.curso.place(x=200,y=100)
        self.nombre.pack()
        self.nombre.place(x=200,y=150)
        self.carnet.pack()
        self.carnet.place(x=200,y=200)
        self.main_window.mainloop()
    
   
