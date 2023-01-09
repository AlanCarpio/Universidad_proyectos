"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Inicio),
    path('ConsultarClientes/',views.ConsultarClientes,name="ConsultarClientes"),
    path('ConsultarCategorias/',views.ConsultarCategorias,name="ConsultarCategorias"),
    path('ConsultarRecursos/',views.ConsultarRecursos,name="ConsultarRecursos"),
    path('ConsultarConsumos/',views.ConsultarConsumos,name="ConsultarConsumos"),
    path('TempleteConfig/',views.TemplateConfig,name="TempleteConfig"),
    path('SendConfig/',views.SendConfig,name="SendConfig"),
    path('TemplateConsumo/',views.TemplateConsumo,name="TemplateConsumo"),
    path('SendConfigConsumo/',views.SendConfigConsumo,name="SendConfigConsumo"),
    path('NewCliente/',views.NewCliente,name="NewCliente"),
    path('NewClientesend/',views.NewClientesend,name="NewClientesend"),
    path('NewInstanciasend/',views.NewInstanciasend,name="NewInstanciasend"),
    path('NewRecurso/',views.NewRecurso,name="NewRecurso"),
    path('NewRecursosend/',views.NewRecursosend,name="NewRecursosend"),
    path('NewCategoria/',views.NewCategoria,name="NewCategoria"),
    path('NewCategoriasend/',views.NewCategoriasend,name="NewCategoriasend"),
    path('NewConfisend/',views.NewConfisend,name="NewConfisend"),
    path('NewRecusend/',views.NewRecusend,name="NewRecusend"),
    path('Facturacion/',views.Facturacion,name="Facturacion"),
    path('Facturar/',views.Facturar,name="Facturar"),
    path('GananciasA/',views.GananciasA,name="GananciasA"),
    path('GananciasB/',views.GananciasB,name="GananciasB")

]
