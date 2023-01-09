from django.shortcuts import HttpResponseRedirect, render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from app.forms import StudentForm
import requests
def Inicio(request):
    return render(request,"index.html")
#============= Funciones Consultar Datos ================
def ConsultarClientes(request):
    try:
        peticion = {"Consultar":"Clientes"}
        r = requests.post("http://localhost:4000/servicio2/ConsultarDatos",json=peticion)
        r = r.json()
        return render(request, "consultar/consultar_usuarios.html",r)
    except requests.exceptions.ConnectionError:
        return render(request, "consultar/consultar_usuarios.html")
def ConsultarCategorias(request):
    try:
        peticion = {"Consultar":"Categorias"}
        r = requests.post("http://localhost:4000/servicio2/ConsultarDatos",json=peticion)
        r = r.json()
        return render(request, "consultar/consultar_categorias.html",r)
    except requests.exceptions.ConnectionError:
        return render(request, "consultar/consultar_categorias.html")
def ConsultarRecursos(request):
    try:
        peticion = {"Consultar":"Recursos"}
        r = requests.post("http://localhost:4000/servicio2/ConsultarDatos",json=peticion)
        r = r.json()
        return render(request, "consultar/consultar_recurso.html",r)
    except requests.exceptions.ConnectionError:
        return render(request, "consultar/consultar_recurso.html")
def ConsultarConsumos(request):
    try:
        peticion = {"Consultar":"Consumos"}
        r = requests.post("http://localhost:4000/servicio2/ConsultarDatos",json=peticion)
        r = r.json()
        return render(request, "consultar/consultar_consumo.html",r)
    except requests.exceptions.ConnectionError:
        return render(request, "consultar/consultar_consumo.html")
#=====================Envio de configuraciones=========================================
def TemplateConfig(request):
    
    return render(request,"Send_XML_template/Enviar_configuracion.html")
@csrf_exempt 
def SendConfig(request):
    if request.method == "POST":
        file = request.POST['document']  
        dic =  {"resul":"True"}
    return render(request,"Send_XML_template/Enviar_configuracion.html",dic)
def TemplateConsumo(request):
    
    return render(request,"Send_XML_template/Enviar_configuracion_consu.html")
@csrf_exempt 
def SendConfigConsumo(request):
    if request.method == "POST":
        file = request.POST['document']  
        dic =  {"resul":"True"}
    return render(request,"Send_XML_template/Enviar_configuracion_consu.html",dic)    
#==================== Nuevos Datos =======================================================
def NewCliente(request):
    return render(request,"Nueva_data/New_Clientes.html")    
@csrf_exempt
def NewClientesend(request):
    
    if request.method == "POST":
        dic ={
        "NIT": request.POST["NIT"],
        "Nombre":request.POST["Nombre"],
        "Usuario": request.POST["Usuario"],
        "Password": request.POST["Password"],
        "Dirrecion": request.POST["Dirrecion"],
        "Email": request.POST["Email"]
        }
        r = requests.post("http://localhost:4000/servicio2/CrearCliente",json=dic)
        r = r.json()
        return render(request,"Nueva_data/New_Clientes.html",r)    
    return render(request,"Nueva_data/New_Clientes.html")
@csrf_exempt
def NewInstanciasend(request):
    if request.method == "POST":
        dic ={
        "NIT_Cliente": request.POST["NIT_Cliente"],
        "ID":request.POST["ID"],
        "ID_Configuracion": request.POST["ID_Configuracion"],
        "Nombre": request.POST["Nombre"],
        "FechaInicial": request.POST["FechaInicial"],
        "Estado": request.POST["Estado"],
        "Fechafinal": request.POST["Fechafinal"]
        }
        r = requests.post("http://localhost:4000/servicio2/CrearInstancia",json=dic)
        r = r.json()
        return render(request,"Nueva_data/New_Clientes.html",r)    
    return render(request,"Nueva_data/New_Clientes.html")        
def NewRecurso(request):
    return render(request,"Nueva_data/New_Recurso.html")    
