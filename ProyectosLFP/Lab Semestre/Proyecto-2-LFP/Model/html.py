class HTML():
    def __init__(self,_contenedor,_ID) -> None:
        self.contenedor = _contenedor
        self.ID = _ID
        pass
    def print_HTML(self):
        print("contenedor:{}|ID:{}".format(self.contenedor,self.ID))