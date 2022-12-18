path = "Day15\\Day15.txt"

sensors = set()
beacons = set()
known = set()
not_in = set()

Y = 2000000
# pattern = re.compile(r"-?\d+")

lines = open(path).read().strip().replace(" x=",",").replace(" y=","").replace(":",",").split("\n")

sensors = list([((x.split(",")[1]), (x.split(",")[2])) for x in lines])
sensors = list((int(x), int(y)) for x, y in sensors) # ????

beacons = list([((x.split(",")[4]), (x.split(",")[5])) for x in lines])
beacons = list((int(x), int(y)) for x, y in beacons) # ????

for i in range(len(sensors)):
    # sx, sy, bx, by = map(int, pattern.findall(line))
    sx, sy, bx, by = (sensors[i] + beacons[i])
     

    manhattan_distance = abs(sx - bx) + abs(sy - by)
    offset = manhattan_distance - abs(sy - Y)

    if offset < 0:
        continue

    for x in range((sx - offset), (sx + offset + 1)):
        not_in.add(x)

    if by == Y:
        known.add(bx)

print(len(not_in - known))