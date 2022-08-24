H, W, X, Y = map(int, input().split())

grid = []
for i in range(H):
    S = input()
    S = list(S)
    grid.append(S)

X -= 1
Y -= 1

ans = 0

# up
for i in range(1, H):
    if 0<=X-i:
        if grid[X-i][Y] == "#":
            break
        else:
            ans += 1

# down
for i in range(1, H):
    if X+i<H:
        if grid[X+i][Y] == "#":
            break
        else:
            ans += 1

# left
for i in range(1, W):
    if 0<=Y-i:
        if grid[X][Y-i] == "#":
            break
        else:
            ans += 1

# right
for i in range(1, W):
    if Y+i<W:
        if grid[X][Y+i] == "#":
            break
        else:
            ans += 1

ans+=1

print(ans)