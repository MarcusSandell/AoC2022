with open("Day09\\Day9.txt") as f:
    lines = f.read().strip().split("\n")

#headPos = [0,0] # X, Y
#tailPos = [0,0] # X, Y
visited_Pos = set()
knots = [[0,0] for x in range(10)]

direction = {
    "U":1,
    "D":-1,
    "R":1,
    "L":-1
}

def Touching(pos1, pos2):
    return (abs(pos1[0]-pos2[0]) <= 1) and (abs(pos1[1] - pos2[1]) <= 1)

def moveKnot(currentKnot, knotInfront):
    currentKnot[0] += 0 if knotInfront[0] == currentKnot[0] else int((knotInfront[0] - currentKnot[0]) / abs(knotInfront[0] - currentKnot[0]))
    currentKnot[1] += 0 if knotInfront[1] == currentKnot[1] else int((knotInfront[1] - currentKnot[1]) / abs(knotInfront[1] - currentKnot[1]))

    return [currentKnot[0], currentKnot[1]]


for line in range(len(lines)):
    op = lines[line].split(" ")
    for j in range(int(op[1])):

        for knot in range(len(knots)):

            if knot == 0:

                if op[0] == "U" or op[0] == "D":
                    knots[0][1] += direction[op[0]]
                else:
                    knots[0][0] += direction[op[0]]
            
            else:

                if not Touching(knots[knot], knots[knot-1]):
                    knots[knot] = moveKnot(knots[knot], knots[knot-1])

            if knot == len(knots)-1:
                visited_Pos.add((knots[knot][0], knots[knot][1]))

print(len(visited_Pos))