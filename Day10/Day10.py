with open("Day10\\Day10.txt") as f:
    operations = f.read().strip().split("\n")

register_val = 1
cycle_nbr = i = 0
adding = False
ans_pt1 = 0
ans_pt2 = ["" for x in range(6)]
row = 0


def renderer():
    ans_pt2[row] += "##" if (abs(cycle_nbr-(40*row) - register_val) <= 1) else "  "


while i < len(operations):

    renderer()
    cycle_nbr += 1
    
    # For part one
    if (cycle_nbr+20)%40 == 0:
        ans_pt1 += register_val*cycle_nbr
    # For part two
    if cycle_nbr % 40 == 0:
        row += 1
    


    if adding == True:
        register_val += int(operations[i].split(" ")[1])
        adding = False
        i += 1 

    elif operations[i][:4] == "addx":
        adding = True

    elif operations[i] == "noop":
        i += 1


print(ans_pt1)

for i in ans_pt2:
    print(i)