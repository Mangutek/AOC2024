file = open("C:\\Users\\Admin\\Desktop\\AOC\\DAY2\\database2.txt") #wczytuje plik
tekst = file.readlines()
data = []
odp = 0

for line in tekst: #wczytuje dane do tabeli
    data.append(line.strip().split())

def czysorted(list):            #funkcja sprawdza, czy jest posortowane
    wynik = 0
    wynik2 = 0
    for i in range(len(list)-1):
        if int(list[i])>int(list[i+1]):
            wynik = wynik+1
        elif int(list[i])<int(list[i+1]):

            wynik2 = wynik2 + 1
    if wynik == len(list)-1 or wynik2 == len(list)-1:
        return 1
    else:
        return 0


            
for el in data:                
    if czysorted(el) == 1:    #sprawdzam czy jest posortowane
        if all(abs(int(el[i])-int(el[i+1])) <=3 for i in range(len(el)-1)):    #sprawdzam czy wszystkie róznice są mniejsze od 3 (takie same wartości wykulczam w czysorted())
            print("tak")
            odp = odp + 1
    else:
        print('nie')


print(odp)

