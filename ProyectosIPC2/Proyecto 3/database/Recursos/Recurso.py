import xml.etree.ElementTree as ET
class recurso():
    def __init__(self,_ID,_nombre,_abreviatura,_metrica,_tipo,_valorxhora:int) -> None:
        self.__ID = _ID
        self.__nombre = _nombre
        self.__abreviatura = _abreviatura
        self.__metrica = _metrica
        self.__tipo = _tipo
        self.__valorxhora = _valorxhora
        pass
    def Getting_all_the_data_JSON(self):
        dic = {
            "ID": self.__ID,
            "Nombre": self.__nombre,
            "Abreviatura": self.__abreviatura,
            "Metrica": self.__metrica,
            "Tipo": self.__tipo,
            "ValorxHora": self.__valorxhora
        }
        return dic 
    def Get_ID(self):
        return self.__ID
    def Get_valorxhora(self):
        return float(self.__valorxhora)
    def Get_nombre(self):
        return self.__nombre
    def Get_data_xml(self,listaRecursos):
        recurso = ET.SubElement(listaRecursos,"recurso", id = self.__ID)
        nombre = ET.SubElement(recurso,"nombre").text(str(self.__nombre))
        nombre = ET.SubElement(recurso,"nombre").text(str(self.__nombre))
        nombre = ET.SubElement(recurso,"nombre").text(str(self.__nombre))
        nombre = ET.SubElement(recurso,"nombre").text(str(self.__nombre))
        nombre = ET.SubElement(recurso,"nombre").text(str(self.__nombre))