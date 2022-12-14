x = list(map(str.splitlines, open("Day14/Day14.txt", "r").read().strip().split("\n\n")))


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


t = 0

for i, (a, b) in enumerate(x):
    if compare(eval(a), eval(b)) < 0:
        t += i + 1

print(t)