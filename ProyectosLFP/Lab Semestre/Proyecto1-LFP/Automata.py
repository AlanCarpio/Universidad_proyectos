import re
from math import*

class automota:
    class operaciones():
        def __init__(self,_tipo,_datos) -> None:
            self.tipo = _tipo
            self.datos = _datos
        def imprimir2(self):
            print(self.tipo)
            print(self.datos)
        def operar(self):
            if len(self.tipo)>=2:
                if len(self.datos)>= len(self.tipo):
                    self.operaciones_var()
                else:
                    if self.tipo[0].lower() == "multiplicacion":
                        self.datos.insert(0,1)
                    else: 
                        self.datos.insert(0,0)
                    self.operaciones_var()
            else:
                self.operaciones_one()
        def operaciones_var(self):
            listaaux = []
            while len(self.tipo)>1:
                dato1 = self.tipo.pop(-1)
                dato2 = self.datos.pop(-1)
                lista = self.operaciones_aux(dato1,dato2)
                listaaux.append(lista[1])
            if len(self.datos)>=2:
                cont = len(self.datos)-1
                while len(self.datos)>0:
                    dato3 = self.datos.pop(-1)
                    listaaux.insert(0,dato3)
                    cont -= 1
            else:
                dato3 = self.datos.pop(-1)
                listaaux.append(dato3)
            lista = self.operaciones_aux(self.tipo[0],listaaux)
            self.tipo = "Operacion Compleja "
            self.datos = lista[1]
        def operaciones_one(self):
            suma = 0
            for iter in self.tipo:
                if iter.lower() == "suma":
                    one_val = float(self.datos[0])
                    self.datos = self.datos[1:]
                    resul = "{}+".format(one_val)
                    while len(self.datos)>0:
                        one_val += float(self.datos[0])
                        resul += "{}+".format(self.datos[0])
                        self.datos = self.datos[1:]
                    resul = list(resul)
                    resul.pop()
                    resul = "".join(resul)
                    resul += "={}".format(one_val)
                    self.datos = resul 
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "multiplicacion":
                    one_val = float(self.datos[0])
                    self.datos = self.datos[1:]
                    resul = "{}*".format(one_val)
                    while len(self.datos)>0:
                        one_val *= float(self.datos[0])
                        resul += "{}*".format(self.datos[0])
                        self.datos = self.datos[1:]
                    resul = list(resul)
                    resul.pop()
                    resul = "".join(resul)
                    resul += "={}".format(one_val)
                    self.datos = resul
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "resta":
                    one_val = float(self.datos[0])
                    self.datos = self.datos[1:]
                    resul = "{}-".format(one_val)
                    while len(self.datos)>0:
                        one_val -= float(self.datos[0])
                        resul += "{}-".format(self.datos[0])
                        self.datos = self.datos[1:]
                    resul = list(resul)
                    resul.pop()
                    resul = "".join(resul)
                    resul += "={}".format(one_val)
                    self.datos = resul
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "division":
                    one_val = float(self.datos[0])
                    self.datos = self.datos[1:]
                    resul = "{}/".format(one_val)
                    while len(self.datos)>0:
                        one_val /= float(self.datos[0])
                        resul += "{}/".format(self.datos[0])
                        self.datos = self.datos[1:]
                    resul = list(resul)
                    resul.pop()
                    resul = "".join(resul)
                    resul += "={}".format(one_val)
                    self.datos = resul
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "potencia":
                    one_val = self.datos[0]
                    seg_val = self.datos[1]
                    numbers1 = float(one_val)
                    numbers2 = float(seg_val)
                    one_val = pow(numbers2,numbers1)
                    self.datos = one_val
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "raiz":
                    one_val = self.datos[0]
                    seg_val = self.datos[1]
                    numbers1 = float(one_val)
                    numbers2 = float(seg_val)
                    one_val = pow(numbers2,1/numbers1)
                    self.datos = one_val
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "inverso":
                    one_val = float(self.datos[0])
                    one_val = 1/one_val
                    self.datos = one_val
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "seno":
                    one_val = float(self.datos[0])
                    one_val = sin(one_val)
                    self.datos = one_val
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "coseno":
                    one_val = float(self.datos[0])
                    one_val = cos(one_val)
                    self.datos = one_val
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "tangente":
                    one_val = float(self.datos[0])
                    one_val = tan(one_val)
                    self.datos = one_val
                    self.tipo = "Operacion: "+ iter
                if iter.lower() == "mod":
                    one_val = float(self.datos[0])
                    dato2 = float(self.datos[1])
                    one_val = fmod(one_val,dato2)
                    self.datos = one_val    
                    self.tipo = "Operacion: "+ iter                
        def operaciones_aux(self,tipo,dato):
            if tipo.lower() == "suma":
                one_val = float(dato[0])
                dato = dato[1:]
                resul = "{}+".format(one_val)
                while len(dato)>0:
                    one_val += float(dato[0])
                    resul += "{}+".format(dato[0])
                    dato = dato[1:]
                resul = list(resul)
                resul.pop()
                resul = "".join(resul)
                resul += "={}".format(one_val)
                return [tipo,one_val]
            if tipo.lower() == "multiplicacion":
                one_val = float(dato[0])
                dato = dato[1:]
                resul = "{}*".format(one_val)
                while len(dato)>0:
                    one_val *= float(dato[0])
                    resul += "{}*".format(dato[0])
                    dato = dato[1:]
                resul = list(resul)
                resul.pop()
                resul = "".join(resul)
                resul += "={}".format(one_val)
                return [tipo,one_val]
            if tipo.lower() == "resta":
                one_val = float(dato[0])
                dato = dato[1:]
                resul = "{}-".format(one_val)
                while len(dato)>0:
                    one_val -= float(dato[0])
                    resul += "{}-".format(dato[0])
                    dato = dato[1:]
                one_val *= -1
                resul = list(resul)
                resul.pop()
                resul = "".join(resul)
                resul += "={}".format(one_val)
                return [tipo,one_val]
            if tipo.lower() == "division":
                one_val = float(dato[0])
                dato = dato[1:]
                resul = "{}/".format(one_val)
                while len(dato)>0:
                    one_val /= float(dato[0])
                    resul += "{}/".format(dato[0])
                    dato = dato[1:]
                resul = list(resul)
                resul.pop()
                resul = "".join(resul)
                resul += "={}".format(one_val)
                return [tipo,one_val]
            if tipo.lower() == "potencia":
                one_val = dato[0]
                seg_val = dato[1]
                numbers1 = float(one_val)
                numbers2 = float(seg_val)
                one_val = pow(numbers2,numbers1)
                dato = one_val
                return [tipo,dato] 
            if tipo.lower() == "raiz":
                one_val = dato[0]
                seg_val = dato[1]
                numbers1 = float(one_val)
                numbers2 = float(seg_val)
                one_val = pow(numbers2,1/numbers1)
                dato = one_val
                return [tipo,dato] 
            if tipo.lower() == "inverso":
                one_val = float(dato[0])
                if one_val > 0:
                    one_val *= -1
                    dato = one_val
                    return [tipo,dato] 
                else:
                    one_val *= -1
                    dato = one_val
                    return [tipo,dato] 
            if tipo.lower() == "seno":
                one_val = float(dato[0])
                one_val = sin(one_val)
                dato = one_val
                return [tipo,dato] 
            if tipo.lower() == "coseno":
                one_val = float(dato[0])
                one_val = cos(one_val)
                dato = one_val
                return [tipo,dato] 
            if tipo.lower() == "tangente":
                one_val = float(dato[0])
                one_val = tan(one_val)
                dato = one_val
                return [tipo,dato] 
            if tipo.lower() == "mod":
                one_val = float(dato[0])
                dato2 = float(dato[1])
                one_val = fmod(one_val,dato2)
                dato = one_val    
                return [tipo,dato]                    
    class HTML():
        def __init__(self,_etiqueta,_tipo,_dato) -> None:
            self.etiqueta = _etiqueta
            self.tipo = _tipo
            self.datos = _dato
        def imprimir(self):
            print(self.etiqueta,end=" ")
            print(self.tipo,end=" ")
            print(self.datos)
    class tokens:
        def __init__(self,columna,fila,token) -> None:
            self.fila = fila
            self.columna = columna
            self.token = token
            pass
        def imprimir(self):
            print("F{}|C{}| {}".format(self.fila,self.columna,self.token))
    def __init__(self) -> None:
        self.letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",",",".","/"]
        self.numeros = ["1","2","3","4","5","6","7","8","9","0",".","*","-","(",")",":","+","^","[","]"]
        self.operadores = ["suma","resta","multiplicacion","division","potencia","raiz","inverso","seno","coseno","tangente","mod"]
        self.estado_actual = 0
        self.estado_anterior = 0
        self.fila = 1
        self.columna = 0
        self.cadena = ""
        self.token = ''
        self.tabla_tokens = []
        self.tabla_tokensMalos = []
        self.tabla_operaciones = []
        self.tabla_HTML = []
        self.HTML_dic = {}
        self.HTML_etiqueta = ""
        self.HTML_tipo = ""
        #---------------------------
        self.operador = []
        self.operador_cont = 0
        self.operador_guardar = ''
        self.cierre_opera = False
        self.cierre_T = False
        self.cierre = False
        self.numeros_eti = []
        self.numeros_eti_aux = []
        self.texto = ""
        pass
    def analizar(self,cadena):
        while len(cadena) > 0:
            char = cadena[0]
            if char == '\n':
                if self.estado_actual == 1 or self.estado_actual == 3 or self.estado_actual == 4:
                    self.token += "<br>"
                    self.estado_actual = 1
                self.fila +=1
                self.columna = 0
                cadena = cadena[1:]
                continue
            elif char == " ":
                if self.estado_actual == 1 or self.estado_actual == 3 or self.estado_actual == 4:
                    if self.token.lower() == "titulo" or self.token.lower() =="descripcion" or self.token.lower() =="contenido":
                        self.HTML_tipo = self.token
                    if self.cierre:
                        for iter in self.HTML_dic.keys():
                            if iter.lower() == "color":
                                self.HTML_dic[iter] = self.token
                        self.cierre = False              
                    self.token += char
                    
                self.columna += 1
                cadena = cadena[1:]
                continue
            if self.estado_actual == 0:
                if char == "<":
                    self.estado_actual = 1
                    self.estado_anterior = 0
                    self.Guardar_token(self.columna,self.fila,char)
                else:
                    self.Guardar_tokenError(self.columna,self.fila,char)
            #-------------------- ESTADO 1-------------------
            elif self.estado_actual == 1:
                if char == ">":
                    self.estado_actual = 2
                    self.estado_anterior = 1
                    if self.cierre_opera:    
                        if self.token.lower() == "/operacion":
                            self.operador_cont -= 1
                            if self.operador_cont == 1:
                                self.numeros_eti.append(self.numeros_eti_aux)
                                self.numeros_eti_aux = []
                            if self.operador_cont == 0:
                                self.Guardar_operacion(self.operador,self.numeros_eti)
                                self.numeros_eti = []
                                self.operador = []
                                self.cierre_opera = False
                            
                    if self.cierre_opera:
                        if self.token.lower() in self.operadores:
                            self.operador.append(self.token)
                            
                        
                    if self.cierre_T:   
                        if self.token.lower() == "/texto":
                            self.Guardar_HTML("Texto","",self.texto)
                            self.texto = ""
                            self.cierre = False
                        pass
                    if self.token.lower() == "/estilo":
                        self.HTML_etiqueta = ""
                    if self.token.lower() == "texto":
                        self.cierre_T = True
                    if self.token.lower() == "titulo":
                        self.cierre = True 
                    if self.token.lower() == "/titulo":
                        self.Guardar_HTML("Titulo","",self.texto)
                        self.cierre = True    
                    if self.token.lower() == "estilo":
                        self.HTML_etiqueta = self.token
                        self.cierre = True
                    self.estado_actual = 2
                    self.estado_anterior = 1
                    self.Guardar_token(self.columna,self.fila,self.token)
                    self.Guardar_token(self.columna,self.fila,char)
                    self.token = ""
                elif char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 1
                    self.token += char
                elif char == "=":
                    if self.token == "Descripcion Color" or self.token == "Titulo Color" or self.token == "Contenido Color" :
                        x = re.findall("Descripcion|Color|Titulo|Contenido",self.token)
                        self.Guardar_token(self.columna,self.fila,x[0])
                        self.token = x[1]
                        
                    x = re.search("Tamanio",self.token)
                    if x:
                        y = x.string
                        w = y.split()
                        self.Guardar_token(self.columna,self.fila,w[0])
                        self.token = w[1]
                        
                    if self.token.lower() == "color" or self.token.lower() == "tamanio":
                        self.HTML_dic[self.token] = ""
                        self.cierre = True
                        
                    if self.token.lower() == "operacion":
                        self.operador_cont += 1
                        self.cierre_opera = True  
                    self.estado_actual = 3
                    self.estado_anterior = 1
                    self.Guardar_token(self.columna,self.fila,self.token)
                    self.Guardar_token(self.columna,self.fila,char)
                    self.token = ""
                elif char == "/":
                    self.estado_actual = 5
                    self.estado_anterior = 1
                    self.token += char
                elif char == "<":
                    self.estado_actual = 6
                    self.estado_anterior = 1
                    self.texto = self.token
                    self.Guardar_token(self.columna,self.fila,self.token)
                    self.Guardar_token(self.columna,self.fila,char)
                    self.token = ""
                elif char in self.numeros:
                    self.estado_actual = 4
                    self.estado_anterior = 1
                    self.token += char
                else:
                    self.Guardar_tokenError(self.columna,self.fila,char)
                    self.token += char
            #-------------------- ESTADO 2-------------------
            elif self.estado_actual == 2:
                if char == "<":
                    self.estado_actual = 1
                    self.estado_anterior = 2
                    self.Guardar_token(self.columna,self.fila,char)
                elif char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 2
                    self.token += char
                elif char in self.numeros:
                    self.estado_actual = 4
                    self.estado_anterior = 2
                    self.token += char
                else:
                    self.Guardar_tokenError(self.columna,self.fila,char)
                    self.token += char
            #-------------------- ESTADO 3-------------------
            elif self.estado_actual == 3:
                if char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 3
                    self.token += char
                elif char in self.numeros:
                    self.estado_actual = 4
                    self.estado_anterior = 3
                    self.token += char
                else:
                    self.Guardar_tokenError(self.columna,self.fila,char)
                    self.token += char
            #-------------------- ESTADO 4-------------------
            elif self.estado_actual == 4:
                if char in self.numeros:
                    self.estado_actual = 4
                    self.estado_anterior = 4
                    self.token += char
                    
                elif char == "/":
                    self.estado_actual = 1
                    self.estado_anterior = 4
                    if self.cierre:
                        for iter in self.HTML_dic.keys():
                            if iter.lower() == "tamanio":
                                self.HTML_dic[iter] = self.token
                        self.cierre = False              
                        self.Guardar_HTML(self.HTML_etiqueta,self.HTML_tipo,self.HTML_dic)
                        self.HTML_tipo = ""
                        self.HTML_dic = {}
                        self.token = ""
                    self.Guardar_token(self.columna,self.fila,self.token)
                    self.token += char
                elif char == "<":
                    self.estado_actual = 1
                    self.estado_anterior = 4
                    if self.operador_cont == 1:
                        self.numeros_eti.append(self.token)
                    if self.operador_cont >= 2:
                        self.numeros_eti_aux.append(self.token)                                        ## Se Guardan los numeros de operadores
                    self.Guardar_token(self.columna,self.fila,self.token)
                    self.Guardar_token(self.columna,self.fila,char)
                    self.token = ""
                elif char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 4
                    self.token += char
                else:
                    self.Guardar_tokenError(self.columna,self.fila,char)
                    self.token += char

            #-------------------- ESTADO 5-------------------
            elif self.estado_actual == 5:
                if char.lower() in self.letras:
                    self.estado_actual = 1
                    self.estado_anterior = 5
                    self.token += char
                else:
                    self.Guardar_tokenError(self.columna,self.fila,char)
                    self.token += char
            #-------------------- ESTADO 6-------------------
            elif self.estado_actual == 6:
                if char == "/":
                    self.estado_actual = 1
                    self.estado_anterior = 6
                    self.token += char
                else:
                    self.Guardar_tokenError(self.columna,self.fila,char)
                    self.token += char
            self.columna+= 1
            cadena = cadena[1:]    
    def Guardar_token(self,columna,fila,token):
        guardar = self.tokens(columna,fila,token)
        self.tabla_tokens.append(guardar)
    def Guardar_tokenError(self,columna,fila,token):
        guardar = self.tokens(columna,fila,token)
        self.tabla_tokensMalos.append(guardar)
    def Guardar_operacion(self,tipo,dato):
        operador1 = self.operaciones(tipo,dato)
        self.tabla_operaciones.append(operador1)
    def Guardar_HTML(self,etiqueta,tipo,dato):
        html1 = self.HTML(etiqueta,tipo,dato)
        self.tabla_HTML.append(html1)    
    