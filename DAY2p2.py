file = open("C:\\Users\\Admin\\Desktop\\AOC\\DAY2\\database2.txt")
tekst = file.readlines()
data = []
odp = 0

for line in tekst:
    data.append(line.strip().split())

def czysorted(list):
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


            
            
            
def czydobry(el):
    if czysorted(el) == 1:
        if all(abs(int(el[i])-int(el[i+1])) <=3 for i in range(len(el)-1)):
            return 1
        else:
            return 0
    else:
        return 0
    
def copymatrix(list1, list2):
    for el in list1:
        list2.append(el)


for el in data:
    if czydobry(el) == 1:
        odp = odp + 1
    else:
        for i in range(0, len(el)):
            el2 = []
            copymatrix(el, el2)
            el2.pop(i)
            if czydobry(el2) == 1:
                odp = odp + 1
                break
            



print(odp)

