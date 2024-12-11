import functools
from collections import defaultdict
rocks = defaultdict(int)

tekst = open("C:\\Users\\Admin\\Desktop\\AOC\\DAY6\\database11.txt").readlines()
data = []
for line in tekst: 
    el = line.split(' ')
    for elem in el:
        data.append(elem)

for el in data:
    rocks[el] = data.count(el)


for _ in range(75):
    new = defaultdict(int)
    for rock, count in rocks.items():
            if rock == '0':
                new['1'] += count
            elif len(str(rock))%2 == 0:
                new[str(int(rock[:len(str(rock))//2]))] += count
                new[str(int(rock[len(str(rock))//2:]))] += count
            else:
                new[str(int(rock)*2024)] += count
    rocks = new


    print(sum(rocks.values()))






