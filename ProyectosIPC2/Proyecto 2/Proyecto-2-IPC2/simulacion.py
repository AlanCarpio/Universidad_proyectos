from inspect import trace
from ListasEnlazadas import*
import time
class Simulacion:
    def Atencion_clientes(self,list_clientes,trac_empre,escri_empre):
        listadoTransacciones = []
        list_clientes_dot = []
        temp = trac_empre.primero
        while temp!=None:
            listadoTransacciones.append(temp.dato)
            temp = temp.siguiente
        #======================== Lista Clientes ========================
        atencion = ListaSimple()
        nombre_escri = escri_empre
        cliente = list_clientes.primero
        cont_cli = 1
        while cliente!=None:
            atencion.insertar_Empresa(cliente.dato)
            list_clientes_dot.append("cliente_{}".format(cont_cli))
            cont_cli += 1
            cliente = cliente.siguiente
        #primer graficado
        self.archivo_dot(list_clientes_dot,"Vacio",nombre_escri,0)
        while atencion.primero != None:
            traccliente = atencion.obtener_primer().dato.trac
            
            temp = traccliente.primero
            time.sleep(1)
            paciente_silla = list_clientes_dot.pop(0)
            self.archivo_dot(list_clientes_dot,paciente_silla,nombre_escri,0)  
        
            while temp!=None:
                for iter in listadoTransacciones:
                    time.sleep(1/4)  
                    if temp.dato.id == iter.id:
                        cont = int(iter.tiempo)
                        for x in range(1,int(iter.tiempo)+1):
                            self.archivo_dot(list_clientes_dot,paciente_silla,nombre_escri,cont)
                            cont -= 1
                            time.sleep(1)
                            
                    time.sleep(1/4)  
                temp = temp.siguiente
            
            self.archivo_dot(list_clientes_dot,"vacio",nombre_escri,0) 
            time.sleep(1)
        
    def archivo_dot(self,list_clientes,paciente_silla,encargado,tiempo):
        var0 = "{"
        var1 = "}"
        escri = """
        subgraph cluster_1 {0}
        node [style=filled shape="circle"];
        style="filled";
        color="chocolate1";
        label="Escritorios";
        # =============== Escritorios ===============
        subgraph cluster_4 {0}
        node [style=filled shape="circle" rankdir="TB"];
        style="filled";
        color="honeydew4";
        label={tiempo};
        {encargado} [fillcolor = green]
        {encargado} -- {paciente_silla}    
        {1}
        {1}
        """.format(var0,var1,encargado = encargado, paciente_silla = paciente_silla,tiempo = tiempo)
        lib0 = """"""
        for iter in list_clientes:
            lib0 += iter+" "
        clientes = """
        subgraph cluster_5 {0}
        node [style=filled shape="circle"];
        style="filled";
        color="chocolate1";
        label="Pacientes en Espera";
        {asd}
        {1}
        """.format(var0,var1,asd = lib0)
        dot = """
        graph  grafi{0}
        rankdir=TB;
        labelloc="t";
        label="Proyecto 2";
        node[shape="circle"
        fixedsize=true
        width=0.8
        height=0.8
        ];
        {escri}
        {clientes}
        {1}
        """.format(var0,var1,escri = escri,clientes = clientes)
        asd = open("prueba2.dot","w")       
        asd.write(dot)                       