t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c0=a.count(0)
    c1=a.count(1)
    res=0
    for i in range(n):
        if a[i]>=2:
            res+=a[i]
    m=min(c0,c1)
    c1-=m
    c0-=m
    res+=m*2
    res+=c1+c0
    print(res)