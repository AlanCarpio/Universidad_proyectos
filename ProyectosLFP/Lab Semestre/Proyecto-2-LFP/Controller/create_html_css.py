class create():
    def __init__(self,_list_html,_list_css) -> None:
        self.list_css = _list_css
        self.list_html = _list_html
        pass
    def create_html(self):
        resul_HTML_final = """"""
        resul_HTML_final2 = """"""
        def obtener_datos_Eti(iter3):
            for iter in self.list_css.data:
                if iter3.ID == iter.ID:
                    if iter.propiedad == "setTexto":
                        return iter.valor
        def obtener_datos_Boton(iter3):
            text = ""
            ali = ""
            for iter in self.list_css.data:
                if iter3.ID == iter.ID:
                    if iter.propiedad == "setTexto":
                        text = iter.valor
                    elif iter.propiedad == "setAlineacion":
                        ali = iter.valor
            if ali == "":
                ali = "left"
            return [text,ali]
        def obtener_datos_check(iter3):
            text = ""
            setmarca = ""
            for iter in self.list_css.data:
                if iter3.ID == iter.ID:
                    if iter.propiedad == "setMarcada":
                        setmarca = iter.valor
                    if iter.propiedad == "setTexto":
                        text = iter.valor    
            return [text,setmarca]
        def obtener_datos_radio(iter3):
            group = ""
            text = ""
            ali = ""
            for iter in self.list_css.data:
                if iter3.ID == iter.ID:
                    if iter.propiedad == "setGrupo":
                        group = iter.valor
                    elif iter.propiedad == "setMarcada":
                        ali = iter.valor
                    elif iter.propiedad == "setTexto":
                        text = iter.valor
            return [group,text,ali]
        def obtener_datos_Texto(iter3):
            text = ""
            ali = ""
            for iter in self.list_css.data:
                if iter3.ID == iter.ID:
                    if iter.propiedad == "setTexto":
                        text = iter.valor
                    elif iter.propiedad == "setAlineacion":
                        ali = iter.valor
            if ali == "":
                ali = "left"
            return [text,ali]
        def obtener_datos_AreaTexto(iter3):
            text = ""
            ali = ""
            for iter in self.list_css.data:
                if iter3.ID == iter.ID:
                    if iter.propiedad == "setTexto":
                        text = iter.valor
            return text
        def obtener_datos_Clave(iter3):
            text = ""
            ali = ""
            for iter in self.list_css.data:
                if iter3.ID == iter.ID:
                    if iter.propiedad == "setTexto":
                        text = iter.valor
                    elif iter.propiedad == "setAlineacion":
                        ali = iter.valor
            if ali == "":
                ali = "left"
            return [text,ali]
        def comprobacion(comproba):
            resul = """"""
            add = """"""
            for iter2 in self.list_css.data:
                if iter2.ID == comproba.ID:
                    if iter2.propiedad == "add":
                        for iter3 in self.list_html.data:
                            if iter2.valor == iter3.ID:
                                if iter3.contenedor == "Contenedor":
                                    resul = comprobacion(iter3)
                                    div1 = """
                                    <div id = "{}">
                                    {}
                                    </div>""".format(iter3.ID,resul)
                                    add += div1
                                    continue
                                elif iter3.contenedor == "Etiqueta":
                                    resul_Eti = obtener_datos_Eti(iter3)
                                    resul = """
                                    <label id="{}">{}</label>""".format(iter3.ID,resul_Eti)
                                elif iter3.contenedor == "Boton":
                                    resul_boton = obtener_datos_Boton(iter3)
                                    resul = """
                                    <input type="submit" id="{}" value="{}"style="text-align: {}"/>""".format(iter3.ID,resul_boton[0],resul_boton[1])
                                elif iter3.contenedor == "Check":
                                    resul_check = obtener_datos_check(iter3)
                                    resul = """
                                    <input type="checkbox" id="{}"{} />{}""".format(iter3.ID,resul_check[1],resul_check[0])
                                elif iter3.contenedor == "RadioBoton":
                                    resul_radio = obtener_datos_radio(iter3)
                                    resul = """
                                    <input type="radio" name="{}" id="{}"{} />{}""".format(resul_radio[0],iter3.ID,resul_radio[2],resul_radio[1])
                                elif iter3.contenedor == "Texto":
                                    resul_boton = obtener_datos_Texto(iter3)
                                    resul = """
                                    <input type = "text" id="{}" value="{}"style="text-align: {}" />""".format(iter3.ID,resul_boton[0],resul_boton[1])
                                elif iter3.contenedor == "AreaTexto":
                                    resul_area = obtener_datos_AreaTexto(iter3)
                                    resul = """
                                    <TEXTAREA id="{}">
                                    {}
                                    </TEXTAREA>""".format(iter3.ID,resul_area)
                                elif iter3.contenedor == "Clave":
                                    resul_boton = obtener_datos_Clave(iter3)
                                    resul = """
                                    <input type = "password" id="{}"value="{}" style="text-align: {}"/>""".format(iter3.ID,resul_boton[0],resul_boton[1])
                                add += resul
            return add        
        def html_add(iter):
            div = """"""
            div1 = """"""
            for iter1 in self.list_html.data:
                if iter.valor == iter1.ID:
                    if iter1.contenedor == "Contenedor":
                        asd = comprobacion(iter1)
                        div1 = """
                        <div id = "{}">
                        {}
                        </div>""".format(iter.valor,asd)
                    div += div1
            return div
        for iter in self.list_css.data:
            if iter.ID == "this":
                resul_HTML_final = html_add(iter)
                resul_HTML_final2 += resul_HTML_final
        code_html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="index.css" />
            <title>Proyecto 3</title>
        </head>
        <body>
        {}    
        </body>
        </html>
        """.format(resul_HTML_final2)   
        asd = open("./documentation/index.html","w")       
        asd.write(code_html)
      
    def create_css(self):
        def recursividad_css(iter):
            list_css_sets = ["setColorLetra","setColorFondo","setAncho","setAlto","setPosicion"]
            css = """"""
            resul_style = """"""
            for iter1 in self.list_css.data:
                if iter.ID == iter1.ID:
                    if iter1.propiedad == "setColorLetra":
                        style = """
                        color: rgb({},{},{});""".format(iter1.valor['R'],iter1.valor['G'],iter1.valor['B'])
                    elif iter1.propiedad == "setColorFondo":
                        style = """
                        background-color:rgb({},{},{});""".format(iter1.valor['R'],iter1.valor['G'],iter1.valor['B'])
                    elif iter1.propiedad == "setAncho":
                        style = """
                        width :{}px;""".format(iter1.valor)
                    elif iter1.propiedad == "setAlto":
                        style = """
                        height :{}px;""".format(iter1.valor)
                    elif iter1.propiedad == "setPosicion":
                        style = """
                        position: absolute;
                        left: {}px; 
                        top: {}px;
                        """.format(iter1.valor["x"],iter1.valor["y"])
                    else: 
                        style = """"""
                    resul_style += style       
            css_style = """
            #{ID}{0}
                        font-size: 12px;
            {valor}
            {1}
            """.format("{","}",valor = resul_style,ID = iter.ID)
            return css_style
        css_resul = """"""
        for iter in self.list_html.data:
            resul_style = recursividad_css(iter)
            css_resul += resul_style
        #print(css_resul)
        asd = open("./documentation/index.css","w")       
        asd.write(css_resul)
    
    