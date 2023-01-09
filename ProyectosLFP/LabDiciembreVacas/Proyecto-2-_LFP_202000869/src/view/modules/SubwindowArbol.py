from tkinter import *
from PIL import Image,ImageTk
from controller.GramaticaLibre.GenerarArbol import GenerarArbol
class SubwindowArbol():
    def __init__(self,Name_GRC,data_GRC) -> None:
        generarArbol = GenerarArbol(Name_GRC,data_GRC)
        generarArbol.BuildTree()
        self.SubVentana = Toplevel()
        self.SubVentana.title('Arbol')
        self.SubVentana.config(width=250 ,height= 650)
        self.FrameImage = Frame(self.SubVentana,width=200,height=600)
        self.ImagePatch = 'C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos/Gramatica.gv.png'
        self.Image = Image.open(self.ImagePatch)
        self.Image = self.Image.resize((200,600),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.Image)
        self.LabelImage = Label(self.FrameImage,image=self.img)
        self.LabelImage.pack()
        self.LabelImage.place(x=0,y= 0)
        self.FrameImage.pack()
        self.FrameImage.place(x=10,y=10)
        self.SubVentana.mainloop()
        pass