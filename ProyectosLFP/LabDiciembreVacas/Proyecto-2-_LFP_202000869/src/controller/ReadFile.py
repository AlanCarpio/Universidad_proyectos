from model.GramaticaLibre.Producciones import Producciones
from model.GramaticaLibre.Gramatica import Gramatica
from model.AutomataPila.Automata import Automata
from model.AutomataPila.Transiciones import Transiciones
class ReadFile():
    def __init__(self,data_GRC,data_AUP,cadena) -> None:
        self.data_GRC = data_GRC
        self.data_AUP = data_AUP
        self.Estado = 0
        self.cadena = cadena
        self.Chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ñ","_","1","2","3","4","5","6","7","8","9","0",'$','#']
        pass
    def ReadFile_GRC(self):
        self.Estado = 0
        token = ''
        producciones = []
        #Declaracion de Variables Nombre Etc..
        Nombre = ''
        No_Terminales = ''
        Terminales = ''
        Nti = ''
        #Declaracion de variable Producciones
        Origen = ''
        Destinos = []
        ComprovacionGramatica = []
        #======================
        apertura_nombre = True
        apertura_No_Terminales = True
        apertura_Terminales = True
        apertura_Nti = True
        
        while len(self.cadena) > 0: 
            char = self.cadena[0]
            # Escargado de Nombre etc../
            #Estado 0
            if self.Estado == 0:
                if char == '\n':
                    if apertura_nombre:
                        Nombre = token
                        apertura_nombre = False
                        token = ''
                    elif apertura_No_Terminales:
                        No_Terminales = token
                        apertura_No_Terminales = False
                        token = ''
                    elif apertura_Terminales:
                        Terminales = token
                        apertura_Terminales = False
                        token = ''
                    elif apertura_Nti:
                        Nti = token
                        apertura_Nti = False
                        token = ''
                        self.Estado = 1
                        self.cadena = self.cadena[1:]
                        continue
                elif char == ' ':
                    self.cadena = self.cadena[1:]
                    continue
                elif char.lower() in self.Chars:
                    token += char
            #Estado 1
            elif self.Estado == 1:
                if char == '\n':
                    Destinos.append(token)
                    ComprovacionGramatica.append(Destinos)
                    produc = Producciones(Origen,Destinos)
                    producciones.append(produc)
                    Origen = ''
                    token = ''
                    Destinos = []
                    pass
                elif char.lower() in self.Chars:
                    token += char
                elif char == ' ':
                    Destinos.append(token)
                    token = ''
                    pass
                elif char == '%':
                    
                    Guardar = False
                    for iter in ComprovacionGramatica:
                        if len(iter) >= 3:
                            Guardar = True
                    if Guardar:
                        gramatica = Gramatica(Nombre,No_Terminales,Terminales,Nti,producciones)
                        self.data_GRC.append(gramatica)
                    ComprovacionGramatica = []
                    apertura_nombre = True
                    apertura_No_Terminales = True
                    apertura_Terminales = True
                    apertura_Nti = True
                    producciones = []
                    self.cadena = self.cadena[1:]
                    self.cadena = self.cadena[1:]
                    self.Estado = 0
                    continue
                    pass
                elif char == '>':
                    Origen = token
                    token = ''
                    pass
                
            self.cadena = self.cadena[1:]
            pass
    
    def ReadFile_AUP(self):
        token = ''
        transiciones = []
        #Declaracion de Variables Nombre Etc..
        Nombre = ''
        Alfabeto = ''
        SimbolosPila = ''
        Estados = ''
        EstadoInicial = ''
        EstadosAcepta = ''
        #Declaracion de variable Transiciones
        Entrada = ''
        Destino = ''
        EstadosTrans = []
        #======================
        apertura_nombre = True
        apertura_Alfabeto = True
        apertura_SimbolosPila = True
        apertura_Estados = True
        apertura_EstadoInicial = True
        apertura_EstadoAcepta = True
        #========================
        apertura_entrada = True
        apertura_destino = False

        while len(self.cadena) > 0: 
            char = self.cadena[0]
            # Escargado de Nombre etc../
            #Estado 0
            if self.Estado == 0:
                if char == '\n':
                    if apertura_nombre:
                        Nombre = token
                        apertura_nombre = False
                        token = ''
                    elif apertura_Alfabeto:
                        Alfabeto = token
                        apertura_Alfabeto = False
                        token = ''
                    elif apertura_SimbolosPila:
                        SimbolosPila = token
                        apertura_SimbolosPila = False
                        token = ''
                    elif apertura_Estados:
                        Estados = token
                        apertura_Estados = False
                        token = ''
                    elif apertura_EstadoInicial:
                        EstadoInicial = token
                        apertura_EstadoInicial = False
                        token = ''
                    elif apertura_EstadoAcepta:
                        EstadosAcepta = token
                        apertura_EstadoAcepta = False
                        token = ''
                        self.Estado = 1
                        self.cadena = self.cadena[1:]
                        continue
                elif char == ' ':
                    self.cadena = self.cadena[1:]
                    continue
                elif char.lower() in self.Chars:
                    token += char
                elif char == ',':
                    token += char
            #Estado 1
            elif self.Estado == 1:
                if char == '\n':
                    EstadosTrans.append(token)
                   
                    trans = Transiciones(Entrada,Destino,EstadosTrans)
                    transiciones.append(trans)
                    token = ''
                    EstadosTrans = []
                    apertura_entrada = True
                    apertura_destino = False
                    pass
                elif char == ' ':
                    self.cadena = self.cadena[1:]
                    continue
                    
                elif char.lower() in self.Chars:
                    token += char
                
                elif char == '%':
                    automata = Automata(Nombre,Alfabeto,SimbolosPila,Estados,EstadoInicial,EstadosAcepta,transiciones)
                    self.data_AUP.append(automata)
                    self.cadena = self.cadena[1:]
                    self.cadena = self.cadena[1:]
                    self.Estado = 0
                    apertura_nombre = True
                    apertura_Alfabeto = True
                    apertura_SimbolosPila = True
                    apertura_Estados = True
                    apertura_EstadoInicial = True
                    apertura_EstadoAcepta = True
                    #========================
                    apertura_entrada = True
                    apertura_destino = False
                    transiciones = []
                    continue                    
                    
                elif char == ';':
                    EstadosTrans.append(token)
                    apertura_destino = True
                    token = ''
                    pass
                elif char == ',':
                    if apertura_entrada:
                        Entrada = token
                        apertura_entrada = False
                    elif apertura_destino:
                        Destino = token
                        apertura_destino = False
                    else:
                        EstadosTrans.append(token)
                    token = ''
                    pass
            self.cadena = self.cadena[1:]
            pass

        pass
    pass