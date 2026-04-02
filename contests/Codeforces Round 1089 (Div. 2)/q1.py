t=int(input())
res=[]

for _ in range(t):
    n=int(input())
    x=[]
    for i in range(n, 0, -1):
        x.append(i)
    res.append(" ".join(map(str, x)))
print(*res, sep="\n")