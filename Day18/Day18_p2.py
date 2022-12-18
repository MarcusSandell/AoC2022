
path = "Day18//Day18.txt"

cubes = set()
outside = set()

for line in open(path):
    x, y, z = map(int, line.split(","))
    cubes.add((x, y, z))

def floodFill():

    min_x = min_y = min_z = float("inf")
    max_x = max_y = max_z = -float("inf")

    for cube in cubes:

        x, y, z = cube
        
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        min_z = min(min_z, z)

        max_x = max(max_x, x)
        max_y = max(max_y, y)
        max_z = max(max_z, z)

    flood_heap = [(0, 0, 0)]

    min_x -= 1
    min_y -= 1
    min_z -= 1

    max_x += 1
    max_y += 1
    max_z += 1

    print(min_x, max_x, min_y, max_y, min_z, max_z)

    while flood_heap:

        x, y, z = flood_heap.pop()

        if (x, y, z) in outside or not (min_x <= x <= max_x and min_y <= y <= max_y and min_z <= z <= max_z ):
            continue

        for ox, oy, oz in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]:
        
            if (x+ox, y+oy, z+oz) not in cubes and (min_x <= x+ox <= max_x and min_y <= y+oy <= max_y and min_z <= z+oz <= max_z):
                flood_heap.append((x+ox, y+oy, z+oz))

        outside.add((x, y, z))


floodFill()
ans = 0

for x, y, z in cubes:

    occupied = 0
    for ox, oy, oz in [(1,0,0),(0,1,0),(0,0,1),(-1,0,0),(0,-1,0),(0,0,-1)]:
        
        if (x+ox, y+oy, z+oz) in outside:
            ans += 1

print(f"ANSWER: {(ans)}")
