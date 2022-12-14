def compare(x, y):

    if type(x) == int:
        if type(y) == int:
            return x - y

        else:
            return compare([x] ,y)

    else:
        if type(y) == int:
            return compare(x, [y])

    for a, b, in zip(x, y):
        v = compare(a, b)
        if v:          # If v non zero
            return v

    return len(x) - len(y)

x = list(map(eval, open("Day13\\Day13.txt").read().strip().split()))

i2 = 1
i6 = 2

for a in x:
    if compare(a, [[2]]) < 0:
        i2 += 1
        i6 += 1

    elif compare(a, [[6]]) < 0:
        i6 += 1

print(i2*i6)