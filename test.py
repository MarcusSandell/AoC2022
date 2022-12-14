from collections import defaultdict
from pprint import pprint
path = "C:\\Users\\Marcu\\Desktop\\Code\\Advent of Code 2022\\Day14\\Day14.txt"


grid = set()
sands = set()
abyss = 0
grid_size_max = (0, 0) # x, -y
grid_size_min = (99999, 0)

for i in open(path):
    s = [list(map(int, p.split(","))) for p in i.strip().split(" -> ")]

    for (x1, y1), (x2, y2) in zip(s, s[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):

                grid.add(x + y * 1j)

                grid_size_max = (max(grid_size_max[0], x), max(grid_size_max[1], y))
                grid_size_min = (min(grid_size_min[0], x), min(grid_size_min[1], y))

        
       # print((x1, y1) + (x2, y2))

def printGrid():
    for y in range(grid_size_min[1],grid_size_max[1]+1):

        temp = ""
        for x in range(grid_size_min[0],grid_size_max[0]+1):
            #print((x, y))
            temp += "#" if (x + y * 1j) in grid else "o" if (x + y * 1j) in sands else "."

        print(temp)

#printGrid()
total_sand = 0

while True:
    sand = 500

    while True:

        if sand.imag >= grid_size_max[1]:
            print(printGrid())
            print(total_sand)
            exit(0)

        if sand + 1j not in grid.union(sands):
            sand += 1j
            continue

        if sand - 1 + 1j not in grid.union(sands):
            sand += -1 + 1j
            continue

        if sand + 1 + 1j not in grid.union(sands):
            sand += 1 + 1j
            continue

        break

    sands.add(sand)
    total_sand += 1


    

        


