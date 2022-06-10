import pygame as pg
import numpy as np
from unidecode import unidecode
import random as r
import requests

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
    f = retira_n(le("Banco_de_nomes.txt"))
    return retira_lixo(f)

class Termo():

    def __init__ (self):
        bp = banco_de_palavras()
        self.pal = r.choice(bp)
        self.acertos = np.zeros((6,5))
        self.tent = 0
        self.ganhou = False
    
    def coloca_palavra(self, pal):

        d = self.pal
        for i in range(5):
            if pal[i] == self.pal[i]:
                self.acertos[self.tent,i] += 2
                d = d.replace(pal[i], '', 1)
        for i in range(5):
            if pal[i] in d:
                self.acertos[self.tent,i] += 1
                d = d.replace(pal[i], '', 1)
            

        if (self.acertos[self.tent, ] ==  np.array([2,2,2,2,2])).all():
            self.ganhou = True
        self.tent += 1

class Interface():

    def __init__(self):
        pg.init() 
        v = Termo()
        self.tela = pg.display.set_mode((800,600)) #cria janela
        self.rodando = True
        
        #Icones
        pg.display.set_caption("Termo")
        icone = pg.image.load('Imagens/t.png')
        pg.display.set_icon(icone)

        #Relógios e caixinhas de texto
        clock = pg.time.Clock() 
        caixa = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] #Cria caixinhas
        termo = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']] #Cria caixinhas de texto
        texto = 6*[5*[0]]
        fonte = pg.font.Font(None, 50) #Fonte

        for i in range (6): # Repetição para criar as caixinhas
            for j in range (5):
                caixa[i][j] = pg.image.load("Imagens/Caixa_Letra.png")
                caixa[i][j] = pg.transform.scale(caixa[i][j], (80, 80))

        x = 0
        while self.rodando: #loop do jogo
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.rodando = False
                    print(v.pal)
                if event.type == pg.KEYDOWN:
                    if v.ganhou:
                        pass
                    elif event.key == pg.K_BACKSPACE and x >= 1:
                        x-=1
                        termo[v.tent][x] = ''
                    elif x < 5 and event.unicode != "\x08":
                        termo[v.tent][x] = event.unicode.upper()
                        x += 1
                    elif event.key == pg.K_KP_ENTER or event.key == pg.K_RETURN:
                        string = ''.join(termo[v.tent]).replace(" ", '')
                        v.coloca_palavra(string.lower())
                        for i in range(5):
                            if v.acertos[v.tent-1,i] == 1.0:
                                caixa[v.tent-1][i] = pg.image.load("Imagens/Caixa_Letra1.png")
                                caixa[v.tent-1][i] = pg.transform.scale(caixa[v.tent-1][i], (80, 80))
                            if v.acertos[v.tent-1,i] == 2.0:
                                caixa[v.tent-1][i] = pg.image.load("Imagens/Caixa_Letra2.png")
                                caixa[v.tent-1][i] = pg.transform.scale(caixa[v.tent-1][i], (80, 80))

                        x = 0
                    else: pass

                        
            self.tela.fill((128,128,128))
            cont_y = 55
            for i in range (6):
                cont_x = 196
                for j in range (5):
                    texto[i][j] = fonte.render(termo[i][j], True, (255,255,255))
                    self.tela.blit(caixa[i][j], (cont_x, cont_y))
                    self.tela.blit(texto[i][j], (cont_x+28, cont_y+25))
                    cont_x += 82
                cont_y += 82
            clock.tick(60)
            pg.display.update()

def le_site():

    myfile = requests.get('https://www.linguateca.pt/acesso/tokens/formas.totalbr.txt', stream=True).raw

    print(myfile)

def main():
    Interface()

if __name__ == "__main__":
    main()
