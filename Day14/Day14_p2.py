blocked = set()
abyss = 0

for line in open("Day14\\Day14.txt"):
    lines = [list(map(int , p.split(","))) for p in line.strip().split(" -> ")]

    for (x1, y1), (x2, y2) in zip(lines, lines[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                blocked.add(x + y * 1j)

                abyss = max(abyss, y+1)

total_sand = 0

floor = abyss + 2

while 500 not in blocked:
    sand_coordinates = 500

    while True:

        if sand_coordinates.imag >= abyss:
            break

        if sand_coordinates + 1j not in blocked:
            sand_coordinates += 1j
            continue
        
        if sand_coordinates -1 +1j not in blocked:
            sand_coordinates += -1 + 1j
            continue

        if sand_coordinates + 1 + 1j not in blocked:
            sand_coordinates += 1 + 1j
            continue
        break

    blocked.add(sand_coordinates)
    total_sand += 1
    print(total_sand)
        
        
print(total_sand)
