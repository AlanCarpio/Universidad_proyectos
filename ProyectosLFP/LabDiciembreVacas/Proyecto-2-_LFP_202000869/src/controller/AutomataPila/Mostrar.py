import graphviz
class Mostrar():
    def __init__(self,Name_AUP,data_AUP) -> None:
        self.Name_AUP = Name_AUP
        self.data_AUP = data_AUP
        self.dot = graphviz.Digraph(name='AutomataDePila',format='pdf')
        self.dot.attr(rankdir = 'LR',shape = 'circle')
    def MostrarInfoAuto(self):
        for iter in self.data_AUP:
            if iter.Get_info()[0] == self.Name_AUP:
                self.dot.node(name='Inicio',shape = 'box',fillcolor = 'red',style = 'filled')
                self.dot.node(name=iter.Get_info()[4],shape = 'circle',)
                for iter3 in iter.Get_info()[3].split(','):
                    if iter3 not in iter.Get_info()[5].split(','):
                        self.dot.node(name = iter3,shape = 'circle')
                    else:
                        self.dot.node(name = iter3,shape = 'doublecircle')
                        pass
                self.dot.edge('Inicio',iter.Get_info()[4])
                for iter2 in iter.Get_info()[6]:
                    resul = iter2.Get_All()
                    self.dot.edge(resul[0],resul[1],label=f'{resul[2][0]},{resul[2][1]},{resul[2][2]}')
                self.dot.node(name = f"Nombre: {iter.Get_info()[0]}\n\nAlfabeto: {iter.Get_info()[1]}\n\nSimbolos Pila: {iter.Get_info()[2]}\n\nEstados: {iter.Get_info()[3]}\n\nEstado Inicial: {iter.Get_info()[4]}\n\nEstado Aceptacion: {iter.Get_info()[5]}",shape = 'box')
                return self.dot.render(format='pdf',directory='C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos',view=True)
        