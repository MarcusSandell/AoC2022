
with open("Day1.txt","r") as f:
        lines = f.readlines()

elves = [] #maxCal, index
temp = 0

for line in lines:
    line = line.replace("\n","")
    if line == "" or line == lines[-1]:

        if line == lines[-1]:
            temp += int(line)

        elves.append(temp)
        temp = 0
    else:
        print(line)
        temp += int(line)

ans2 = []

temp = elves

for i in range(3):
    ans2.append(max(temp))
    temp.remove(max(temp))
    
    

print(f"Answer to part one: {max(elves)}")
print(f"Answer to part two: {sum(ans2)}")