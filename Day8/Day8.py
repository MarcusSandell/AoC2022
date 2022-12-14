grid = [list(map(int, line)) for line in open("Day8\\Day8.txt").read().splitlines()]

ans1 = 0
ans2 = 0

for r in range(len(grid)):
    for c in range(len(grid)):

        k = grid[r][c]
        if all(grid[r][x] < k for x in range(c)) or all(grid[r][x] < k for x in range(c + 1, len(grid[r]))) or all(grid[x][c] < k for x in range(r)) or all(grid[x][c] < k for x in range(r + 1, len(grid))):
            ans1 += 1

        w = e = n = s = 0

        for x in range(c - 1, -1 , -1):
            w += 1
            if grid[r][x] >= k:
                break
        for x in range(c + 1, len(grid[r])):
            e += 1
            if grid[r][x] >= k:
                break
        for x in range(r - 1, -1 , -1):
            n += 1
            if grid[x][c] >= k:
                break
        for x in range(r + 1,len(grid)):
            s += 1
            if grid[x][c] >= k:
                break
        ans2 = max(ans2, w*e*n*s)


print(ans1)
print(ans2)