file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY4\\database4.txt") #wczytuje plik
tekst = file.readlines()
dane = []
for linia in tekst:                    #dodaje dane do tabeli
    dane.append(linia.strip())

wynik = 0            #ustalam zmienna
ktoryx = 1

for y in range(len(dane)):      #ide po wierszach 
    for x in range(len(dane[0])): #po znakach w każdym wierszu (kolumny)
        if dane[y][x]=='X':                #jeżeli x to kontynuje
                print(ktoryx)
                ktoryx = ktoryx+1
                if x+3 < len(dane[0]):  #sprawdzenia, żeby nie wyjśc poza zakres tabeli
                    if dane[y][x] + dane[y][x+1] + dane[y][x+2] + dane[y][x+3] == 'XMAS': #linijka normalnie
                       wynik = wynik +1
                       print('linijka normalnie')
                    if y+3 < len(dane[0]):
                        if dane[y][x] + dane[y+1][x+1] + dane[y+2][x+2] + dane[y+3][x+3] == 'XMAS':   #diagonalnie  prawa dół
                            wynik = wynik + 1
                            print('diagonalnie  prawa dół')
                    if y-3>=0:
                        if dane[y][x] + dane[y-1][x+1] + dane[y-2][x+2] + dane[y-3][x+3] == 'XMAS':  #diagonalnie prawa góra
                            wynik = wynik+1
                            print('diagonalnie prawa góra')
                        
                if x-3 >= 0:
                    if dane[y][x]+dane[y][x-1]+dane[y][x-2]+dane[y][x-3] == 'XMAS':                     #linijka odwrotnie
                        wynik = wynik+1
                        print('linijka odwrotnie')
                    if y-3>=0:
                        if dane[y][x] + dane[y-1][x-1] + dane[y-2][x-2] + dane[y-3][x-3] == 'XMAS':   #diagonalnie lewa góra
                            wynik = wynik+1
                            print('diagonalnie lewa góra')
                    if y+3 < len(dane[0]):
                        if dane[y][x] + dane[y+1][x-1] + dane[y+2][x-2] + dane[y+3][x-3] == 'XMAS':   #diagonalnie lewa dół
                            wynik = wynik+1
                            print('diagonalnie lewa dół')
                if y+3 < len(dane[0]):
                    
                    if dane[y][x] + dane[y+1][x]+dane[y+2][x]+dane[y+3][x] == 'XMAS': #kolumna dół
                        wynik = wynik+1
                        print('kolumna dół')
                if y-3>=0:
                    if dane[y][x]+dane[y-1][x]+dane[y-2][x]+dane[y-3][x] == 'XMAS': #kolumna góra
                        wynik = wynik+1
                        print('kolumna góra')
                
                
print(wynik)
