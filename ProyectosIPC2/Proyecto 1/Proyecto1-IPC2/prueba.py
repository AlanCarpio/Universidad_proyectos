
import re


lista = [0,1,2,3,4,5,6,7,8]

def hola():
    bolan = False
    for i in range(len(lista)):
        if i!=0:
            if i == 1 and lista[0] == lista[i]:
                return print("mortal n:{}".format(i))
    bolan = True        
    if bolan == True:
        for i in range(len(lista)):
            for j in range(i,len(lista)):
                if i!=j:
                    if  lista[i] == lista[j] and i==j-1:
                        return print("mortal n={} , n1 = {}".format(i,1))
                    elif lista[i] == lista[j]:
                        return print("grave")
    return print("leve")
HTML = "<HTML>\nHola como esta\n </HTML>"
print(HTML)

