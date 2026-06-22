t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    g=list(map(int,input().split()))
    s=True
    curmin=g[0]
    curmax=g[0]
    for i in range(1,n):
        curmax+=k-1
        curmin-=k-1
        if i==n-1:
            curmax=min(curmax,g[i])
            curmin=max(curmin,g[i])
        else:
            curmax=min(curmax,g[i]+k-1)
            curmin=max(curmin,g[i])
        if curmax<curmin:
            s=False
            break
    
    print("YES") if s else print("NO")