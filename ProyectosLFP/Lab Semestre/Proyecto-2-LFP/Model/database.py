
class data():
    def __init__(self) -> None:
        self.data = []
        pass
    #=========== Funciones insertar datos =============
    def insertar_dato(self,dato):
        self.data.append(dato)
    def print_navega(self):
        for iter in self.data:
            iter.print_token()
    def print_navega2(self):
        for iter in self.data:
            iter.print_HTML()
    def empty_Elements(self):
        self.data = []
    def print_navega3(self):
        for iter in self.data:
            iter.imprimir_css()
