t=int(input())
for _ in range(t):
    n=int(input())
    if n<4:
        print(-1)
        continue
    res=[]
    cn=n
    if cn%2==0: cn-=1
    for i in range(cn,0,-2):
        res.append(i)
    res.append(4)
    for i in range(2,n+1,2):
        if i!=4:
            res.append(i)
    print(*res)