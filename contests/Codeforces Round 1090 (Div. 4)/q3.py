t=int(input())
for _ in range(t):
    n=int(input())
    res=[]
    s=1
    e=n+1
    for i in range(n):
        res.append(s)
        res.append(e)
        res.append(e+1)
        s+=1
        e+=2
    print(*res)

