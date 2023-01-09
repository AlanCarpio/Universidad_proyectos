from tkinter import*
from PIL import Image,ImageTk
from controller.AutomataPila.RutaPasada import RutaPasada
class SubWindowRutaPasada():
    def __init__(self,Name_AUP,data_AUP,cadena_ruta,Estado) -> None:
        self.Estado = Estado
        self.EstadoCadena = 2
        self.Transiciones = cadena_ruta
        self.CadenaRuta = cadena_ruta
        self.Estado_actual = ''
        self.Estado_Siguiente = ''
        self.Estado_While = True
        self.char = self.CadenaRuta[0]
        self.char = self.char.split(',')
        self.CadenaRuta = self.CadenaRuta[1:]
        self.Estado_actual = self.char[0]
        self.Estado_Siguiente = self.char[4]
        self.pas = RutaPasada(Name_AUP,data_AUP,self.Transiciones)
        self.pas.GrafoPasoaPaso('     ')
        self.Siguiente()
        
        pass
    
    def Siguiente(self):
        if self.Estado_While:
            self.Estado_While = self.pas.GrafoPasoaPaso(self.char)
            if len(self.CadenaRuta) > 0:
                self.char = self.CadenaRuta[0]
                self.char = self.char.split(',')
                self.Estado_actual = self.char[0]
                self.Estado_Siguiente = self.char[4]
                self.CadenaRuta = self.CadenaRuta[1:]
            else:
                #0 cadena Invalida
                #1 cadena Valida
                #2 cadena Indefinida
                if self.Estado == 'Cadena Invalida':
                    self.pas.Get_Pila()
                    self.SubVentana = Toplevel()
                    self.SubVentana.title('Paso A paso')
                    self.SubVentana.config(width=600 ,height= 300)
                    self.FrameImage = Frame(self.SubVentana,width=580,height=300)
                    self.ImagePatch = 'C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos/RutaPasada.gv.png'
                    self.Image = Image.open(self.ImagePatch)
                    self.Image = self.Image.resize((580,200),Image.ANTIALIAS)
                    self.img = ImageTk.PhotoImage(self.Image)
                    self.LabelImage = Label(self.FrameImage,image=self.img)
                    self.LabelImage.pack()
                    self.LabelImage.place(x=0,y= 0)
                    self.FrameImage.pack()
                    self.FrameImage.place(x=10,y=10)
                    self.SubVentana.mainloop()
                    return
                                        
                else:
                    self.pas.Get_Pila()
                    self.SubVentana = Toplevel()
                    self.SubVentana.title('Paso A paso')
                    self.SubVentana.config(width=600 ,height= 320)
                    self.FrameImage = Frame(self.SubVentana,width=580,height=320)
                    self.ImagePatch = 'C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos/RutaPasada.gv.png'
                    self.Image = Image.open(self.ImagePatch)
                    self.Image = self.Image.resize((580,300),Image.ANTIALIAS)
                    self.img = ImageTk.PhotoImage(self.Image)
                    self.LabelImage = Label(self.FrameImage,image=self.img)
                    self.LabelImage.pack()
                    self.LabelImage.place(x=0,y= 0)
                    self.FrameImage.pack()
                    self.FrameImage.place(x=10,y=10)
                    self.SubVentana.mainloop()
                    return
                    
            self.Siguiente()
                    