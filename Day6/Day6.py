with open("Day6\\Day6.txt") as f:
    lines = f.readline()


for i in range(14,len(lines)):
    #print(lines[i-4:i])
    print(f"{lines[i-4:i]} :  set: {len(set(lines[i-4:i]))}, len: {len(lines[i-4:i])}")
    if len(set(lines[i-14:i])) == len(lines[i-14:i]):
        print(f"i: {i}")
        break
        