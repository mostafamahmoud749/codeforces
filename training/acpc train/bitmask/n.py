t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    d=[0]*31
    res=0
    for i in a:
        for j in range(31):
            if i&(1<<j)==0: d[j]+=1
    for i in range(30,-1,-1):
        if d[i]<=k:
            res|=(1<<i)
            k-=d[i]
    print(res)