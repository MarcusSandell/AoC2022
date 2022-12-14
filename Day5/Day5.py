
def resetStack():
    stacks = [[],[],[],[],[],[],[],[],[]]
    for i in reversed(range(len(stacks)-1)):
        print(lines[i])
        temp = ""
        for j in (range(9)):
            if lines[i][j*4+1] != " ":

                temp += f"{lines[i][j*4+1]}"
                stacks[j].append(lines[i][j*4+1])
    return stacks

with open("Day5\\Day5.txt") as f:
    lines = f.readlines()
temp = ""

stacks = resetStack()

# Part one
for i in range(10,len(lines)):
    #print(lines[i].strip())
    orders = lines[i].strip().split(" ")
    for j in range(int(orders[1])):
        stacks[int(orders[5])-1].append(stacks[int(orders[3])-1].pop())

answer_pt1 = ""

for i in stacks:
    answer_pt1 += i[-1]

# Part two
stacks = resetStack()
for i in range(10,len(lines)):

    orders = lines[i].strip().split(" ")
    print(stacks[int(orders[3])-1])
    for j in range(int(orders[1])):

        stacks[int(orders[5])-1].append(stacks[int(orders[3])-1].pop(-int(orders[1])+j))

answer_pt2 = ""
for i in stacks:
    answer_pt2 += i[-1]    


print(f"Answer to part one is: {answer_pt1}")
print(f"Answer to part two is: {answer_pt2}")