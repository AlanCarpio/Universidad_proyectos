from tkinter import*
from tkinter.ttk import Treeview

class Tables():
    def __init__(self,analizador_lexico,analizador_sintac) -> None:
        self.scanner = analizador_lexico
        self.parser = analizador_sintac
        self.subventana = Toplevel()
        self.subventana.geometry("550x300")
        self.subventana.title("Tokens")
        self.frame = Frame(self.subventana,width=550,height=300)
        self.table = Treeview(self.frame,columns=("col1","col2","col3"))
        self.var = IntVar()
        self.radio_tokens = Radiobutton(self.frame,text="Tokens",variable=self.var,value=1,command=self.tabla_radio_tokens)
        self.radio_tokens_malos_lexicos = Radiobutton(self.frame,text="Tokens de errores lexicos",variable=self.var,value=3,command=self.tabla_radio_tokens_malos_lexicos)
        self.radio_tokens_malos_sintac = Radiobutton(self.frame,text="Tokens de errores sintacticos",variable=self.var,value=4,command=self.tabla_radio_tokens_malos_sintac)
        self.radio_tokens_comentarios = Radiobutton(self.frame,text="Tokens de comentarios",variable=self.var,value=5,command=self.tabla_radio_tokens_comentarios)
    def placement_and_options(self):
        self.frame.place(x=0,y=0)
        self.table.place(x=20,y=20)
        self.table.column("#0",width=80)
        self.table.column("col1",width=80,anchor=CENTER)
        self.table.column("col2",width=80,anchor=CENTER)
        self.table.column("col3",width=80,anchor=CENTER)
        self.table.heading("#0",text="Correlativo", anchor=CENTER)
        self.table.heading("col1",text="Token", anchor=CENTER)
        self.table.heading("col2",text="Fila", anchor=CENTER)
        self.table.heading("col3",text="Tipo", anchor=CENTER)
        self.radio_tokens.place(x=370,y=20)
        self.radio_tokens_malos_lexicos.place(x=370,y=70)
        self.radio_tokens_malos_sintac.place(x=370,y=120)
        self.radio_tokens_comentarios.place(x=370,y=170)
        
        pass
    def tabla_radio_tokens(self):
        for i in self.table.get_children():
            self.table.delete(i)
        data1 = self.scanner.Get_data_tokens().data
        cont = 1
        for iter in data1:
            self.table.insert("",END,text=cont,values=(iter.Get_token(),iter.fila,"Lexico"))
            cont += 1
            pass
    def tabla_radio_tokens_malos_lexicos(self):
        for i in self.table.get_children():
            self.table.delete(i)
        data1 = self.scanner.Get_data_tokens_malos().data
        cont = 1
        for iter in data1:
            self.table.insert("",END,text=cont,values=(iter.Get_token(),iter.fila,"Lexico"))
            cont += 1
            pass
    def tabla_radio_tokens_malos_sintac(self):
        for i in self.table.get_children():
            self.table.delete(i)
        data1 = self.parser.Get_tokens_malos_sintactico().data
        cont = 1
        for iter in data1:
            self.table.insert("",END,text=cont,values=(iter.Get_token(),iter.fila,"Sintactico"))
            cont += 1
            pass
    def tabla_radio_tokens_comentarios(self):
        for i in self.table.get_children():
            self.table.delete(i)
        data1 = self.scanner.Get_data_tokens_comentarios().data
        cont = 1
        for iter in data1:
            self.table.insert("",END,text=cont,values=(iter.Get_token(),iter.fila,"comentarios"))
            cont += 1
            pass
        pass
    