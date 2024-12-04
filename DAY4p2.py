file = open("C:\\Users\\Franek\\Desktop\\AOC\\DAY4\\database4.txt")
tekst = file.readlines()
dane = []
for linia in tekst:
    dane.append(linia.strip())

print(dane)
wynik = 0

for x in range(len(dane)):
    for y in range(len(dane[0])):
            if dane[x][y]=='A':
                if x-1>=0:
                    
                    if x+1<len(dane[0]):
                        
                        if y-1>=0:
                            
                            if y+1<len(dane[0]):
                               
                                
                                if dane[x-1][y-1]+dane[x][y]+dane[x+1][y+1] == 'MAS' or dane[x-1][y-1]+dane[x][y]+dane[x+1][y+1] == 'SAM':
                                    
                                    if dane[x+1][y-1]+dane[x][y]+dane[x-1][y+1] == 'MAS' or dane[x+1][y-1]+dane[x][y]+dane[x-1][y+1] == 'SAM':
                                        wynik = wynik+1
                                       
                
                
                       



print(wynik)
