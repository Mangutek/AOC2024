import re #importuje REGULAR EXPRESION
file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY3\\database3.txt") #wczytuje plik
tekst = file.readlines()
data = []
wynik =0
enable = 1

for linia in tekst:  #wczytuje dane do tabeli
    data.append(linia)

example = "mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"  #dodałem do wzoru do() i don't() (w tabeli będą się znajdować pomiędzy mul())
example2 = '[0-9]+'



for n in range(len(data)):  #w zależności od do() i don't() zmieniam wartość enable i albo wykonuje mul() albo nie
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





