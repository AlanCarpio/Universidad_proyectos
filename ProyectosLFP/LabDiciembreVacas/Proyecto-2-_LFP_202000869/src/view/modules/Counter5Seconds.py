from tkinter import *
from time import sleep
from view.modules.MenuBar import MenuBar
from PIL import Image,ImageTk
class Counter5Seconds():
    def __init__(self,Win,Master,dataGRC,dataAUP) -> None:
        self.Master = Master
        self.Master_win = Win
        self.dataGRC = dataGRC
        self.dataAUP = dataAUP
        self.LabelNumber = Label(self.Master,text=5,font='calibri 32 bold')
        self.StartBotton = Button(self.Master,text='Start',font='calibri 24 bold',command=self.CuentaRegresiva)
        self.StartBotton.pack()
        self.StartBotton.place(x=340,y=200)
        self.LabelNumber.pack()
        self.LabelNumber.place(x=380,y=120)
        pass
    def CuentaRegresiva(self):
        cont = 5
        while cont > 0:
            cont -= 1
            self.LabelNumber.config(text=cont)
            sleep(1)
            self.Master_win.update()
        sleep(1)
        self.Master_win.update()
        self.MenuBar = MenuBar(self.Master_win,self.Master,self.dataGRC,self.dataAUP)
        self.MenuBar.Insert_sub_elements_bar()
        self.ImagePatch = 'C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos/compi.png'
        self.Image = Image.open(self.ImagePatch)
        self.Image = self.Image.resize((800,350),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.Image)
        self.LabelImage = Label(self.Master,image=self.img)
        self.LabelImage.pack()
        self.LabelImage.place(x=0,y= 0)
