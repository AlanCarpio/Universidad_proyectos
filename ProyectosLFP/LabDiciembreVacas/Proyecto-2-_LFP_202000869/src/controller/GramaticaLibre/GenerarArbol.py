import graphviz

class GenerarArbol():
    def __init__(self,Name_GRC,data_GRC) -> None:
        self.Name_GRC = Name_GRC
        self.data_GRC = data_GRC
        self.dot = graphviz.Graph(name='Gramatica',format='pdf')
        self.dot.attr(rankdir = 'LB',shape = 'circle')
        pass
    def BuildTree(self):
        for iter in self.data_GRC:
            if iter.Get_DatosGramatica()[0] == self.Name_GRC:
                contNode = 0
                OrigenAnterior = ''
                for iter2 in iter.Get_DatosGramatica()[4]:
                    if len(iter2.Get_Destinos()) == 1:
                        if iter2.Get_Origen() == iter.Get_DatosGramatica()[3]:
                            contNode += 1
                            Nombre1 = 'node{}'.format(contNode)
                            contNode += 1
                            Nombre2 = 'node{}'.format(contNode)
                            OrigenAnterior = Nombre2
                            self.dot.node(Nombre1,label=iter2.Get_Origen(),shape = 'circle')
                            self.dot.node(Nombre2,label=iter2.Get_Destinos()[0],shape = 'circle')
                            self.dot.edge(Nombre1,Nombre2,shape = None)
                        else:
                            if iter2.Get_Destinos()[0] in iter.Get_DatosGramatica()[2].split(','):
                                contNode += 1
                                Nombre1 = 'node{}'.format(contNode)
                                contNode += 1
                                Nombre2 = 'node{}'.format(contNode)
                                self.dot.node(Nombre1,label=iter2.Get_Origen(),shape = 'circle')
                                self.dot.node(Nombre2,label=iter2.Get_Destinos()[0],shape = 'circle')
                                self.dot.edge(OrigenAnterior,Nombre1)
                                self.dot.edge(Nombre1,Nombre2,shape = None)
                                OrigenAnterior = Nombre2
                            else:
                                contNode += 1
                                Nombre1 = 'node{}'.format(contNode)
                                contNode += 1
                                Nombre2 = 'node{}'.format(contNode)
                                self.dot.node(Nombre2,label=iter2.Get_Destinos()[0],shape = 'circle')
                                self.dot.edge(OrigenAnterior,Nombre2,shape = None)
                                OrigenAnterior = Nombre2
                       
                        pass
                    elif len(iter2.Get_Destinos()) == 2:
                        contNode += 1
                        Nombre1 = 'node{}'.format(contNode)
                        contNode += 1
                        Nombre2 = 'node{}'.format(contNode)
                        self.dot.node(Nombre1,label=iter2.Get_Destinos()[0],shape = 'circle')
                        self.dot.node(Nombre2,label=iter2.Get_Origen(),shape = 'circle')
                        self.dot.edge(OrigenAnterior,Nombre1)
                        self.dot.edge(OrigenAnterior,Nombre2)
                        OrigenAnterior = Nombre2
                        pass
                    elif len(iter2.Get_Destinos()) == 3:
                        contNode += 1
                        Nombre1 = 'node{}'.format(contNode)
                        contNode += 1
                        Nombre2 = 'node{}'.format(contNode)
                        contNode += 1
                        Nombre3 = 'node{}'.format(contNode)
                        self.dot.node(Nombre1,label=iter2.Get_Destinos()[0],shape = 'circle')
                        self.dot.node(Nombre3,label=iter2.Get_Destinos()[1],shape = 'circle')
                        self.dot.node(Nombre2,label=iter2.Get_Destinos()[2],shape = 'circle')
                        self.dot.edge(OrigenAnterior,Nombre1)
                        self.dot.edge(OrigenAnterior,Nombre3)
                        self.dot.edge(OrigenAnterior,Nombre2)
                        OrigenAnterior = Nombre3
                        
                        pass
                self.dot.render(format='png',directory='C:/Users/Krpi/Documents/Python/Lenguajes Formales Lab Diciembre 2022 ESV/Proyecto-2-_LFP_202000869/Documentos')

                