import re
file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY3\\database3.txt")
tekst = file.readlines()
data = []
wynik =0
enable = 1

for linia in tekst:
    data.append(linia)

example = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
example2 = '[0-9]+'



for n in range(len(data)):
    dane = re.findall(example, data[n])
    print(dane)
    for i in range(len(dane)):
        if dane[i]== "don't()":
            enable = 0
        elif dane[i] == "do()":
            enable = 1
        else:
            if enable == 1:
                dane2= re.findall(example2,dane[i])
                wynik = wynik + (int(dane2[0])*int(dane2[1]))




print(wynik)





