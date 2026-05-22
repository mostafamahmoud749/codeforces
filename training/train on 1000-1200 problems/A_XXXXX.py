t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))
    if n==1:
        print(-1) if a[0]%x==0 else print(1)
        continue
    p=[0]*(n+1)
    rem=[-1]*n
    res=-2
    for i in range(1,n+1):
        p[i]=p[i-1]+a[i-1]
        rem[i-1]=p[i]%x
    
    res = -1
    if p[n] % x != 0:
        res = n
    else:
        for i in range(n):
            if rem[i] != 0:
                res = max(res, i + 1, n - (i + 1))
    print(res)
