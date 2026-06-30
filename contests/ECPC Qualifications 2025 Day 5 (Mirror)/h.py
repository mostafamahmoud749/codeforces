t=int(input())
for _ in range(t):
    n=int(input())
    a=list(input().strip())
    b=[]
    res=[]
    for i in range(1,n+1):
        if a[i]=="1":
            res.append(i-1)
            res=res+b[::-1]
            b=[]
        else:
            b.append(i-1)
    print(*res)