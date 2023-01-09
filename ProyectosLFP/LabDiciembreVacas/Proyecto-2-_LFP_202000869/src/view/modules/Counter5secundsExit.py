from tkinter import *
from time import sleep
def Exit(Master_win,Master_frame):
    for iter in Master_frame .winfo_children():
            iter.destroy()
    LabelNumber = Label(Master_frame,text=5,font='calibri 32 bold')
    LabelNumber.pack()
    LabelNumber.place(x=380,y=120)
  
    cont = 6
    while cont > 0:
        cont -= 1
        LabelNumber.config(text=cont)
        sleep(1)
        Master_win.update()
    sleep(1)
    Master_win.destroy()
pass

