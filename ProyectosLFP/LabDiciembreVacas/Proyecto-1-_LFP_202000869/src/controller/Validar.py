from tkinter.messagebox import showinfo
class Validar():
    def __init__(self,nombre_focus,cadena_solicitud,data_afd,data_gr) -> None:
        self.nombre_focus = nombre_focus
        self.cadena_solicitud = cadena_solicitud
        self.data_afd = data_afd
        self.data_gr = data_gr
        
        pass
    def Algoritmo_validar(self,iter,estado_inicial,char) -> str:
        for iter2 in iter.Get_transiciones():
            if estado_inicial == iter2.Get_entrada() and char == iter2.Get_estado():
                return iter2.Get_destino()
    def Validar_AFD(self):
        for iter in self.data_afd.Get_data():
            if iter.Get__Nombre() == self.nombre_focus:
                estado_inicial = iter.Get__Estado_inicial()
                while len(self.cadena_solicitud) > 0:
                    char = self.cadena_solicitud[0]
                    resul = self.Algoritmo_validar(iter,estado_inicial,char)
                    estado_inicial = resul
                    self.cadena_solicitud = self.cadena_solicitud[1:]
                for iter3 in iter.Get__Estado_Aceptacion().split(','):
                    if estado_inicial == iter3:
                        return showinfo("Notification","Cadena valida")
                return showinfo("Notification","Cadena invalida")
        pass
    def Validar_GR(self):
        for iter in self.data_gr.Get_data():
            if iter.Get__Nombre() == self.nombre_focus:
                estado_inicial = iter.Get__Estado_inicial()
                while len(self.cadena_solicitud) > 0:
                    char = self.cadena_solicitud[0]
                    resul = self.Algoritmo_validar(iter,estado_inicial,char)
                    estado_inicial = resul
                    self.cadena_solicitud = self.cadena_solicitud[1:]
                for iter3 in iter.Get__Estado_Aceptacion().split(','):
                    if estado_inicial == iter3:
                        return showinfo("Notification","Cadena valida")
                return showinfo("Notification","Cadena invalida")
        pass
    pass