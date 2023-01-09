from multiprocessing.connection import wait
from tkinter import Tk
from Automata import*

class pagina:
    def pagina_html(self,automata_1):
        lista_op = automata_1.tabla_operaciones
        lista_tk = automata_1.tabla_tokensMalos
        lista_ht = automata_1.tabla_HTML
        TextoHT = ""
        TituloHT = ""
        ColorT = ""
        sizeT = 0
        ColorD = ""
        sizeD = 0
        ColorC = ""
        sizeC = 0
        for iter in lista_ht:
            if iter.etiqueta.lower() == "texto":
                TextoHT = iter.datos
            elif iter.etiqueta.lower() == "titulo":
                TituloHT = iter.datos
            elif iter.etiqueta.lower() == "estilo":
                if iter.tipo.lower() == "titulo":
                    ColorT = iter.datos["Color"].lower()
                    sizeT = iter.datos["Tamanio"]
                elif iter.tipo.lower() == "descripcion":
                    ColorD = iter.datos["Color"].lower()
                    sizeD = iter.datos["Tamanio"]
                elif iter.tipo.lower() == "contenido":
                    ColorC = iter.datos["Color"].lower()
                    sizeC = iter.datos["Tamanio"]
        w = """"""
        for asd in lista_op:
            asd.operar()
        for iter2 in lista_op:
            w += """
            <p style="color:{color};font-size:{size}px">{tipo} ---- >{res}</p>
            """.format(tipo = iter2.tipo,res = iter2.datos,color = ColorC,size = sizeC)
        tabla = """"""
        if len(lista_tk) != 0:
            
            for iter2 in lista_tk:
                tabla += """
                <tr>
                <td>{Fila}</td>
                <td>{Columna}</td>
                <td>{Lexema}</td>
                </tr>
                """.format(Fila = iter2.fila,Columna = iter2.columna,Lexema = iter2.token)
            pass
        else:
            tabla = """<h2 style="color:black;font-size:3px">No hay Errores Lexicos</h2>"""
        stile = """
        <style>
            table, th, td {
                border:1px solid black;
            }
        </style>
        """
        indexHt = """
        <!DOCTYPE html>
        <html>
            <head>
            <title>Operaciones</title>
            </head>
            {stile}
            <body>
            <h1 style="color:{colorT};font-size:{sizeT}px">{Titulo}</h1>
            <h2 style="color:{colorD};font-size:{sizeD}px">{Texto}</h2>
            {tipo}
            <table style="font-size:3px">
            <tr>
            <th>Fila</th>
            <th>Columna</th>
            <th>Lexema</th>
            </tr>
            {tabla}
            </table>
            
            </body>
        </html>
        """.format(Titulo = TituloHT,Texto = TextoHT,colorT = ColorT,sizeT = sizeT,colorD = ColorD,sizeD = sizeD,tipo = w,tabla = tabla,stile = stile)
        return indexHt
    

