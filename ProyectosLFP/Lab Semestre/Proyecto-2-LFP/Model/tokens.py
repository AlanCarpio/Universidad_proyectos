from fileinput import filename
class Tokens():
    def __init__(self,_token,_fila) -> None:
        self.__token = _token
        self.fila = _fila
        ##columna = _columna
        pass
    def print_token(self):
        print("token | {}           | fila {}".format(self.__token,self.fila))
    def Get_token(self):
        return self.__token