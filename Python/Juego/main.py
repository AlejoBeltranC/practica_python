import random
from pprint import pprint
import os
def get_file():
    """
    Lee un archivo con varias palabras.
    Retorna una palabra aleatoria
    """

    with open('archivos/words.txt','r',encoding = 'utf-8') as f :
        data = f.readlines()
        data = list(random.choice(data))
        data.pop(len(data)-1)
        return data
        

def incognita(data):
    """
    Recibe un str.
    Retorna incognita 
    """
    incognita =['*' for i in data]
    return incognita
    

def cycle(incognita,data,live=5,count=0):
    """
    Se ejecuta un Ciclo while 
    """
    
    while live > 0 and incognita != data: 

        letra_u = input('Digite una letra: ')
        os.system('cls')

        for i in data:
            if i == letra_u:
                incognita[count] = letra_u             
            count +=1

        if letra_u not in data: live -= 1

        print(*incognita)
        print('lives: ',str(live))

        count = 0

        if live == 0 : print('GAME OVER')
        if incognita == data: print('GANASTE!!')
    
 
    
if __name__ == '__main__':

    data = get_file()
    incognita = incognita(data)
    cycle(incognita,data)
    