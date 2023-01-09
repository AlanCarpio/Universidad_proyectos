
from Controller.Analizador_lexico import scanner
from Controller.analizador_sintactico import parser
from View.windown_main import window_main
from Controller.create_html_css import create
from Controller.open_file import abrir_archivo

if __name__ == "__main__":
    window_main.mainloop()
    """
    analisis = scanner()
    asd = abrir_archivo()
    analisis.analisis_lexico(asd[0])
    data = analisis.Get_data_tokens().data
    analisis2 = parser(analisis.Get_data_HTML(),analisis.Get_data_tokens())
    analisis2.analisis_sintactico()
    
    #asd = analisis.Get_data_tokens()
    asd = analisis2.Get_tokens_sintactico()
    html = create(analisis.Get_data_HTML(),asd)
    html.create_html()
    html.create_css()
    #asd.print_data()
    #print(data)
    #asd.print_navega()
    #asd.print_navega2()
    #asd.print_navega3()
    """

    
    