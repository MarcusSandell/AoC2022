#A = Rock (1), B = Paper (2), C = Scissors (3)
#X = Rock, Y = Paper, Z = Scissors
#0 for loss, 3 for draw, 6 for win

with open("Day02\\Day2.txt") as file:
    lines = [i for i in file.read().strip().split("\n")]

#lines = list(map(lambda x: x.replace("\n",""), lines))

#All possible outcomes_pt1
# A vs X = DRAW = (1+3) = 4
# A vs Y = WIN = (2+6) = 8
# A vs Z = LOSS = (3+0) = 3
# B vs X = LOSS = (1+0) = 1
# B vs Y = DRAW = (2+3) = 5
# B vs Z = WIN = (3+6) = 9
# C vs X = WIN = (1+6) = 7
# C vs Y = LOSS = (2+0) = 2
# C vs Z = DRAW = (3+3) = 6

outcomes_pt1 = {
    "A X":4,"A Y":8,"A Z":3,
    "B X":1,"B Y":5,"B Z":9,
    "C X":7,"C Y":2,"C Z":6
    }

outcomes_pt2 = {
    "A X":3,"A Y":4,"A Z":8,
    "B X":1,"B Y":5,"B Z":9,
    "C X":2,"C Y":6,"C Z":7
    }

ans_pt1 = 0
ans_pt2 = 0

for i in lines:
    ans_pt1 += outcomes_pt1[i]
    ans_pt2 += outcomes_pt2[i]

print(f"Answer to part one: {ans_pt1}")
print(f"Answer to part two: {ans_pt2}")