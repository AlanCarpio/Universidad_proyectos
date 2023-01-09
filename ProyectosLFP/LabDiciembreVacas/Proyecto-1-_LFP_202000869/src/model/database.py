class database:
    def __init__(self) -> None:
        self.__data = []
        pass
    def insert_element(self,data):
        self.__data.append(data)
    def clear_list(self):
        self.__data = []
    def Get_data(self):
        return self.__data