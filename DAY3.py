import re  #importuje REGULAR EXPRESION
file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY3\\database3.txt") #wczytuje plik
tekst = file.readlines()
data = []
wynik =0

for linia in tekst:            #wczytuje plik
    data.append(linia)

example = 'mul\([0-9]+,[0-9]+\)'  #tworze wzór szukanego stringa/ wszystko tu --> https://www.w3schools.com/python/python_regex.asp
example2 = '[0-9]+'


for n in range(len(data)):                #szukam w tekscie mul() 
    dane = re.findall(example, data[n])
    for i in range(len(dane)):
        dane2= re.findall(example2,dane[i])   #korzystam z regexa, żeby uzyskać liczby i wykonuje funkcje mul()
        wynik = wynik + (int(dane2[0])*int(dane2[1]))



print(wynik)





