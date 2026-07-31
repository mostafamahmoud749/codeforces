def can(mid):
    curw=w
    for i in a:
        if i<mid:
            curw-=mid-i
    return True if curw>=0 else False

t=int(input())
for _ in range(t):
    n,w=map(int,input().split())
    a=list(map(int,input().split()))
    l=0
    r=10**18
    res=0

    while l<=r:
        mid=l+(r-l)//2
        if can(mid):
            res=mid
            l=mid+1
        else:
            r=mid-1

    print(res)
