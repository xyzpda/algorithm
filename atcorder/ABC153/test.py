H, A = map(int, '10 2'.split())
if H % A == 0:
    print(H // A)
else:
    print(H // A + 1)