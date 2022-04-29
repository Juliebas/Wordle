import numpy as np
from unidecode import unidecode
import random as r

def le(s):
    '''
    Recebe uma string com o nome do arquivo e retorna uma lista lida
    '''
    lista = []
    with open(s, encoding='utf8') as f:
        for line in f:
            lista.append(line)
    return lista

def retira_n(ls):
    '''
    Retira o \n das palavras
    '''
    for i in range(len(ls)):
        ls[i] = ls[i].replace("\n", "")
    return(ls)

def retira_lixo(ls):
    lista_nova = []
    lista_nova1 = []
    for i in range(len(ls)): #Tira acentos
        ls[i] = unidecode(ls[i])
    for i in range(len(ls)):
        if ls[i][0].isupper() == False: #Tira os nomes próprios
            lista_nova.append(ls[i])
    for i in range(len(lista_nova)): #Tira palavras com mais de cinco letra
        if len(lista_nova[i]) == 5:
           lista_nova1.append(lista_nova[i])
    return lista_nova1


def banco_de_palavras():
    f = retira_n(le("Programas.txt"))
    return retira_lixo(f)

class Termo():

    def __init__ (self):
        bp = banco_de_palavras()
        self.pal = r.choice(bp)
        self.acertos = np.zeros((6,5))
        self.tent = 0
    
    def coloca_palavra(self, pal):
        d = self.pal
        for i in range(5):
            if pal[i] in d:
                self.acertos[self.tent,i] += 1
                d.replace(pal[i], "", 1)
            if pal[i] == self.pal[i]:
                self.acertos[self.tent,i] += 1
        print(self.acertos)
        self.tent += 1
        if self.acertos[self.tent, ] == np.array([2,2,2,2,2]):
            return "Você é foda"
        if self.tent < 6:
            self.coloca_palavra(input("Nova palavra: "))

v = Termo()
v.coloca_palavra(input("Nova palavra??: "))
                

