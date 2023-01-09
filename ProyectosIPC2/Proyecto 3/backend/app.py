
from backend.Config_controller import config_controller
from flask import Flask, render_template ,jsonify,request,redirect,url_for
from flask_cors import CORS
from backend.config import config
import os
app = Flask(__name__)
app.config.from_object(config['development'])
# index
Configuracion = config_controller()
#================== [Rutas para el frontend] =======================
def Update_database():
    if os.path.exists("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/database/Datebase_XML/database.xml"):
        Configuracion.read_xml("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/database/Datebase_XML/database.xml")
    else:
        pass
@app.route('/' , methods = ["POST"])
def index():
    peticion = request.get_json()
    print(peticion)
    return {"Hola":"NameUser{} |Pass{}".format(peticion.get("NameUser"),peticion.get("Password"))}
#=============[ Rutas Servicio 2 consumidas por Postman ]================

@app.route('/servicio2/CrearRecurso',methods = ["POST"])
def CrearRecurso():
    peticion = request.get_json()
    resul =  Configuracion.create_recurso(peticion.get("ID"),peticion.get("Nombre"),peticion.get("Abreviatura"),peticion.get("Metrica"),peticion.get("Tipo"),int(peticion.get("valorxHora")))
    return jsonify(resul[0]),resul[1]
#============ Rutas Clientes =============================
@app.route('/servicio2/CrearCliente',methods = ["POST"])
def CrearCliente():
    peticion = {
        "NIT": request.json["NIT"],
        "Nombre": request.json["Nombre"],
        "Usuario": request.json["Usuario"],
        "Password": request.json["Password"],
        "Dirrecion": request.json["Dirrecion"],
        "Email": request.json["Email"]
    }
    resul = Configuracion.create_cliente(peticion.get("NIT"),peticion.get("Nombre"),peticion.get("Usuario"),peticion.get("Password"),peticion.get("Dirrecion"),peticion.get("Email"))
    return jsonify(resul[0]),resul[1]

@app.route('/servicio2/CrearInstancia',methods = ["POST"])
def CrearInstancia():
    peticion = request.get_json()
    resul = Configuracion.create_instacia(peticion.get("NIT_Cliente"),peticion.get("ID"),peticion.get("ID_Configuracion"),peticion.get("Nombre"),peticion.get("FechaInicial"),peticion.get("Estado"),peticion.get("Fechafinal"))
    return jsonify(resul[0])

#===================== Rutas Categorias ==============================
@app.route('/servicio2/CrearCategoria',methods = ["POST"])
def CrearCategoria():
    peticion = request.get_json()
    resul =  Configuracion.create_categoria(
        peticion.get("ID"),peticion.get("Nombre"),peticion.get("Abreviatura"),peticion.get("Carga_Trabajo"))
    return jsonify(resul[0])
@app.route('/servicio2/CrearListaConfiguracion',methods = ["POST"])
def CrearListaConfiguracion():
    peticion = request.get_json()
    resul =  Configuracion.create_ListaConfiguraciones(
        peticion.get("ID_Categoria"),peticion.get("ID"),peticion.get("Nombre"),peticion.get("Descripcion"))
    return jsonify(resul[0])
@app.route('/servicio2/CrearRecursoConfiguracion',methods = ["POST"])
def CrearRecursoConfiguracion():
    peticion = request.get_json()
    resul =  Configuracion.create_RecursosConfiguracion(
        peticion.get("ID_Categoria"),peticion.get("ID_list_configuracion"),peticion.get("ID"),peticion.get("Cantidad_recursos"))
    return jsonify(resul[0])
#========================= Carga de datos XML ===========================

@app.route('/servicio2/CargarConfiguracion',methods = ["POST"])
def CargarConfiguracion():
    peticion = request.get_data()
    if os.path.exists("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/database/Datebase_XML/database.xml"):
        asd = open("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_Config_temporal.xml","wb")       
        asd.write(peticion)
        asd.close()
        return jsonify({"MSG":"Archivo xml recibido"})
    else:      
        asd = open("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/database/Datebase_XML/database.xml","wb")       
        asd.write(peticion)
        asd.close()
        asd = open("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_Config_temporal.xml","wb")       
        asd.write(peticion)
        asd.close()
        return jsonify({"MSG":"Archivo xml recibido"})

@app.route('/servicio2/CargarConsumo',methods = ["POST"])
def CargarConsumo():
    peticion = request.get_data()
    asd = open("C:/Users/Krpi/Documents/Python/Proyecto_3_IPC2_202000869/backend/Received_files/XML_consumo_temporal.xml","wb")       
    asd.write(peticion)
    asd.close()
    return jsonify({"MSG":"Archivo xml recibido"})


#================Rutas De Obtecion de datos==========================================
@app.route('/servicio2/ConsultarDatos',methods = ["POST"])
def ConsultarDatos():
    peticion = request.get_json()
    Configuracion.conprobacion_xml_config()
    Configuracion.conprobacion_xml_consumo()
    if peticion.get("Consultar") == "Clientes":
        resul = Configuracion.Get_list_Clientes_and_Instancias()
        return jsonify(resul),202
    elif peticion.get("Consultar") == "Categorias":
        resul = Configuracion.Get_list_Categorias()
        return jsonify(resul),202
    elif peticion.get("Consultar") == "Recursos":
        resul = Configuracion.Get_list_recursos()
        return jsonify(resul),202
    elif peticion.get("Consultar") == "Consumos":
        resul = Configuracion.Get_list_consumos()
        return jsonify(resul),202
    else:
        return jsonify({"MSG":"Ingrese un dato de consulta valido"})
@app.route('/servicio2/ConsultarFacturas',methods = ["POST"])
def ConsultarFacturas():
    peticion = request.get_json()
    resul = Configuracion.Get_list_facturas_clientes(peticion.get("NIT_Cliente"))
    return jsonify(resul[0]),resul[1]

#================ Rutas De Generacion Factura ==========================================
@app.route('/servicio2/GenerarFactura',methods = ["POST"])
def GenerarFactura():
    peticion = request.get_json()

    resul = Configuracion.Generar_factura(peticion.get("FirstDate"),peticion.get("LatestDate"))
    return jsonify(resul)
    pass
@app.route('/servicio2/AnalisisdeVentasopcionA',methods = ["POST"])
def Analisis_de_Ventas_opcion_A():
    peticion = request.get_json()
    resul = Configuracion.Analisis_de_Ventas_opcion_A(peticion.get("FirstDate"),peticion.get("LatestDate"))
    return jsonify(resul[0])
    pass
@app.route('/servicio2/AnalisisdeVentasopcionb',methods = ["POST"])
def Analisis_de_Ventas_opcion_b():
    peticion = request.get_json()
    resul = Configuracion.Analisis_de_Ventas_opcion_b(peticion.get("FirstDate"),peticion.get("LatestDate"))
    return jsonify(resul[0])
    pass

