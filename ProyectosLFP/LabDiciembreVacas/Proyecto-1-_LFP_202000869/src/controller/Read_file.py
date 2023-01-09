from src.model.AFD.AFD import AFD

from src.model.AFD.Transicion import Transicion
from src.model.GR.GR import GR
from src.model.GR.Produccion import Produccion
from tkinter import messagebox
class Read_File:
    def __init__(self,_cadena) -> None:
        self.__cadena = _cadena
        self.__letras_and_numbers = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","ñ","_","1","2","3","4","5","6","7","8","9","0",',','$']
    def scanner_AFD(self,data_AFD):
        cont_resul = 0
        cont = 0
        resul = False
        cadena = self.__cadena
        apertura_nombre = True
        apertura_Estados = True
        apertura_Alfabeto = True
        apertura_Estado_inicial = True
        apertura_Estado_aceptacion = True
        apertura_Transcision = True
        apertura_entrada = True
        apertura_estado = True
        apertura_destino = True
        list_transcision = []

        estado = 0
        token = ""
        while len(cadena) > 0:
            char = cadena[0]
            if char == '\n':
                if apertura_nombre:
                    nombre = token
                    apertura_nombre = False
                    token = ""
                elif apertura_Estados:
                    Estados = token
                    apertura_Estados = False
                    token = ""
                elif apertura_Alfabeto:
                    Alfabeto = token
                    apertura_Alfabeto = False
                    token = ""
                elif apertura_Estado_inicial:
                    resul = False
                    Estado_inicial = token
                    for iter in Estados.split(','):
                        if iter == Estado_inicial:
                            resul = True
                    if resul:
                        apertura_Estado_inicial = False
                        token = ""
                    else:
                        data_AFD.clear_list()
                        return messagebox.showerror("Error","El estado Inicial No pertenece A los Estados")
                        
                elif apertura_Estado_aceptacion:
                    cont_resul = 0
                    cont = 0
                    Estado_acep = token
                    resul_acep = Estado_acep.split(',')
                    cont_resul = len(resul_acep)
                    for iter in resul_acep:
                        for iter2 in Estados.split(","):
                            if iter == iter2:
                                cont+=1
                    if cont_resul == cont:
                        apertura_Estado_aceptacion = False
                        token = ""
                    else:
                        data_AFD.clear_list()
                        return messagebox.showerror("Error","Unos de los estados de aceptacion No pertenece A los Estados")
                elif apertura_Transcision:
                    resul_destino = False
                    for iter in Estados.split(','):
                        if iter == token:
                            resul_destino = True
                    if resul_destino:
                        pass
                    else:
                        data_AFD.clear_list()
                        return messagebox.showerror("Error","Unos de los destinos de transicion No pertenece A los Estados")
                    transicion = Transicion(entrada,estado,token)
                    list_transcision.append(transicion)
                    apertura_entrada = True
                    apertura_estado = True
                    apertura_destino = True
                    token = ''
                cadena = cadena[1:]
                continue
            elif char == " ":
                cadena = cadena[1:]
                continue 
            elif char.lower() in  self.__letras_and_numbers:
                token += char
            elif char == ';':
                if apertura_entrada:
                    apertura_entrada = False
                    entrada = token
                    resul_entrada = False
                    for iter in Estados.split(','):
                        if iter == entrada:
                            resul_entrada = True
                    if resul_entrada:
                        token = ''
                    else:
                        data_AFD.clear_list()
                        return messagebox.showerror("Error","Unas de las entradas de Transicion No pertenece A los Estados")
                elif apertura_estado:
                    apertura_estado = False
                    estado = token
                    resul_estado = False
                    for iter in Alfabeto.split(","):
                        if iter == estado:
                            resul_estado = True
                    if resul_estado:
                        token = ''
                    else:
                        data_AFD.clear_list()
                        return messagebox.showerror("Error","Unas de los estados de Transicion No pertenece Al Alfabeto")
            elif char == '%':
                dat_afd = AFD(nombre,Estados,Alfabeto,Estado_inicial,Estado_acep,list_transcision)
                data_AFD.insert_element(dat_afd)
                list_transcision = []
                apertura_nombre = True
                apertura_Estados = True
                apertura_Alfabeto = True
                apertura_Estado_inicial = True
                apertura_Estado_aceptacion = True
                apertura_Transcision = True
                cadena = cadena[1:]
            cadena = cadena[1:]
        pass
    def scanner_GR(self,data_gr):
        Alfabeto = ''
        cont_resul = 0
        cont = 0
        resul = False
        Estado_acep = ''
        cadena = self.__cadena
        apertura_nombre = True
        apertura_Estados = True
        apertura_Alfabeto = True
        apertura_Estado_inicial = True
        apertura_Estado_aceptacion = True
        apertura_Transcision = True
        apertura_entrada = True
        apertura_estado = False
        apertura_destino = True
        list_transcision = []

        estado = 0
        token = ""
        while len(cadena) > 0:
            char = cadena[0]
            if char == '\n':
                if apertura_nombre:
                    nombre = token
                    apertura_nombre = False
                    token = ""
                elif apertura_Estados:
                    Estados = token
                    apertura_Estados = False
                    token = ""
                elif apertura_Alfabeto:
                    Alfabeto = token
                    apertura_Alfabeto = False
                    token = ""
                elif apertura_Estado_inicial:
                    resul = False
                    Estado_inicial = token
                    for iter in Estados.split(','):
                        if iter == Estado_inicial:
                            resul = True
                    if resul:
                        apertura_Estado_inicial = False
                        token = ""
                    else:
                        data_gr.clear_list()
                        return messagebox.showerror("Error","El No Terminal Inicial No pertenece A los No Terminales")
                elif token == '$':
                        transicion = Produccion(entrada,token,' ')
                        list_transcision.append(transicion)
                        apertura_entrada = True
                        apertura_estado = True
                        apertura_destino = True
                        entrada += ','
                        Estado_acep += entrada
                        token = ''
                elif apertura_Transcision:
                    resul_destino = False
                    for iter in Estados.split(','):
                        if iter == token:
                            resul_destino = True
                    if resul_destino:
                        
                        pass
                    else:
                        data_gr.clear_list()
                        return messagebox.showerror("Error","Unos de los destinos de transicion No pertenece A los Estados")
                    transicion = Produccion(entrada,estado,token)
                    list_transcision.append(transicion)
                    apertura_entrada = True
                    apertura_estado = True
                    apertura_destino = True
                    token = ''
                cadena = cadena[1:]
                continue
            elif char == " ":
                if apertura_estado: 
                    apertura_estado = False
                    estado = token
                    resul_estado = False
                    for iter in Alfabeto.split(","):
                        if iter == estado:
                            resul_estado = True
                    if resul_estado:
                        token = ''
                        apertura_estado = False
                    else:
                        data_gr.clear_list()
                        return messagebox.showerror("Error","Unas de los estados de Produccion No pertenece A los Terminales")   
                cadena = cadena[1:]
                continue
            elif char.lower() in  self.__letras_and_numbers:
                token += char
            elif char == '>':
                if apertura_entrada:
                    apertura_entrada = False
                    entrada = token
                    resul_entrada = False
                    for iter in Estados.split(','):
                        if iter == entrada:
                            resul_entrada = True
                    if resul_entrada:
                        token = ''
                        apertura_estado = True
                    else:
                        data_gr.clear_list()
                        return messagebox.showerror("Error","Unas de las entradas de Produccion No pertenece A los No terminales")
            elif char == '%':
                
                dat_gr = GR(nombre,Estados,Alfabeto,Estado_inicial,Estado_acep,list_transcision)
                data_gr.insert_element(dat_gr)
                list_transcision = []
                apertura_nombre = True
                apertura_Estados = True
                apertura_Alfabeto = True
                apertura_Estado_inicial = True
                apertura_Estado_aceptacion = True
                apertura_Transcision = True
                cadena = cadena[1:]
            cadena = cadena[1:]
        pass