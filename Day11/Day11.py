
path = "C:\\Users\\Marcu\\Desktop\\Code\\Advent of Code 2022\\Day11\\Day11.txt"
with open(path) as f:
    lines = f.read().strip().split("\n")

amountOfMonkeys = int(lines[-6][7])
monkeys = []

class Monkey:
    def __init__(self, items, operation, test, next_monkey):
        self.items = items
        self.operation = operation
        self.test = test
        self.next_monkey = next_monkey

        self.inspections = 0

    def __str__(self):
        return f"Items: {self.items}\tOps: {self.operation}\ttest: {self.test}\tNext: {self.next_monkey}\tInspections: {self.inspections}"

for i in range(0,len(lines),7):

    items = list(map(int, lines[i+1][18:].replace(" ","").split(",")))
    operation = eval("lambda old:" + lines[i+2].split("=")[-1])
    test = int(lines[i+3].split()[-1])
    next_monkey = [int(lines[i+4].split()[-1]),int(lines[i+5].split()[-1])]

    monkeys.append(Monkey(items,operation,test,next_monkey))


mod = 1
for monkey in monkeys:
    mod *= monkey.test

for i in range(10000):
    for monkey in monkeys:
        for item in monkey.items:

            item = monkey.operation(item) # New worry
            item %= mod
            #item //= 3  # Worry level divided by 3 rounded down

            if item % monkey.test == 0:
                monkeys[monkey.next_monkey[0]].items.append(item)
            else:
                monkeys[monkey.next_monkey[1]].items.append(item)

        monkey.inspections += len(monkey.items)

        monkey.items = []
                
answer = [0,0]

for monkey in monkeys:
    insp = monkey.inspections
    if(monkey.inspections > answer[0]):
        answer[1] = answer[0]
        answer[0] = monkey.inspections
    else:
        answer[1] = max(answer[1], monkey.inspections)

print(answer[0]*answer[1])