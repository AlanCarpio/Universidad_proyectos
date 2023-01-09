class css():
    def __init__(self,_ID,_propiedad,_valor) -> None:
        self.ID = _ID
        self.propiedad = _propiedad
        self.valor = _valor
        pass
    def imprimir_css(self):
        print("ID|{} |Pro{} |Valor{}".format(self.ID,self.propiedad,self.valor))
    