@csrf_exempt
def NewRecursosend(request):
    if request.method == "POST":
        dic ={
        "ID": request.POST["ID"],
        "Nombre":request.POST["Nombre"],
        "Abreviatura": request.POST["Abreviatura"],
        "Metrica": request.POST["Metrica"],
        "Tipo": request.POST["Tipo"],
        "valorxHora": request.POST["valorxHora"]
        }
        r = requests.post("http://localhost:4000/servicio2/CrearRecurso",json=dic)
        r = r.json()
        return render(request,"Nueva_data/New_Recurso.html",r)      
    return render(request,"Nueva_data/New_Clientes.html")
#======================= Categorias
def NewCategoria(request):
    return render(request,"Nueva_data/New_Categoria.html")    
@csrf_exempt
def NewCategoriasend(request):
    
    if request.method == "POST":
        dic ={
        "ID": request.POST["ID"],
        "Nombre":request.POST["Nombre"],
        "Abreviatura": request.POST["Abreviatura"],
        "Carga_Trabajo": request.POST["Carga_Trabajo"]
        }
        r = requests.post("http://localhost:4000/servicio2/CrearCategoria",json=dic)
        r = r.json()
        return render(request,"Nueva_data/New_Categoria.html",r)    
    return render(request,"Nueva_data/New_Categoria.html")
@csrf_exempt
def NewConfisend(request):
    if request.method == "POST":
        dic ={
        "ID_Categoria": request.POST["ID_Categoria"],
        "ID":request.POST["ID"],
        "Nombre": request.POST["Nombre"],
        "Descripcion": request.POST["Descripcion"]
        }
        r = requests.post("http://localhost:4000/servicio2/CrearListaConfiguracion",json=dic)
        r = r.json()
        return render(request,"Nueva_data/New_Categoria.html",r)    
    return render(request,"Nueva_data/New_Categoria.html")
@csrf_exempt
def NewRecusend(request):
    if request.method == "POST":
        dic ={
        "ID_Categoria": request.POST["ID_Categoria"],
        "ID_list_configuracion":request.POST["ID_list_configuracion"],
        "ID": request.POST["ID"],
        "Cantidad_recursos": request.POST["Cantidad_recursos"]
        }
        r = requests.post("http://localhost:4000/servicio2/CrearRecursoConfiguracion",json=dic)
        r = r.json()
        return render(request,"Nueva_data/New_Categoria.html",r)    
    return render(request,"Nueva_data/New_Categoria.html")
#============================= Funciones de Facturacion =========================
@csrf_exempt
def Facturacion(request):
    if request.method == "POST":
        dic = {
            "FirstDate":request.POST["FirstDate"],
            "LatestDate":request.POST["LatestDate"]
        }
        r = requests.post("http://localhost:4000/servicio2/GenerarFactura",json = dic)
        r = r.json()
        return render(request,"Facturacion/Generar_facturas.html",r)
    return render(request,"Facturacion/Generar_facturas.html")
@csrf_exempt
def Facturar(request):
    if request.method == "POST":
        dic = {
        "NIT_Cliente":request.POST['NIT_Cliente']
        }
        r = requests.post("http://localhost:4000/servicio2/ConsultarFacturas",json=dic)
        r = r.json()
        return render(request,"Facturacion/Buscar_facturas.html",r)
    return render(request,"Facturacion/Buscar_facturas.html")
@csrf_exempt
def GananciasA(request):
    if request.method == "POST":
        dic = {
            "FirstDate":request.POST["FirstDate"],
            "LatestDate":request.POST["LatestDate"]
        }
        r = requests.post("http://localhost:4000/servicio2/AnalisisdeVentasopcionA",json = dic)
        r = r.json()
        return render(request,"Facturacion/Analisis_A.html",r)
    return render(request,"Facturacion/Analisis_A.html")
@csrf_exempt
def GananciasB(request):
    if request.method == "POST":
        dic = {
            "FirstDate":request.POST["FirstDate"],
            "LatestDate":request.POST["LatestDate"]
        }
        r = requests.post("http://localhost:4000/servicio2/AnalisisdeVentasopcionb",json = dic)
        r = r.json()
        return render(request,"Facturacion/Analisis_B.html",r)
    return render(request,"Facturacion/Analisis_B.html")
        
      
    