tekst = open("C:\\Users\\Admin\\Desktop\\AOC\\DAY6\\database10.txt").readlines()
mapa = []
count = 0
czy = []
for line in tekst: mapa.append(line.strip())

zera = []
odwiedzone = []
def czyjestw(elem, tablica):
    for el in tablica:
        if el == elem:
            return 1
    return 0
for y in range(len(mapa)):
    for x in range(len(mapa[y])):
        if mapa[y][x] == '0':
            zera.append((y, x))
print(zera)

def szukaj(odwiedzone, count, wartosc, yp, xp):
    if wartosc == 9 and czyjestw((yp, xp), odwiedzone) == 0:
        odwiedzone.append((yp, xp))
        count = count + 1
    try:
        if int(mapa[yp-1][xp]) == wartosc + 1 and yp!=0:
            szukaj(odwiedzone, count, wartosc+1, yp-1, xp)
    except:
        pass
    try:
        if int(mapa[yp][xp-1]) == wartosc + 1 and xp!=0:
            szukaj(odwiedzone, count, wartosc+1, yp, xp-1)
    except:
        pass
    try:
        if int(mapa[yp][xp+1]) == wartosc + 1:
            szukaj(odwiedzone, count, wartosc+1, yp, xp+1)
    except:
        pass
    try:
        if int(mapa[yp+1][xp]) == wartosc + 1:
            szukaj(odwiedzone, count, wartosc+1, yp+1, xp)
    except:
        pass
    czy.append(count)



for el in zera:
    odwiedzone.clear()
    szukaj(odwiedzone, 0, 0, el[0], el[1])
    print(czy.count(1))
