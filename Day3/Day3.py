def getScore(nbr):
    if nbr > 90: # lower case
        return nbr - ord('a') + 1

    else:
        return nbr - ord('A') + 27

with open("C:\\Users\\Marcu\\Desktop\\Code\\Advent of Code 2022\\Day3\\Day3.txt") as f:
    lines = [i for i in f.read().strip().split("\n")]

answer_pt1 = 0
answer_pt2 = 0

for i in range(len(lines)):

    common = set(lines[i][:int(len(lines[i])/2)]).intersection(lines[i][int(len(lines[i])/2):]).pop()

    if i % 3 == 0:
        
        badge = set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2]).pop()
        print(f"THIRD: {i} : {badge} : {set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2])}")
        answer_pt2 += getScore(ord(badge))
        
    #else:
        #print(i)

    answer_pt1 += getScore(ord(common))



print(f"Answer to part one: {answer_pt1}")
print(f"Answer to part two: {answer_pt2}")