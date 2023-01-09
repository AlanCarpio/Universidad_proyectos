
from tkinter.messagebox import showerror
import xml.etree.ElementTree as ET
from tkinter import filedialog
from ListasEnlazadas import ListaSimple
from tkinter.ttk import Treeview

class cargar_archivo:
    listaEmpre = ListaSimple() #-----------------------------> Lista Simple Empresas
    listaconfigInicial = ListaSimple() #-----------------------------> Lista Simple configInicial
    class empresa_configuracion:
        class listPuntos_confi:
            def __init__(self,_id,_nombre,_dirreccion,_listescritorios) -> None:
                self.__id = _id
                self.__nombre = _nombre
                self.__direccion = _dirreccion
                self.estado = False
                self.listescritorios = _listescritorios
                pass
            def imprimir_puntos(self):
                print("{} | {} | {} ".format(self.__id,self.__nombre,self.__direccion))
                self.__listescritorios.obtenerdatoEscritorio()
            def get_id(self):
                return self.__id
            def get_nombre(self):
                return self.__nombre
            def get_direc(self):
                return self.__direccion
        class listEscri_confi:
            def __init__(self,_id,_identificacion,_encargado) -> None:
                self.__id = _id
                self.identificacion = _identificacion
                self.encargado = _encargado
                self.estado = False
                pass
            def imprimir_escri(self):
                print("{} | {} | {}".format(self.__id,self.__identificacion,self.__encargado))
            def get_id(self):
                return self.__id    
        class listTracc_config:
            def __init__(self,_id,_nombre,_tiempo) -> None:
                self.id = _id
                self.__nombre = _nombre
                self.tiempo = _tiempo
                pass
            def imprimir_trac(self):
                print("{} | {} | {} ".format(self.__id,self.__nombre,self.__tiempo))
        def __init__(self,_id,_nombre,_abrebiatura,_listPuntosAtencion,_listTransaccion) -> None:
            self.__id = _id
            self.__nombre = _nombre
            self.__abrebiatura = _abrebiatura
            self.__listPuntosAtencion = _listPuntosAtencion
            self.__listTransaccion = _listTransaccion
            pass
        def imprimir(self):
            print("id: {} | nombre: {} | abrebitura: {} ".format(self.__id,self.__nombre,self.__abrebiatura))
            self.__listPuntosAtencion.obtenerdatoPunto()
            print("traccionciones")
            self.__listTransaccion.obtenerdatoTrac()
        def get_id(self):
            return self.__id
        def get_nombre(self):
            return self.__nombre
        def get_abre(self):
            return self.__abrebiatura
        def get_punto(self):
            return self.__listPuntosAtencion
        def get_trac(self):
            return self.__listTransaccion    
    class empresa_prueba:
        class listEscri():
            def __init__(self,_id) -> None:
                self.id = _id
                pass
        class listClientes():
            def __init__(self,_dpi,_trac) -> None:
                self.dpi = _dpi
                self.trac = _trac
        class listTrac():
            def __init__(self,_id,_cantidad) -> None:
                self.id = _id
                self.cantidad = _cantidad
        def __init__(self,_id,_id_empresa,_id_punto,_listEscri,_listTracc) -> None:
            self.id = _id
            self.id_empresa = _id_empresa
            self.id_punto = _id_punto
            self.listEscriActivos = _listEscri
            self.listclientes = _listTracc
            pass  
    def cargar_confi(self,ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()
        if len(root.findall("empresa")) == 0:
            er = showerror("Error","Archivo incorrecto")
            return False
        else:
            for iter_0 in root.findall("empresa"):
                id = iter_0.get("id")
                nombre = iter_0.find("nombre").text
                abrebiatura = iter_0.find("abreviatura").text
                listaPuntos = ListaSimple()#-----------------------------> Lista Simple Puntos
                for iter_1 in iter_0.iter("puntoAtencion"):
                    idLista = iter_1.get("id")
                    nombrePuntos = iter_1.find("nombre").text
                    direccion = iter_1.find("direccion").text
                    listaEscri = ListaSimple()#-----------------------------> Lista Simple Escritorios
                    for iter_2 in iter_1.iter("escritorio"):
                        idescritorio = iter_2.get("id")
                        identificacion = iter_2.find("identificacion").text
                        encargado = iter_2.find("encargado").text
                        escri = self.empresa_configuracion.listEscri_confi(idescritorio,identificacion,encargado) ## Obj Escritorio
                        listaEscri.insertar_Empresa(escri) #Agregando Escritorio a la lista Simple
                    listPuntos = self.empresa_configuracion.listPuntos_confi(idLista,nombrePuntos,direccion,listaEscri) ## Obj Puntos Atencion
                    listaPuntos.insertar_Empresa(listPuntos)
                    ##list_escri = []
                listaTrac = ListaSimple()#-----------------------------> Lista Simple Trac
                for iter_3 in iter_0.iter("transaccion"):
                    idTrac = iter_3.get("id")
                    nombreTran = iter_3.find("nombre").text
                    Tiempo = iter_3.find("tiempoAtencion").text
                    Transaccion = self.empresa_configuracion.listTracc_config(idTrac,nombreTran,Tiempo)
                    listaTrac.insertar_Empresa(Transaccion)
                ## Obj empresa
                empresa = self.empresa_configuracion(id,nombre,abrebiatura,listaPuntos,listaTrac)
                self.listaEmpre.insertar_Empresa(empresa)
            return True
            
    def cargar_prueba(self,ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()
        if len(root.findall("configInicial")) == 0:
            er = showerror("Error","Archivo incorrecto")
            return False
        else:
            for iter in root.findall("configInicial"):
                idconfig = iter.get("id")
                idEmpre = iter.get("idEmpresa")
                idPunto = iter.get("idPunto")
                listaPruebaEscritorio = ListaSimple()
                for iter_1 in iter.iter('escritorio'):
                    idEscri = iter_1.get("idEscritorio")
                    escri = self.empresa_prueba.listEscri(idEscri)
                    listaPruebaEscritorio.insertar_Empresa(escri)
                listaPruebaClientes = ListaSimple()
                for iter_2 in iter.iter('cliente'):
                    dpi = iter_2.get("dpi")
                    listaPruebaTrac = ListaSimple()
                    for iter_3 in iter_2.iter("transaccion"):
                        idTransaccion = iter_3.get("idTransaccion")
                        cantidad = iter_3.get("cantidad")
                        trac = self.empresa_prueba.listTrac(idTransaccion,cantidad)
                        listaPruebaTrac.insertar_Empresa(trac)
                    cli = self.empresa_prueba.listClientes(dpi,listaPruebaTrac)
                    listaPruebaClientes.insertar_Empresa(cli)
                confic_inicial = self.empresa_prueba(idconfig,idEmpre,idPunto,listaPruebaEscritorio,listaPruebaClientes)
                self.listaconfigInicial.insertar_Empresa(confic_inicial)
            return True
 