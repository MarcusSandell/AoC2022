path = "Day15\\Day15.txt"

sensors = set()
beacons = set()


M = 4000000
# pattern = re.compile(r"-?\d+")

lines = open(path).read().strip().replace(" x=",",").replace(" y=","").replace(":",",").split("\n")

sensors = list([((x.split(",")[1]), (x.split(",")[2])) for x in lines])
sensors = list((int(x), int(y)) for x, y in sensors) # ????

beacons = list([((x.split(",")[4]), (x.split(",")[5])) for x in lines])
beacons = list((int(x), int(y)) for x, y in beacons) # ????


for Y in range(M):

    intervals = []

    for i in range(len(sensors)):
        # sx, sy, bx, by = map(int, pattern.findall(line))
        sx, sy, bx, by = (sensors[i] + beacons[i])
        

        manhattan_distance = abs(sx - bx) + abs(sy - by)
        offset = manhattan_distance - abs(sy - Y)

        if offset < 0:
            continue

        lx = sx - offset
        hx = sx + offset

        intervals.append((lx, hx)) # Points that cannot exist


    intervals.sort()

    q = [] # Non overlapping intervals

    for lo, hi in intervals:
        if not q:
            q.append([lo, hi])
            continue
        qlo, qhi = q[-1]

        if lo > qhi + 1: # If the intevals are touching
            q.append([lo, hi])

        q[-1][1] = max(qhi, hi)

    x = 0
    for lo, hi in q:
        if x < lo:
            print(x * 4000000 + Y)
            exit(0)
        
        x = max(x, hi + 1)
        if x > M:
            break