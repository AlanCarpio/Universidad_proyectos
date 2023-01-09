from tkinter import *

#from view.modules.MenuBar import MenuBar
from view.modules.Counter5Seconds import Counter5Seconds
from view.modules.LabelsMain import LabelsMain
class WindowMain(Frame):
    def __init__(self) -> None:
        self.data_GRC = []
        self.data_AUP = []
        self.Master = Tk()
        self.MasterFrame = Frame(self.Master,height=350,width=800)
        #self.MenuBar = MenuBar(self.Master,self.MasterFrame,self.data_GRC,self.data_AUP)
        
        labelmains = LabelsMain(self.MasterFrame)
        labelmains.Labels()
        Counter5Seconds(self.Master,self.MasterFrame,self.data_GRC,self.data_AUP)
       
        pass
    def Iniciar_ventana(self) -> None:
        # Menu Bar
        #self.MenuBar.Insert_sub_elements_bar()
        self.Master.geometry("800x350")
        self.Master.title("Proyecto 2")
        self.MasterFrame.pack()
        self.MasterFrame.place(x=0,y=0)
        self.Master.mainloop()
        
        
        