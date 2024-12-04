file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY4\\database4.txt")
tekst = file.readlines()
dane = []
for linia in tekst:
    dane.append(linia.strip())

print(dane)
wynik = 0

for y in range(len(dane)):
    for x in range(len(dane[0])):
            if dane[y][x]=='X':
                if x+3 < len(dane[0]):
                    if dane[y][x] + dane[y][x+1] + dane[y][x+2] + dane[y][x+3] == 'XMAS':
                       wynik = wynik +1
                    if y+3 < len(dane[0]):
                        if dane[y][x] + dane[y+1][x+1] + dane[y+2][x+2] + dane[y+3][x+3] == 'XMAS':
                            wynik = wynik + 1
                    if y-3>=0:
                        if dane[y][x] + dane[y-1][x+1] + dane[y-2][x+2] + dane[y-3][x+3] == 'XMAS':
                            wynik = wynik+1
                        
                if x-3 >= 0:
                    if dane[y][x] == 'X' and dane[y][x-1] == 'M' and dane[y][x-2] == 'A' and dane[y][x-3] == 'S':
                        wynik = wynik+1
                    if y-3>=0:
                        if dane[y][x] + dane[y-1][x-1] + dane[y-2][x-2] + dane[y-3][x-3] == 'XMAS':
                            wynik = wynik+1
                    if y+3 < len(dane[0]):
                        if dane[y][x] + dane[y+1][x-1] + dane[y+2][x-2] + dane[y+3][x-3] == 'XMAS':
                            wynik = wynik+2
                if y+3 < len(dane[0]):
                    if dane[x][y] + dane[x][y+1]+dane[x][y+2]+dane[x][y+3] == 'XMAS':
                        wynik = wynik+1
                if y-3>=0:
                    if dane[x][y]+dane[x][y-1]+dane[x][y-2]+dane[x][y-3] == 'XMAS':
                        wynik = wynik+1
                
                       



print(wynik)
