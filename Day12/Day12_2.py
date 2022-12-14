from string import ascii_lowercase

path = "C:\\Users\\Marcu\\Desktop\\Code\\Advent of Code 2022\\Day12\\Day12.txt"

with open(path) as f:
    lines = f.read().strip().split("\n")


grid = [list(line) for line in lines]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        
        if grid[i][j] == "E":
            start = (i, j)
        #elif grid[i][j] == "a":
        #    end = (i, j)

def getHeight(char):
    if char == "S":
        return 0
    elif char == "E":
        return 25
    elif char in ascii_lowercase:
        return ascii_lowercase.index(char)


def getNeighbours(i, j, visited):

    validNeighbours = []

    for di, dj in [[1,0],[0,1],[-1,0],[0,-1]]:

        newI = di+i
        newJ = dj+j

        if not((0 <= newI < len(grid)) and (0 <= newJ < len(grid[0]))):
            continue

        if visited[newI][newJ]:
            continue
        
        elif getHeight(grid[newI][newJ]) >= getHeight(grid[i][j]) - 1:
            validNeighbours.append((newI,newJ))

    return validNeighbours

visited = [[False] * len(grid[0]) for x in grid]
nodes = [(0, start[0], start[1])] # Weight/Cost, i/y, j/x

while True:

    weight, i, j = nodes.pop(nodes.index(min(nodes)))

    if visited[i][j]:
        continue
    visited[i][j] = True

    if grid[i][j] == "a":
        print(f"DONE: {weight}")
        break

    for newI, newJ in getNeighbours(i, j, visited):
        nodes.append((weight+1,newI,newJ))

    print(f"{weight}, {i}, {j}")