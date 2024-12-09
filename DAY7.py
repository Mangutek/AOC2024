file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY7\\database7.txt") #wczytuje plik
tekst = file.readlines()
dane= []
count = 0
kombinacje = []
wynik = 0



for line in tekst:        #wprowadzam dane do tabeli
    roz1 = line.strip().split(':')
    for el in roz1:
        el2 = el.split(' ')
        dane.append(el2)


for y in range(len(dane)):
    for x in range(len(dane[y])-1):
        if dane[y][x].isdigit() == 0:
            dane[y].pop(x)

def generuj_kombinacje(liczba_znakow, aktualna_kombinacja=""):
    if len(aktualna_kombinacja) == liczba_znakow:
        kombinacje.append(aktualna_kombinacja)
        return
    generuj_kombinacje(liczba_znakow, aktualna_kombinacja + '*')
    generuj_kombinacje(liczba_znakow, aktualna_kombinacja + '+')


def dodaj(el1, el2):
    return int(el1) + int(el2)

def mul(el1, el2):
    return int(el1) * int(el2)

for n in range(1, len(dane), 2):
    kombinacje.clear()
    generuj_kombinacje(len(dane[n])-1)
    for i in range(len(kombinacje)):
        count = int(dane[n][0])
        for z in range(len(kombinacje[i])):
            if kombinacje[i][z][0] == '*':
                count = count * int(dane[n][z+1])
            elif kombinacje[i][z][0] == '+':
                count = count + int(dane[n][z+1])
        if count == int(dane[n-1][0]):
            wynik = wynik+count
            break

        


print(wynik)          




        
        


