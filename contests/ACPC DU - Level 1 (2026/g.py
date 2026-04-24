import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    res=float("inf")
    for i in range(1,n):
        cur=0
        a[0]=a[0]+a[i]
        for j in range(i):
            cur+=min(a[0:j+1])
        a[0]=a[0]-a[i]
        res=min(res,cur)
    print(res)