import random
import re
import os
import xml.etree.ElementTree as ET

from database.Configuracion import configuracion
#Recurso
from database.Recursos.Recurso import recurso
#Consumos
from database.Consumos.Consumo import consumo
#Cliente
from database.Clientes.Clientes import clientes
from database.Clientes.Instancias import instancias
#Categoria
from database.Categorias.Categoria import categoria
from database.Categorias.ListaConfiguraciones import list_configuracion
from database.Categorias.RecursosConfiguracion import recursos_configuracion

#Class
class config_controller():
    
    def __init__(self) -> None:
        self.list_configuracion = configuracion()
        pass
     #==== funciones y Objet Recursos 
    
    def create_recurso(self,_ID,_nombre,_abreviatura,_metrica,_tipo,_valorxhora):
        Recurso = recurso(_ID,_nombre,_abreviatura,_metrica,_tipo,_valorxhora)
        self.list_configuracion.insert_recursos(Recurso)
        return [{"MSG":"Recurso Creado Exitosamente"},200]
    #==== funciones y Objet Clientes
    
    def create_cliente(self,_NIT,_Nombre,_Usuario,_Password,_Direccion,_Email):
        Cliente = clientes(_NIT,_Nombre,_Usuario,_Password,_Direccion,_Email)
        self.list_configuracion.insert_clientes(Cliente)
        return [{"MSG":"Cliente Creado correctamente"},200]
    
    def create_instacia(self,NIT_cliente,_ID,_ID_configuracion,_nombre,_fecha_inicial,_estado,_fecha_final):
        Reg_ex_fecha = "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
        resul_fecha= re.findall(Reg_ex_fecha, _fecha_inicial)
        if resul_fecha == []:
            return [{"MSG":"Ingrese un formato de fecha valido dd/mm/aaaa"},400]
        for iter in self.list_configuracion.Get_list_clientes().Get_database(): 
            if iter.Get_NIT() == NIT_cliente:
                if _estado == "Vigente" or _estado == "vigente":
                    _fecha_final = ""
                elif _estado == "Cancelado" or _estado == "cancelado":
                    pass
                else:
                    return [{"MSG":"Ingrese un estado de tipo Vigente o Cancelado"},400]
                instancia = instancias(_ID,_ID_configuracion,_nombre,resul_fecha[0],_estado,_fecha_final)
                iter.insert_instancia(instancia)
                return [{"MSG":"Instancia Creada correctamente"},200]
        return [{"MSG":"No existe este cliente en nuestra base de datos"},404]
    
    #===== Funciones y Objet Categorias
    def create_categoria(self,_ID,_nombre,_abreviatura,_cargaTrabajo):
        Categoria = categoria(_ID,_nombre,_abreviatura,_cargaTrabajo)
        self.list_configuracion.insert_categorias(Categoria)
        return [{"MSG":"Categoria Creada correctamente"},200]
    
    def create_ListaConfiguraciones(self,_ID_categoria,_ID,_nombre,_descripcion):
        for iter in self.list_configuracion.Get_list_categorias().Get_database(): 
            if iter.Get_ID() == _ID_categoria:
                List_configuracion = list_configuracion(_ID,_nombre,_descripcion)
                iter.insert_configuracion(List_configuracion)
                return [{"MSG":"Config Creada correctamente"},200]
        return [{"MSG":"No existe esta categoria en nuestra base de datos"},404]

    def create_RecursosConfiguracion(self,ID_categoria,ID_List_configuracion,_ID,_cantidad_recurso):
        for iter in self.list_configuracion.Get_list_categorias().Get_database(): 
            if iter.Get_ID() == ID_categoria:
                for iter2 in iter.Get_list_configuracion().Get_database():
                    if iter2.Get_ID() == ID_List_configuracion:
                        Recursos_configuracion = recursos_configuracion(_ID,_cantidad_recurso)
                        iter2.insert_recursos_configuracion(Recursos_configuracion)
                        return [{"MSG":"Config recurso Creada correctamente"},200]
                return [{"MSG":"No existe esta List de configuracion en categoria en nuestra base de datos"},404]
        return [{"MSG":"No existe esta categoria en nuestra base de datos"},404]
    #==== Base de datos XML ==============================
    
    def read_xml(self,ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()        
        for raiz2 in root.findall("listaRecursos"):
            for raiz in raiz2.iter("recurso"):
                id = raiz.get("id")
                nombre = raiz.find("nombre").text
                abreviatura = raiz.find("abreviatura").text
                metrica = raiz.find("metrica").text
                tipo = raiz.find("tipo").text
                valorXhora = raiz.find("valorXhora").text
                Recurso = recurso(id,nombre,abreviatura,metrica,tipo,valorXhora)
                self.list_configuracion.insert_recursos(Recurso)
                pass
        #==========================
        for raiz in root.findall("listaCategorias"):
            for raiz2 in raiz.iter("categoria"):
                id =  raiz2.get("id")
                nombre = raiz2.find("nombre").text
                descripcion = raiz2.find("descripcion").text
                cargaTrabajo = raiz2.find("cargaTrabajo").text
                Categoria = categoria(id,nombre,descripcion,cargaTrabajo)
                for raiz3 in raiz2.findall("listaConfiguraciones"):
                    for raiz4 in raiz3.iter("configuracion"):
                        id =  raiz4.get("id")
                        nombre = raiz4.find("nombre").text
                        descripcion = raiz4.find("descripcion").text
                        List_configuracion = list_configuracion(id,nombre,descripcion)
                        for raiz5 in raiz4.findall("recursosConfiguracion"):
                            for raiz6 in raiz5.iter("recurso"):
                                id = raiz6.get("id")
                                cantidadRecurso = raiz6.text
                                Recursos_configuracion = recursos_configuracion(id,cantidadRecurso)
                                List_configuracion.insert_recursos_configuracion(Recursos_configuracion)
                        Categoria.insert_configuracion(List_configuracion)
                    self.list_configuracion.insert_categorias(Categoria)    
        #===========================
        for raiz in root.findall("listaClientes"):
            for raiz2 in raiz.iter("cliente"):
                nit =  raiz2.get("nit")
                nombre = raiz2.find("nombre").text
                usuario = raiz2.find("usuario").text
                clave = raiz2.find("clave").text
                direccion = raiz2.find("direccion").text
                correoElectronico = raiz2.find("correoElectronico").text
                Cliente = clientes(nit,nombre,usuario,clave,direccion,correoElectronico)
                for raiz3 in raiz2.findall("listaInstancias"):
                    for raiz4 in raiz3.iter("instancia"):
                        id =  raiz4.get("id")
                        idConfiguracion = raiz4.find("idConfiguracion").text
                        nombre = raiz4.find("nombre").text
                        fechaInicio = raiz4.find("fechaInicio").text
                        Reg_ex_fecha = "[0-9]{1,4}\\-[0-9]{1,2}\\-[0-9]{1,4}"
                        fechaHora1= re.findall(Reg_ex_fecha, fechaInicio)
                        if fechaHora1 == []:
                            Reg_ex_fecha = "[0-9]{1,4}\\/[0-9]{1,2}\\/[0-9]{1,4}"
                            fechaHora1= re.findall(Reg_ex_fecha, fechaInicio)
                        estado = raiz4.find("estado").text
                        fechaFinal = raiz4.find("fechaFinal").text
                        print(type(fechaFinal))
                        if fechaFinal == None:
                            fechaHora2 = ["",""]
                            fechaHora2[0] = fechaFinal
                        else:
                            Reg_ex_fecha = "[0-9]{1,4}\\-[0-9]{1,2}\\-[0-9]{1,4}"
                            fechaHora2= re.findall(Reg_ex_fecha, fechaFinal)
                            if fechaHora2 == []:
                                Reg_ex_fecha = "[0-9]{1,4}\\/[0-9]{1,2}\\/[0-9]{1,4}"
                                fechaHora2= re.findall(Reg_ex_fecha, fechaFinal)
                        instancia = instancias(id,idConfiguracion,nombre,fechaHora1[0],estado,fechaHora2[0])                        
                        Cliente.insert_instancia(instancia)
                self.list_configuracion.insert_clientes(Cliente)
    def read_xml_consumo(self,ruta):
        tree = ET.parse(ruta)
        root = tree.getroot()
        #for raiz2 in root.findall("listadoConsumos"):
        for raiz in root.iter("consumo"):
            nit_cliente = raiz.get("nitCliente")
            ID_instancia = raiz.get("idInstancia")
            tiempo = raiz.find("tiempo").text
            fechaHora = raiz.find("fechaHora").text
            Reg_ex_fecha = "[0-9]{1,4}\\-[0-9]{1,2}\\-[0-9]{1,4}"
            fechaHora1= re.findall(Reg_ex_fecha, fechaHora)
            if fechaHora1 == []:
                Reg_ex_fecha = "[0-9]{1,4}\\/[0-9]{1,2}\\/[0-9]{1,4}"
                fechaHora1= re.findall(Reg_ex_fecha, fechaHora)
            Consumo = consumo(nit_cliente,ID_instancia,tiempo,fechaHora1[0])
            self.list_configuracion.insert_consumo(Consumo)
            pass
    def conprobacion_xml_config(self):
        if os.path.exists("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_Config_temporal.xml"):
            self.read_xml("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_Config_temporal.xml")
            os.remove("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_Config_temporal.xml")
        else:
            pass
    def conprobacion_xml_consumo(self):
        if os.path.exists("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_consumo_temporal.xml"):
            self.read_xml_consumo("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_consumo_temporal.xml")
            os.remove("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_consumo_temporal.xml")
        else:
            pass
    def Create_Database_XML(self):
        root = ET.Element("archivoConfiguraciones")
        #============= lista Recursos
        listaRecursos = ET.SubElement(root,"listaRecursos")
        for iter_recursos in self.list_configuracion.Get_list_recursos().Get_database():
            pass
        pass
    #======== Funciones Obtener datos etc.. ================
    def Get_list_Clientes_and_Instancias(self):
        resul = []
        for iter in self.list_configuracion.Get_list_clientes().Get_database(): 
           dic_clientes = iter.Getting_all_the_data_JSON()
           resul_instacias = []
           for iter2 in iter.Get_List_instancias():
                resul_instacias.append(iter2.Getting_all_the_data_JSON()) 
           dic_clientes.update({"Instacias":resul_instacias})
           resul.append(dic_clientes)
        return {"Consulta_Clientes":resul}
    
    def Get_list_Categorias(self):
        resul = []
        for iter in self.list_configuracion.Get_list_categorias().Get_database(): 
           dic_categoria = iter.Getting_all_the_data_JSON()
           resul_list_configuraciones = []
           for iter2 in iter.Get_list_configuracion().Get_database():
                dic_list_configuracion = iter2.Getting_all_the_data_JSON() 
                resul_list_recursos_configuracion = []
                print(iter2.Get_list_recursos_configuracion())
                for iter3 in iter2.Get_list_recursos_configuracion().Get_database():
                    resul_list_recursos_configuracion.append(iter3.Getting_all_the_data_JSON()) 
                dic_list_configuracion.update({"lista_recursos":resul_list_recursos_configuracion})
                resul_list_configuraciones.append(dic_list_configuracion)
           dic_categoria.update({"lista_configuracion":resul_list_configuraciones})
           resul.append(dic_categoria)
        return {"Consulta_Categoria":resul}
    
    def Get_list_recursos(self):
        resul = []
        for iter in self.list_configuracion.Get_list_recursos().Get_database():
            resul.append(iter.Getting_all_the_data_JSON())
        return {"Consulta_Recursos":resul}
    
    def Get_list_consumos(self):
        resul = []
        for iter in self.list_configuracion.Get_list_consumos().Get_database():
            resul.append(iter.Getting_all_the_data_JSON())
        return {"Consulta_Consumos":resul}
    def Get_list_facturas_clientes(self,NIT_cliente):
        for iter in self.list_configuracion.Get_list_clientes().Get_database(): 
            if iter.Get_NIT() == NIT_cliente:
                return [{"facturas":iter.Get_facturas()},200]
        return [{"MSG":"No existe este cliente en nuestra base de datos"},404]

    #======= Funciones Obtencion de Factura ============
    def Generar_factura(self,firstdate,latestDate):
        if self.list_configuracion.Get_list_consumos().Get_database() == []:
            return {"MSG":"No hay Consumos para poder facturar"}
        firstdate = re.sub("/","-",firstdate)
        latestDate = re.sub("/","-",latestDate)
        Reg_ex_fecha = "[0-9]{1,4}\\-[0-9]{1,2}\\-[0-9]{1,4}"
        resul_fecha = re.findall(Reg_ex_fecha, firstdate)
        
        firstdate1 = resul_fecha[0].split("-")
        Reg_ex_fecha = "[0-9]{1,4}\\-[0-9]{1,2}\\-[0-9]{1,4}"
        resul_fecha2 = re.findall(Reg_ex_fecha, latestDate)
        latestDate1 = resul_fecha2[0].split("-")
        firstdate1 = firstdate1[0]+firstdate1[1]+firstdate1[2]
        
        latestDate1 = latestDate1[0]+latestDate1[1]+latestDate1[2]
        
        Validacion = False
        factura = []
        for iter_consumo in self.list_configuracion.Get_list_consumos().Get_database():
            if int(firstdate1) <= iter_consumo.Get_fecha() <= int(latestDate1):
                
                #=====================Consumo=========================          
                for iter_clientes in self.list_configuracion.Get_list_clientes().Get_database():    
                    if iter_clientes.Get_NIT() == iter_consumo.Get_NIT_Cliente():
                        
                        No_Fac = random.randrange(1000,9999)
                        dic = {
                            "No_Fac": No_Fac,
                            "NIT":iter_clientes.Get_NIT(),
                            "Fecha":latestDate,
                            "ID_Instacia":"",
                            "Monto_a_Pagar":""
                        }
                        dic_factura_especial = {
                            "No_Fac": No_Fac,
                            "NIT":iter_clientes.Get_NIT(),
                            "Fecha":latestDate,
                            "ID_Instacia":"",
                            "Tiempo_del_Cobro":"",
                            "Monto_a_Pagar":"",
                            "Recursos": ""
                        }
                        #==================Cliente ======================
                        ID_instancias = ""
                        suma = 0
                        list_recursos = []
                        for iter_instacia in iter_clientes.Get_List_instancias():
                            if iter_instacia.Get_ID() == iter_consumo.Get_ID_instancia():
                                if iter_instacia.Get_estado().lower() == "vigente" :
                                    pass
                                elif iter_instacia.Get_estado().lower() == "cancelada":
                                    if iter_consumo.Get_fecha() < iter_instacia.Get_fecha_final():
                                        continue
                                    pass
                                Validacion = True
                                #iter_instacia.Set_estado("Cancelado")
                                ID_instancias = iter_instacia.Get_ID()
                                
                                #====================Categoria==============================
                                for iter_categoria in self.list_configuracion.Get_list_categorias().Get_database():
                                    for iter_list_confi in iter_categoria.Get_list_configuracion().Get_database():
                                        if iter_instacia.Get_ID_configuracion() == iter_list_confi.Get_ID():
                                            
                                            for iter_list_recursos in iter_list_confi.Get_list_recursos_configuracion().Get_database():
                                                #=============== recursos ====================
                                                for iter_recursos in self.list_configuracion.Get_list_recursos().Get_database():
                                                    if iter_list_recursos.Get_ID() == iter_recursos.Get_ID():
                                                        valor = iter_list_recursos.Get_cantidad_recurso()* iter_recursos.Get_valorxhora()
                                                        valor = valor * iter_consumo.Get_tiempo()
                                                        
                                                        dic2 = {
                                                            "Recurso_nombre":iter_recursos.Get_nombre(),
                                                            "ValorXHora":iter_recursos.Get_valorxhora()
                                                        }
                                                        list_recursos.append(dic2)
                                                        suma += valor
                                                        pass
                        dic_factura_especial.update({"Tiempo_del_Cobro":iter_consumo.Get_tiempo()})
                        dic.update({"Tiempo_del_Cobro":iter_consumo.Get_tiempo()})
                        dic_factura_especial.update({"Recursos":list_recursos}) 
                        dic_factura_especial.update({"ID_Instacia":ID_instancias}) 
                        dic.update({"ID_Instacia":ID_instancias}) 
                        dic_factura_especial.update({"Monto_a_Pagar":suma})
                        dic.update({"Monto_a_Pagar":suma})
                        if Validacion:
                            iter_clientes.Set_facturas(dic_factura_especial)
                            factura.append(dic)
                            Validacion = False
                            suma = 0
        self.list_configuracion.Get_list_consumos().empty_elements()
        return {"facturas":factura}                           
    def Analisis_de_Ventas_opcion_A(self,firstdate,latestDate):
        resul_first = firstdate.split('/')
        resul_latest = latestDate.split('/')
        agno1 = resul_latest[2]
        agno2 = resul_first[2]
        
        resul_agno = int(agno1)-int(agno2)
        if resul_agno == 0:
            resul_agno = int(resul_latest[1])-int(resul_first[1])
            resul_agno = resul_agno / 12
            resul_agno = resul_agno * 365
            resul_agno = resul_agno - (int(resul_latest[0])- int(resul_first[0]))
            resul_agno = resul_agno * 24
        else:
            resul_agno = resul_agno * 12
            resul_agno = resul_agno - (int(resul_latest[1])-int(resul_first[1]))
            resul_agno = resul_agno / 12
            resul_agno = resul_agno * 365
            resul_agno = resul_agno - (int(resul_latest[0])- int(resul_first[0]))
            resul_agno = resul_agno * 24
        Categorias = []
        for iter_categoria in self.list_configuracion.Get_list_categorias().Get_database():
            dic = {
                "ID_categoria":iter_categoria.Get_ID(),
               
            }
            Configuraciones = []
            for iter_list_confi in iter_categoria.Get_list_configuracion().Get_database():
                suma = 0
                dic2 = {"ID_confi":iter_list_confi.Get_ID()}
                for iter_list_recursos in iter_list_confi.Get_list_recursos_configuracion().Get_database():
                    #=============== recursos ====================
                    for iter_recursos in self.list_configuracion.Get_list_recursos().Get_database():
                        if iter_list_recursos.Get_ID() == iter_recursos.Get_ID():
                            valor = iter_list_recursos.Get_cantidad_recurso()* iter_recursos.Get_valorxhora()
                            valor = valor * resul_agno
                            suma += valor
                            pass
                dic2.update({"Ganancias":suma})
                Configuraciones.append(dic2)
            dic.update({ "Configuraciones":Configuraciones})
            Categorias.append(dic)          
        return [{"Categorias_Ganancias":Categorias},200]
    def Analisis_de_Ventas_opcion_b(self,firstdate,latestDate):
        resul_first = firstdate.split('/')
        resul_latest = latestDate.split('/')
        agno1 = resul_latest[2]
        agno2 = resul_first[2]
        resul_agno = int(agno1)-int(agno2)
        if resul_agno == 0:
            resul_agno = int(resul_latest[1])-int(resul_first[1])
            resul_agno = resul_agno / 12
            resul_agno = resul_agno * 365
            resul_agno = resul_agno - (int(resul_latest[0])- int(resul_first[0]))
            resul_agno = resul_agno * 24
        else:
            resul_agno = resul_agno * 12
            resul_agno = resul_agno - (int(resul_latest[1])-int(resul_first[1]))
            resul_agno = resul_agno / 12
            resul_agno = resul_agno * 365
            resul_agno = resul_agno - (int(resul_latest[0])- int(resul_first[0]))
            resul_agno = resul_agno * 24
        pass
        Recursos = []
        for iter_recursos in self.list_configuracion.Get_list_recursos().Get_database():
            dic = {"Recurso":iter_recursos.Get_nombre()}
            valor = iter_recursos.Get_valorxhora() * resul_agno
            dic.update({"Ganancia":valor})
            Recursos.append(dic)
        return [{"Recursos_Ganancias":Recursos},200] 

                
        
