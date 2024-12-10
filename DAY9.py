tekst = open("C:\\Users\\Admin\\Desktop\\AOC\\DAY6\\database9.txt").readlines()
data = []
linijka = []
for line in tekst: data.append(line)
count  = 0
co = 0

for el in data:
    for char in el:
        if co==0:
            for i in range(int(char)):
                linijka.append(str(count))
            count = count + 1
            co = 1
        elif co == 1:
            for i in range(int(char)):
                linijka.append('.')
            co = 0
def ostatninumer(tablica):
    for i in range(len(tablica)-1, 0, -1):
        if tablica[i].isnumeric() == 1:
            
            return (tablica[i], i)
        
for n in range(len(linijka)):
    
    if linijka[n] =='.':
        x = ostatninumer(linijka)
        linijka.pop(x[1])
        linijka[n] = x[0]
    if n == len(linijka)-1:
        break
while '.' in linijka: linijka.remove('.')
wynik = 0

for y in range(len(linijka)):
    wynik = wynik + (int(linijka[y])*y)
    print(wynik)


print(wynik)