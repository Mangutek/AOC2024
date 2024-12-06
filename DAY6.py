file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY6\\database6.txt") #wczytuje plik
tekst = file.readlines()
mapa=[]
odwiedzone = []
kierunek = 0
for line in tekst:
    mapa.append(line.strip())

def find():
    for y in range(len(mapa)-1):
        for x in range(len(mapa[y])):
            if mapa[y][x] == "^":
                return [y, x]

straznik = find()
y = straznik[0]
x = straznik[1]
while y>=0 and y< len(mapa)-1 and x>=0 and x<len(mapa[0])-1:
    if kierunek == 0:
        if mapa[y-1][x] == '#':
            kierunek = 1
        else:
            y = y-1
            odwiedzone.append((y,x))
    elif kierunek == 1:
        if mapa[y][x+1] == '#':
            kierunek = 2
        else:
            x = x+1
            odwiedzone.append((y,x))
    elif kierunek == 2:
        if mapa[y+1][x] == '#':
            kierunek = 3
        else:
            y = y+1
            odwiedzone.append((y,x))
    elif kierunek == 3:
        if mapa[y][x-1] == '#':
            kierunek = 0
        else:
            x = x-1
            odwiedzone.append((y,x))



odwiedzone = list(set(odwiedzone))
print(len(odwiedzone))
     
            


