N, S, D = map(int, input().split())

ans = False
for i in range(N):
    X, Y = map(int, input().split())
    if X < S and D < Y:
        ans = True
        break

if ans:
    print('Yes')
else:
    print('No')