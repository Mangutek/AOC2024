import re
file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY3\\database3.txt")
tekst = file.readlines()
data = []
wynik =0

for linia in tekst:
    data.append(linia)

example = 'mul\([0-9]+,[0-9]+\)'
example2 = '[0-9]+'


for n in range(len(data)):
    dane = re.findall(example, data[n])
    for i in range(len(dane)):
        dane2= re.findall(example2,dane[i])
        wynik = wynik + (int(dane2[0])*int(dane2[1]))




print(wynik)





