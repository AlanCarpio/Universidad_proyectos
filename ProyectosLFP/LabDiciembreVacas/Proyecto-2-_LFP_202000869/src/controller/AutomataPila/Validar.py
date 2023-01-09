from tkinter.messagebox import showinfo
class Validar():
    
    def __init__(self,nombre_focus,cadena_solicitud,data_AUP) -> None:
        self.nombre_focus = nombre_focus
        self.cadena_solicitud = cadena_solicitud
        self.data_AUP = data_AUP
        self.pila = []
        pass
    def Algoritmo_validar(self,iter,estado_inicial,char) -> str:
        resul = iter.Get_info()
        for iter2 in resul[6]:
            resul2 = iter2.Get_All()
            if estado_inicial == resul2[0] and char == resul2[2][0]:
                if resul2[2][2] != '$':
                    self.pila.append(resul2[2][2])
                try:
                    if resul2[2][1] != '$':
                        self.pila.remove(resul2[2][1])
                except ValueError:
                    return 
                self.cadena_solicitud = self.cadena_solicitud[1:]
                return resul2[1]
            elif estado_inicial == resul2[0] and resul2[2][0] == '$':
                if resul2[2][2] != '$':
                    self.pila.append(resul2[2][2])
                try:
                    if resul2[2][1] != '$':
                        self.pila.remove(resul2[2][1])
                except ValueError:
                    return 
                return resul2[1]
        self.cadena_solicitud = self.cadena_solicitud[1:]
            

    def Validar_AUP(self):
        
        for iter in self.data_AUP:
            resul = iter.Get_info()
            if resul[0] == self.nombre_focus:
                estado_inicial = resul[4]
                while len(self.cadena_solicitud) > 0:
                    char = self.cadena_solicitud[0]
                    estado_inicial2 = self.Algoritmo_validar(iter,estado_inicial,char)
                    estado_inicial = estado_inicial2
                for iter3 in resul[5].split(','):
                    for iter4 in resul[6]:
                        resul2 = iter4.Get_All()
                        if resul2[2][0] == '$' and iter3 == resul2[1] and estado_inicial == resul2[0]:
                            if resul2[2][2] != '$':
                                self.pila.append(resul2[2][2])
                            try:
                                if resul2[2][1] != '$':
                                    self.pila.remove(resul2[2][1])
                            except ValueError:
                                return showinfo("Notification","Cadena invalida") 
                            if self.pila != []:
                                return showinfo("Notification","Cadena invalida") 
                            return showinfo("Notification","Cadena valida")
                    if estado_inicial == iter3:
                        if resul2[2][2] != '$':
                            self.pila.append(resul2[2][2])
                        try:
                            if resul2[2][1] != '$':
                                self.pila.remove(resul2[2][1])
                        except ValueError:
                            return showinfo("Notification","Cadena invalida") 
                        if self.pila != []:
                            return showinfo("Notification","Cadena invalida") 
                        return showinfo("Notification","Cadena valida")
                return showinfo("Notification","Cadena invalida")
        pass