import graphviz
class RutaPasada():
    def __init__(self,Name_AUP,data_AUP,Transiciones) -> None:
        self.Name_AUP = Name_AUP
        self.data_AUP = data_AUP
        self.entrada = ''
        self.Pila = []
        self.PilaTabla = []
        self.EntradaTabla = []
        self.Transiciones = Transiciones
        self.EstadoWhile = True
        
    def GrafoPasoaPaso(self,char_cadena):
        
        for iter in self.data_AUP:
            if iter.Get_info()[0] == self.Name_AUP:
                if char_cadena[2] == '$' and char_cadena[3] == '$':
                    asd = ''.join(self.Pila)
                    self.PilaTabla.append(asd)
                else:
                    try:
                        if char_cadena[2] != '$':
                            self.Pila.remove(char_cadena[2])
                            asd = ''.join(self.Pila)
                            self.PilaTabla.append(asd)


                    except ValueError:
                        #self.EstadoWhile = False
                        pass
                    if char_cadena[3] != '$':
                        self.Pila.append(char_cadena[3])
                        asd = ''.join(self.Pila)
                        self.PilaTabla.append(asd)

                if char_cadena[1] != '$':
                    self.entrada += char_cadena[1]
                    self.EntradaTabla.append(self.entrada)
                else:
                    self.EntradaTabla.append(self.entrada)

                
                return self.EstadoWhile
    def Get_Pila(self):
        self.PilaTabla.append(self.PilaTabla[-1])
        self.EntradaTabla.append(self.EntradaTabla[-1])
        self.Transiciones.append('')
        All = """"""
        self.EntradaTabla = self.EntradaTabla[1:]
        self.cont = len(self.Transiciones)
        
        for x in range(self.cont):
            Tabla = f"""
            <TR>
            <TD>{x}</TD>
            <TD>{self.PilaTabla[x]}</TD>
            <TD>{self.EntradaTabla[x]}</TD>
            <TD>{self.Transiciones[x]}</TD>
            </TR>
            """
            All = All + Tabla
            pass
        
        self.dot = graphviz.Digraph(name='RutaPasada',format='png')
        self.dot.attr(rankdir = 'LR',shape = 'circle')
        self.dot.node(name = 'Entrada',label=f'''<<TABLE>
                            <TR>
                            <TD>Iteracion</TD>
                            <TD>Pila</TD>
                            <TD>Entrada</TD>
                            <TD>Transicion</TD>
                            </TR>
                            {All}
                            
                            </TABLE>>''',shape = 'plaintext')
        self.dot.render(format='png',directory='C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos')
        return 