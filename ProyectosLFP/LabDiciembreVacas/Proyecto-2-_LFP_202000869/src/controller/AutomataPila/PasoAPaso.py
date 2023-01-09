import graphviz
class PasoAPaso():
    def __init__(self,Name_AUP,data_AUP) -> None:
        self.Name_AUP = Name_AUP
        self.data_AUP = data_AUP
        self.entrada = ''
        self.Pila = []
        self.EstadoWhile = True
        
    def GrafoPasoaPaso(self,char_cadena,Estado_actual,EstadoCadena):
        
        self.dot = graphviz.Digraph(name='GrafoPasoAPaso',format='png')
        self.dot.attr(rankdir = 'LR',shape = 'circle')
        for iter in self.data_AUP:
            if iter.Get_info()[0] == self.Name_AUP:
                self.dot.node(name='Inicio',shape = 'box',fillcolor = 'red',style = 'filled')
                self.dot.node(name=iter.Get_info()[4],shape = 'circle',)
                for iter3 in iter.Get_info()[3].split(','):
                    if iter3 not in iter.Get_info()[5].split(','):
                        if iter3 == Estado_actual:
                            self.dot.node(name = iter3,shape = 'circle',fillcolor = 'yellow',style = 'filled')
                        else:
                            self.dot.node(name = iter3,shape = 'circle')
                    else:
                        if iter3 == Estado_actual:
                            self.dot.node(name = iter3,shape = 'doublecircle',fillcolor = 'yellow',style = 'filled')
                            self.EstadoWhile = False
                        else:
                            self.dot.node(name = iter3,shape = 'doublecircle')
                self.dot.edge('Inicio',iter.Get_info()[4])
                
                for iter2 in iter.Get_info()[6]:
                    resul = iter2.Get_All()
                    self.dot.edge(resul[0],resul[1],label=f'{resul[2][0]},{resul[2][1]},{resul[2][2]}')
                try:
                    if char_cadena[2] != '$':
                        self.Pila.remove(char_cadena[2])
                except ValueError:
                    #self.EstadoWhile = False
                    pass
                if char_cadena[3] != '$':
                    self.Pila.append(char_cadena[3])
                PilaNodo = ''.join(self.Pila)
                
                if char_cadena[1] != '$':
                    self.entrada += char_cadena[1]
                self.dot.node(name = 'Entrada',label=f'''<<TABLE>
                            <TR>
                            <TD>Entrada:</TD>
                            <TD>{self.entrada}</TD>
                            </TR>
                            <TR>
                            <TD>Pila:</TD>
                            <TD>{PilaNodo}</TD>
                            </TR>
                            </TABLE>>''',shape = 'plaintext')
                
                if EstadoCadena == 2:
                    pass
                elif EstadoCadena == 0:
                    self.dot.node(name='0',label='Cadena Invalida',shape = 'plaintext',fillcolor = 'red')
                    self.dot.edge('Entrada','0')
                elif EstadoCadena == 1:
                    self.dot.node(name = '1',label='Cadena Valida',shape = 'plaintext',fillcolor = 'green')
                    self.dot.edge('Entrada','1')
                self.dot.render(format='png',directory='C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos')
                return self.EstadoWhile