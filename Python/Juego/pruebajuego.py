# -*- coding: utf-8 -*-
"""pruebajuego.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16NovrVwDn_zAXQ9pDP8b75ekdULxeh_n
"""

import random
from pprint import pprint
import os
def get_file():

    with open('archivos/words.txt','r',encoding = 'utf-8') as f :
        data = f.readlines()
        data = random.choice(data)
        data = list(data)
        data.pop(len(data)-1)
        return data 

def incognita(data):
    incognita =['*' for i in data]
    return incognita

def cycle(incognita,data):
    print(incognita)
    
if __name__ == '__main__':

    data = get_file()
    incognita = incognita(data)