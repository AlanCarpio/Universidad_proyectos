from tokenize import String
from Model.database import data
from Model.CSS import css
from Model.tokens import Tokens
class parser():
    def __init__(self) -> None:
        self.list_ID_propiedad = ["setColorLetra","setTexto","setAlineacion","setColorFondo","setMarcada","setGrupo","setAncho","setAlto","add","setPosicion"]
        self.token = ""
        self.data_css = data()
        self.data_tokens_malos = data()
        self.ID = ""
        self.propiedad = ""
        self.valor = ""
        self.RGB = {}
        self.posicion = {}
        self.asd = 0
        self.char = ""
        self.fila = 1
        pass
    def analisis_sintactico(self,_list_html,_list_tokens):
        list_html = _list_html
        cadena = _list_tokens.data
        ID_html = ["this"]
        self.data_css.empty_Elements()
        self.data_tokens_malos.empty_Elements()
        for iter in list_html.data:
            ID_html.append(iter.ID)
        estado = 'A'
        while len(cadena) > 0:
            char = cadena[0].Get_token()
            char = str(char)
            if estado == 'A':
                if char in ID_html:
                    estado = 'B'
                    self.ID = char
                else:
                    estado = 'B'
                    self.Guardar_dato_tokens_malos(char,self.fila)
                    cadena = cadena[1:]
                    self.fila += 1
                    continue
                cadena = cadena[1:]
                self.fila += 1
                continue
            elif estado == 'B':
                if char == ".":
                    estado = 'C'
                else:
                    estado = 'C'
                    #self.Guardar_dato_tokens_malos(char,self.fila)
                    cadena = cadena[1:]
                    self.fila += 1
                    continue
                cadena = cadena[1:]
                self.fila += 1
                continue
            elif estado == 'C':
                if char in self.list_ID_propiedad:
                    estado = 'D'
                    self.propiedad = char
                else:
                    estado = 'I'
                    self.Guardar_dato_tokens_malos(char,self.fila)
                    cadena = cadena[1:]
                    self.fila += 1
                    continue
                cadena = cadena[1:]
                self.fila += 1
                continue          
            elif estado == 'D':
                if char == "(":
                    estado = 'E'
                cadena = cadena[1:]
                self.fila += 1
                continue    
            elif estado == 'E':
                estado = 'F'
                if self.propiedad in ["setColorLetra","setColorFondo"]:
                    if self.asd == 0:
                        self.RGB['R'] = char
                    elif self.asd == 1:
                        self.RGB['B'] = char
                elif self.propiedad == "setPosicion":
                    self.posicion['x'] = char
                    pass
                else:
                    self.valor = char
                pass
                cadena = cadena[1:]
                self.fila += 1
                continue
            elif estado == 'F':
                if char == ",":
                    estado = 'G' 
                elif char == ")":
                    estado = 'H'
                cadena = cadena[1:]
                self.fila += 1
                continue            
            elif estado == 'G':
                estado = 'F'
                if self.asd == 1:
                    self.RGB['B'] = char
                elif self.propiedad in ["setColorLetra","setColorFondo"]:
                    self.RGB['G'] = char
                    self.asd = 1
                    
                elif self.propiedad == "setPosicion":
                    self.posicion['y'] = char
                cadena = cadena[1:]
                self.fila += 1
                continue 
            elif estado =='H':
                if char == ";":
                    estado = 'A'
                    if self.propiedad in ["setColorLetra","setColorFondo"]:
                        #print("|ID:{} |Pro:{} | Valor:{}".format(self.ID,self.propiedad,self.RGB))
                        self.Guardar_dato_css(self.ID,self.propiedad,self.RGB)                        # Guardar Dato 
                        self.ID = ""
                        self.propiedad = ""
                        self.RGB = {}
                        self.asd = 0
                    elif self.propiedad == "setPosicion":
                        #print("|ID:{} |Pro:{} | Valor:{}".format(self.ID,self.propiedad,self.posicion))
                        self.Guardar_dato_css(self.ID,self.propiedad,self.posicion)
                        self.ID = ""
                        self.propiedad = ""
                        self.posicion = {}
                    else:
                        #print("|ID:{} |Pro:{} | Valor:{}".format(self.ID,self.propiedad,self.valor))
                        self.Guardar_dato_css(self.ID,self.propiedad,self.valor)
                        self.ID = ""
                        self.propiedad = ""
                        self.valor = {}
                    cadena = cadena[1:]
                    self.fila += 1
                    continue
                pass
            elif estado == 'I':
                estado = 'I'
                self.fila += 1
                if char == ";":
                    estado = 'A'
                    self.fila += 1
                    cadena = cadena[1:]
                    continue
                cadena = cadena[1:]
                continue

            cadena = cadena[1:]
            
    def Guardar_dato_css(self,ID,propiedad,valor):
        CSs = css(ID,propiedad,valor)
        self.data_css.insertar_dato(CSs)
    def Guardar_dato_tokens_malos(self,tokens,fila):
        token = Tokens(tokens,fila)
        self.data_tokens_malos.insertar_dato(token)
    def Get_tokens_sintactico(self):
        return self.data_css
    def Get_tokens_malos_sintactico(self):
        return self.data_tokens_malos