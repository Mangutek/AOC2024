import numpy as np
file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY6\\database6.txt") #wczytuje plik
tekst = file.readlines()

count = 0
mapa = []

def czysiepowtarza(lista, el):
    wynik = 0
    for elem in lista:
        if elem == el:
            wynik = wynik+1
        if wynik == 2:  
            return 1

for line in tekst:
    roz1 = []
    for char in line.strip():
        roz1.append(char)
    mapa.append(roz1)

def find():
    for y in range(len(mapa)-1):
        for x in range(len(mapa[y])):
            if mapa[y][x] == "^":
                return [y, x]

straznik = find()
def ruch(matrix):
    odwiedzone = []
    odwiedzone.clear()
    kierunek = 0
    x = straznik[1]
    y = straznik[0]


    while y>=0 and y< len(matrix)-1 and x>=0 and x<len(matrix[0])-1:
  
            if kierunek == 0:
                if matrix[y-1][x] == '#':
                    kierunek = 1
                else:
                    y = y-1
            elif kierunek == 1:
                if matrix[y][x+1] == '#':
                    kierunek = 2
                else:
                    x = x+1
            elif kierunek == 2:
                if matrix[y+1][x] == '#':
                    kierunek = 3
                else:
                    y = y+1
            elif kierunek == 3:
                if matrix[y][x-1] == '#':
                    kierunek = 0
                else:
                    x = x-1
            odwiedzone.append((y,x,kierunek))
            if czysiepowtarza(odwiedzone, ((y,x,kierunek))) == 1:
                return 1
           
                
def copymatrix(newmatrix, oldmatrix):
    for el in oldmatrix:
        newmatrix.append(el)

mapa2 = []

for y in range(len(mapa)):
    print(y)
    for x in range(len(mapa[0])):
        print(x)
    
        p=0
        if mapa[y][x] == '.':
            p=1

    
        mapa2.clear()
        copymatrix(mapa2 ,mapa)
        if mapa2[y][x] == '^':
            print('nie')
        else:
    
            mapa2[y][x] = '#'
            if ruch(mapa2) == 1:
                count = count +1
                print(count)
            
            if p==1:
                mapa2[y][x] = '.'
            





    
