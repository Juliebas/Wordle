#CONSTANTES
N = 5
G = 1
NE = 1

from copy import deepcopy
import random as r

class CatBox:
    
    def __init__(self, N, G, NE):
        self.length = N
        self.ncats = G
        self.nchoices = NE

    def gato_ini(self):
        lista = [0]*self.length
        lista[0] = 1
        r.shuffle(lista)
        for i in range (self.length):
            if lista[i] == 1:
                g = deepcopy(i)
        self.boxes = lista
        self.cat = g

    def escolhe(self, i):
        if self.boxes[i] == 1:
            return True
        else: 
            return False

    def gato_passa (self):
        random = r.randrange(2)
        if self.cat == 0:
            self.boxes[self.cat+1] = 1
            self.boxes[self.cat] = 0
            self.cat += 1
        elif self.cat == self.length-1:
            self.boxes[self.cat-1] = 1
            self.boxes[self.cat] = 0
            self.cat -= 1
        elif random == 0:
            self.boxes[self.cat-1] = 1
            self.boxes[self.cat] = 0
            self.cat -= 1
        else:
            self.boxes[self.cat+1] = 1
            self.boxes[self.cat] = 0
            self.cat += 1
        
    def jogo (self, ind=-1):
        e = False
        contador = 0
        while e == False:
            if ind == -1:
                lugar = input("Escolha uma caixa: ")
            else:
                lugar = ind
            e = self.escolhe(int(lugar))
            if e == False:
                self.gato_passa()
                contador += 1
            else:
                return contador


caixa = CatBox(N, G, NE)