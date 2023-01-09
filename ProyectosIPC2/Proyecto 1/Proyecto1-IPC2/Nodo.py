from Paciente import paciente as p
class Nodo(object):
    def __init__(self,_dato) -> None:
        self.dato = _dato
        self.siguiente = None
        self.anterior = None
        self.superior = None
        self.inferior = None
        pass
class ListaEnlazada:
    
    def __init__(self,_sizeMatriz) -> None:
        self.primero = None
        self.final = None
        self.temp = None
        self.size = 0
        self.size2 = 0
        self.size3 = 0
        self.sizeMatriz = int(_sizeMatriz)
    def insertar(self,dato):
        nodo = Nodo(dato)
        self.size += 1
        self.size2 += 1 
        # Primera Fila
        if self.primero == None:
            self.primero = nodo #primer nodo de la primera fila
            self.final = nodo
        elif self.size < self.sizeMatriz+1:
            self.final.siguiente = nodo #siguientes Nodos de la primera fila
            nodo.anterior = self.final
            self.final = nodo
            self.temp = self.primero.siguiente
        ########################################
        elif self.size2 == self.sizeMatriz+1:
            self.primero.inferior = nodo
            nodo.superior = self.primero # primer nodo de la segunda fila
            self.final = nodo
            self.size3 = 1
        elif self.size3 == self.sizeMatriz:
            self.temp.inferior = nodo
            nodo.superior = self.temp #primer nodo de las siguientes filas
            self.final = nodo
            self.size3 = 1
            self.temp = self.temp.siguiente
        elif self.size3 < self.sizeMatriz: ##siguientes nodos de las siguientes filas
            self.size3 += 1
            self.final.siguiente = nodo
            self.temp.inferior = nodo
            nodo.anterior = self.final
            nodo.superior = self.temp
            self.final = nodo
            if self.size3 < self.sizeMatriz:
                self.temp = self.temp.siguiente
            if self.size3 == self.sizeMatriz:
                for i in range(1,self.size3):
                    self.temp =  self.temp.anterior
                self.temp = self.temp.inferior
    def sumador(self,com):
        contador = 0
        if com!= None:
            if com.dato == 1:
                contador+=1
                return contador
            else:
                return 0
        else:
            return 0
    def comprabaciones_superiores(self,com):
        contador = 0
        com2 = com.superior
        if com2 != None:
            contador += self.sumador(com2)
            com = com2.siguiente
            contador += self.sumador(com)
            com = com2.anterior
            contador += self.sumador(com)
            return int(contador)
        else:
            return 0 
    def comprabaciones_inferiores(self,com):
        contador = 0
        com2 = com.inferior
        if com2 != None:
            contador += self.sumador(com2)
            com = com2.siguiente
            contador += self.sumador(com)
            com = com2.anterior
            contador += self.sumador(com)
            return int(contador)
        else:  
            return 0 
    def comprobacion_siguiente(self,com):
        contador = 0
        com2 = com.siguiente
        if com2 != None:
            contador += self.sumador(com2)
            return contador
        else:
            return 0
    def comprobacion_anterior(self,com):
        contador = 0
        com2 = com.anterior
        if com2!= None:
            contador += self.sumador(com2)
            return contador
        elif com2 == None:
            return 0        
    def comprobacion(self,m,lol):
        contadoraux = 0
        contadoraux2 = 0
        listacontador = 0
        com = self.primero
        lista2 = []
        lista2.append([])
        while com!=None:
           contador = 0
           contador += self.comprabaciones_superiores(com)
           contador += self.comprabaciones_inferiores(com)
           contador += self.comprobacion_siguiente(com)
           contador += self.comprobacion_anterior(com)
           if com.dato == 1:
                if contador == 2 or contador == 3:
                    aux = 1
                else: 
                    aux = 0
                lista2[listacontador].append(aux)
           else:
                if contador == 3:
                    aux = 1
                else: 
                    aux = 0
                lista2[listacontador].append(aux)
           contadoraux += 1
           contadoraux2 += 1
           if contadoraux == m:
                for i in range(1,m):
                   com = com.anterior
                com = com.inferior
                lista2.append([])
                listacontador+=1
                contadoraux = 0
           else:
                com = com.siguiente         
           if contadoraux2 == (m * m):
                lista2.pop()
                lol.insertar_lista(lista2)
                break
    def imprimir(self):
        num = self.primero
        num = num.siguiente
        num = num.siguiente
        num = num.anterior
        print(num.dato)

