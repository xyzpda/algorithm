N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = list()
for i in range(N):
    if A[i] != X:
        ans.append(A[i])

print(*ans)