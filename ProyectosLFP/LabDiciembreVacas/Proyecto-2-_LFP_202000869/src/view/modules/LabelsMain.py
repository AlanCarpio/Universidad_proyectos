from tkinter import *
class LabelsMain ():
    def __init__(self,Master) -> None:
        self.Master = Master
        pass
    def Labels(self):
        for iter in self.Master.winfo_children():
            iter.destroy()
        self.curso = Label(self.Master,text="Lenguajes Formales de la Programacion, Seccion: N",font="calibri 16 bold")
        self.nombre = Label(self.Master,text="Alan Misael Carpio Garcia",font="calibri 16 bold")
        self.carnet = Label(self.Master,text="202000869",font="calibri 16 bold")
        self.LabelsPack()
    def LabelsPack(self):
        self.curso.pack()
        self.curso.place(x=0,y=0)
        self.nombre.pack()
        self.nombre.place(x=0,y=50)
        self.carnet.pack()
        self.carnet.place(x=0,y=100)