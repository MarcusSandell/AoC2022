path =  "C:\\Users\\Marcu\\Desktop\\Code\\Advent of Code 2022\\Day13\\Day13.txt"

x = list(map(str.splitlines, open(path).read().strip().split("\n\n")))


def f(x, y):

    if type(x) == int:
        if type(y) == int:
            return x - y

        else:
            return f([x] ,y)

    else:
        if type(y) == int:
            return f(x, [y])

    for a, b, in zip(x, y):
        v = f(a, b)
        if v:          # If v non zero
            return v

    return len(x) - len(y)


t = 0

for i, (a, b) in enumerate(x):
    if f(eval(a), eval(b)) < 0:
        t += i + 1

print(t)