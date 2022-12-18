
path = "Day18//Day18.txt"

cubes = set()

for line in open(path):
    x, y, z = map(int, line.split(","))
    cubes.add((x, y, z))


ans = 0

for x, y, z in cubes:

    occupied = 0
    print(x,y,z)
    for ox, oy, oz in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]:
        
        if (x+ox, y+oy, z+oz) in cubes:
            occupied += 1

    ans += 6 - occupied

print(ans)
