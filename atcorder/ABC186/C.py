def judge_ten(x):
    x = str(x)
    return "7" in x

def judge_eight(x):
    s=""
    while x>0:
        s=str(x%8)+s
        x//=8
    return "7" in s

N = int(input())

ans=0

for i in range(1, N+1):
    if judge_ten(i)==False and judge_eight(i)==False:
        ans+=1

print(ans)