file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY4\\database4.txt")  #wczytuje plik
tekst = file.readlines()
dane = []
for linia in tekst:            #wczytuje dane do tabeli
    dane.append(linia.strip())

wynik = 0

for y in range(len(dane)):      #po wierszach nazwanych y            
    for x in range(len(dane[0])): #po znakach nazwynych x (kolumnach)
            if dane[y][x]=='A':  #sprawdzam kiedy ==A
                if y-1>=0:   #czy istnieje wiersz nad
                    
                    if y+1<len(dane[0]): #czy instnieje wiercz pod
                        
                        if x-1>=0:  #czy istnieje wiersz na lewa
                            
                            if x+1<len(dane[0]): #czy istnieje wiersz na prawo
                               
                                
                                if dane[y-1][x-1]+dane[y][x]+dane[y+1][x+1] == 'MAS' or dane[y-1][x-1]+dane[y][x]+dane[y+1][x+1] == 'SAM':  #spawdzam czy na ukos
                                    
                                    if dane[y+1][x-1]+dane[y][x]+dane[y-1][x+1] == 'MAS' or dane[y+1][x-1]+dane[y][x]+dane[y-1][x+1] == 'SAM': #sprawdzam czy na ukos z drugiej strony
                                        wynik = wynik+1   #jeżeli spełnia wszytkie te warunki dodaje do wyniku
                                       
                
print(wynik)
