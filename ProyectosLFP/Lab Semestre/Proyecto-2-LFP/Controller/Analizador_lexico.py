
from Model.tokens import Tokens
from Model.html import HTML
from Model.database import data
class scanner():
    def __init__(self) -> None:
        self.letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ñ"]
        self.simbolos_comentarios = [',','#',"!","(",")",'[',']','{','}','$','%','^',]
        self.numeros = ["1","2","3","4","5","6","7","8","9","0"]
        self.tipo = ["contenedor","boton","clave","etiqueta","texto","areatexto","radioboton","check"]
        self.__data_tokens = data()
        self._data_HTML = data()
        self.__data_tokens_malos_lexicos = data()
        self.__tokens_comentarios = data()
        
    def analisis_lexico(self,cadena):
        self.__data_tokens.empty_Elements()
        self._data_HTML.empty_Elements()
        self.__data_tokens_malos_lexicos.empty_Elements()
        self.__tokens_comentarios.empty_Elements()
        #=========== Control de Etiquetas ============
        Etiqueta_1_control = False
        Etiqueta_2_propiedades = False
        Etiqueta_3_Colocacion = False
        Etiqueta_comentario = False
        Etiqueta_comentario_multilinea = False
        Etiqueta_comillas = False
        estado = 0
        char_verificacion_comentario_multi = ''
        fila = 1
        columna = 0
        token = ""
        contenedor = ""
        while len(cadena) > 0:
            char = cadena[0]
            if char == '\n':
                if token == "!--Controles" or token == "!--controles":         
                    Etiqueta_1_control = True # Etiqueta de control Apertura
                elif token == "!--Propiedades"or token == "!--propiedades":
                    Etiqueta_2_propiedades = True # Etiqueta de propiedades Apertura
                elif token == "!--Colocacion" or token == "!--colocacion":
                    Etiqueta_3_Colocacion = True # Etiqueta de  colocacion Apertura
                elif Etiqueta_comentario:
                    self.Guardar_Tokens_comentarios(token)
                    token = ""
                    Etiqueta_comentario = False
                    estado = 1
                elif Etiqueta_comentario_multilinea:
                    if char_verificacion_comentario_multi == "/*":
                        char_verificacion_comentario_multi = ""
                    self.Guardar_Tokens_comentarios(token)
                cadena = cadena[1:]
                token = ""
                fila +=1
                continue
            elif char == " ":
                columna += 1
                if token.lower() in self.tipo:
                    contenedor = token
                    token = ""
                elif Etiqueta_comillas:
                    token += char
                elif Etiqueta_comentario_multilinea:
                    token += char
                elif Etiqueta_comentario:
                    token += char
                    pass
                cadena = cadena[1:]
                continue
        #--------- Estado 0 ------------------
            if estado == 0:
                if char == "<":
                    estado = 1
                else:
                    estado = 1
                    self.Guardar_Tokens_malos(char,fila)
                    
        #--------- Estado 1 ------------------
            elif estado == 1:
                if char == ";":
                    if Etiqueta_1_control:                    # Etiqueta de control Guardar datos
                        self.Guardar_datos_HTML(contenedor,token)
                    elif Etiqueta_2_propiedades:
                        #self.Guardar_Tokens(token,fila)
                        self.Guardar_Tokens(char,fila)
                    elif Etiqueta_3_Colocacion:
                        #self.Get_data_tokens(token)
                        self.Guardar_Tokens(char,fila)
                    estado = 3
                    token = ""
                elif char.lower() in self.letras:
                    estado = 1
                    token += char
                elif char == '!':
                    estado = 2
                    token += char
                elif char == '-':
                    estado = 4
                    token += char
                elif char == '/':
                    estado = 5
                    token += char
                elif char in self.numeros:
                    token += char
                    estado = 1
                elif char == '.':
                    if Etiqueta_2_propiedades:
                        self.Guardar_Tokens(token,fila)
                        token = ""
                        pass
                    elif Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(token,fila)
                        token = ""
                    if Etiqueta_2_propiedades or Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(char,fila)
                    estado = 7
                elif char == '(':
                    if Etiqueta_2_propiedades:
                        self.Guardar_Tokens(token,fila)
                        token = ""
                        pass
                    elif Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(token,fila)
                        token = ""
                    if Etiqueta_2_propiedades or Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(char,fila)
                    estado = 8
                elif char == '"':
                    #token += char
                    estado = 11
                elif char == ")":
                    if Etiqueta_2_propiedades or Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(token,fila)
                        self.Guardar_Tokens(char,fila)
                    token = ""
                    estado = 12
                else:
                    self.Guardar_Tokens_malos(char,fila)
        #--------- Estado 2 ------------------
            elif estado == 2:
                if char == '-':
                    estado = 2
                    token += char
                elif char.lower() in self.letras:
                    token += char
                    estado = 1
                else:
                    self.Guardar_Tokens_malos(char,fila)
        #--------- Estado 3 ------------------
            elif estado == 3:
                if char.lower() in self.letras:
                    estado = 1
                    token += char
                elif char == '/':
                    token += char
                    estado = 5
                else:
                    self.Guardar_Tokens_malos(char,fila)
        #--------- Estado 4 ------------------
            elif estado == 4:
                if char == '-':
                    estado = 4
                    token += char
                elif char == '>':
                    if token == "Controles--":
                        Etiqueta_1_control = False # Etiqueta de control Cierre
                    elif token == "Propiedades--":
                        Etiqueta_2_propiedades = False # Etiqueta de propiedades Cierre
                    elif token == "Colocacion--":
                        Etiqueta_3_Colocacion = False # Etiqueta de  colocacion Cierre
                    estado = 0
                else:
                    self.Guardar_Tokens_malos(char,fila)
         #--------- Estado 5 ------------------    
            elif estado == 5:
                if char == '*':
                    token += char
                    if token == "/*":
                        self.Guardar_Tokens_comentarios(token)
                        char_verificacion_comentario_multi = token
                        token = ""
                        Etiqueta_comentario_multilinea = True #Etiqueta comentario multi linea apertura
                        estado = 6
                        cadena = cadena[1:]
                        continue
                elif char == '/':
                    token += char
                    if token == "*/":
                        self.Guardar_Tokens_comentarios(token)
                        token = ""
                        Etiqueta_comentario_multilinea = False  #Etiqueta  multi linea Cierre
                        estado = 1
                        cadena = cadena[1:]
                        continue
                    elif token == "//":
                        self.Guardar_Tokens_comentarios(token)
                        token = ""
                        Etiqueta_comentario = True #Etiqueta comentario  apertura
                        estado = 6
                        cadena = cadena[1:]
                        continue   
                else:
                    self.Guardar_Tokens_malos(char,fila)
         #--------- Estado 6 ------------------
            elif estado == 6:
                if char.lower() in self.letras:
                    token += char
                    estado = 6
                elif char in self.numeros:
                    token += char
                    estado = 6
                elif char in self.simbolos_comentarios:
                    token += char
                    estado = 6
                elif char == '*':
                    token += char
                    estado = 5
                else:
                    self.Guardar_Tokens_malos(char,fila)
        #--------- Estado 7 ------------------
            elif estado == 7:
                if char.lower() in self.letras:
                    token += char
                    estado = 1
                else:
                    self.Guardar_Tokens_malos(char,fila)
                    
        #--------- Estado 8 ------------------
            elif estado == 8:
                if char.lower() in self.letras:
                    token += char
                    estado = 1
                elif char in self.numeros:
                    token += char
                    estado = 10
                elif char == '"':
                    #token += char
                    Etiqueta_comillas = True
                    estado = 9
                else:
                    self.Guardar_Tokens_malos(char,fila)
                    
        #--------- Estado 9 ------------------
            elif estado == 9:
                if char.lower() in self.letras:
                    token += char
                    estado = 9
                elif char in self.numeros:
                    token += char
                    estado = 9
                elif char == '"':
                    #token += char
                    Etiqueta_comillas = False
                    estado = 1
                else:
                    self.Guardar_Tokens_malos(char,fila)
                    
        #--------- Estado 10 ------------------
            elif estado == 10:
                if char in self.numeros:
                    token += char
                    estado = 10
                elif char == ',':
                    if Etiqueta_2_propiedades or Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(token,fila)
                        self.Guardar_Tokens(char,fila)
                    token = ""
                    estado = 8
                elif char == ')':
                    if Etiqueta_2_propiedades or Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(token,fila)
                        self.Guardar_Tokens(char,fila)
                    token = ""
                    estado = 12
                else:
                    self.Guardar_Tokens_malos(char,fila)
                    
        #--------- Estado 11 ------------------
            elif estado == 11:
                if char == ')':
                    if Etiqueta_2_propiedades or Etiqueta_3_Colocacion:
                        self.Guardar_Tokens(token,fila)
                        self.Guardar_Tokens(char,fila)
                    token = ""
                    estado = 12
                else:
                    self.Guardar_Tokens_malos(char,fila)
        #--------- Estado 12 ------------------
            elif estado == 12:
                if char == ';':
                    if Etiqueta_2_propiedades:
                        #self.Guardar_Tokens(token,fila)
                        self.Guardar_Tokens(char,fila)
                        token = ""
                    elif Etiqueta_3_Colocacion:
                        #self.Guardar_Tokens(token,fila)
                        self.Guardar_Tokens(char,fila)
                        token = ""
                    estado = 3 
                else:
                    self.Guardar_Tokens_malos(char,fila)
            
            cadena = cadena[1:]
        
    def Guardar_datos_HTML(self,contenedor,ID):
        token = HTML(contenedor,ID)         
        self._data_HTML.insertar_dato(token)
    def Guardar_Tokens(self,dato,fila):
        token = Tokens(dato,fila)
        self.__data_tokens.insertar_dato(token)
    def Guardar_Tokens_malos(self,dato,fila):
        token = Tokens(dato,fila)
        self.__data_tokens_malos_lexicos.insertar_dato(token)
    def Guardar_Tokens_comentarios(self,dato):
        token = Tokens(dato,dato)
        self.__tokens_comentarios.insertar_dato(token)
    
    def Get_data_tokens(self):
        return self.__data_tokens
    def Get_data_tokens_comentarios(self):
        return self.__tokens_comentarios
    def Get_data_tokens_malos(self):
        resul = self.__data_tokens_malos_lexicos
        return resul
    def Get_data_HTML(self):
        return self._data_HTML

        

