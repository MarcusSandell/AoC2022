with open("Day04\\Day4.txt") as f:
    lines = [i for i in f.read().strip().split("\n")]

answer_pt1 = 0
answer_pt2 = 0

for i in lines:
    
    sections = list(map(int, i.replace("-",",").split(",")))

    print(sections)

    if(sections[0] <= sections[2] and sections[1] >= sections[3] or sections[0] >= sections[2] and sections[1] <= sections[3]):
    #if((sections[0] >= sections[2] and sections[1] <= sections[3]) or (sections[2] >= sections[0] and sections[3] <= sections[1])):
        answer_pt1 += 1
        answer_pt2 += 1

    elif not(sections[1] < sections[2] or sections[3] < sections[0]):
    #elif(len(list(range(sections[0],sections[1]+1))+list(range(sections[2],sections[3]+1))) != len(set(list(range(sections[0],sections[1]+1))+list(range(sections[2],sections[3]+1))))):
        answer_pt2 += 1
    
    
print(f"Answer_pt1 to part one is: {answer_pt1}")
print(f"Answer_pt1 to part two is: {answer_pt2}")