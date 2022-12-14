from collections import defaultdict
from functools import lru_cache

# Jag fattar inget asså

with open("C:\\Users\\Marcu\\Desktop\\Code\\Advent of Code 2022\\Day7\\Day7.txt") as f:
    blocks = ("\n" + f.read().strip()).split("\n$ ")[1:]

path = []

dirSizes =  defaultdict(int)
children = defaultdict(list)

def parse(block):
    line = block.split("\n")
    command = line[0]
    outputs = line[1:]

    parts = command.split(" ")
    op = parts[0]

    if op == "cd":
        if parts[1] == "..":
            path.pop()
        else:
            path.append(parts[1])

        return

    sizes = 0
    abspath = "/".join(path)

    for line in outputs:
        if not line.startswith("dir"):
            sizes += int(line.split(" ")[0])
        else:
            dirName = line.split(" ")[1]
            children[abspath].append(f"{abspath}/{dirName}")

    dirSizes[abspath] = sizes

for block in blocks:
    parse(block)    

print(dirSizes)
print(children)

@lru_cache(None)
def dfs(abspath):
    size = dirSizes[abspath]
    for child in children[abspath]:
        size += dfs(child)
    return size

unused = 70000000 - dfs("/")
required = 30000000 - unused

ans_2 = 1 << 60
for abspath in dirSizes:
    size = dfs(abspath)
    if size >= required:
        ans_2 = min(ans_2, size)


ans = 0
for abspath in dirSizes:
    if dfs(abspath) <= 100000:
        ans += dfs(abspath)

print(ans)
print(ans_2)