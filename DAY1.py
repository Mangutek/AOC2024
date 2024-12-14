#wczytuje plik
text = open("C:\\Users\\Admin\\Desktop\\AOC\\DAY1\\database1.txt").readlines()
data = []
left = []
right = []
score = 0

for line in text:        #wprowadzam dane do tabeli
    roz1 = line.split('   ')
    for el in roz1:
        el2 = el.strip()
        data.append(el2)

i = 2
for el in txt:        #dziele na dwie tabele
    if i%2 == 0:
        left.append(el)
    else:
        right.append(el)
    i = i+1

PRAWA.sort() #sortuje
LEWA.sort()

for i in range(len(left)):  #sumuje róznice pomiędzy nimi
    p = 0
    p = int(left[i]) - int(right[i])
    p2 = abs(p)
    score = score + p2
print(score)
