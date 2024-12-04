file = open("C:\\Users\\Admin\\Desktop\\AOC\\DAY1\\database1.txt") #wczytuje plik
tekst = file.readlines()
txt = []
LEWA = []
PRAWA = []
wynik = 0

for line in tekst:        #wprowadzam dane do tabeli
    roz1 = line.split('   ')
    for el in roz1:
        el2 = el.strip()
        txt.append(el2)

i = 2
for el in txt:        #dziele na dwie tabele
    if i%2 == 0:
        LEWA.append(el)
    else:
        PRAWA.append(el)
    i = i+1

PRAWA.sort() #sortuje
LEWA.sort()

for i in range(len(LEWA)):  #sumuje róznice pomiędzy nimi
    p = 0
    p = int(LEWA[i]) - int(PRAWA[i])
    p2 = abs(p)
    wynik = wynik + p2
print(wynik)
