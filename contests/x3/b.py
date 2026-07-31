import math
def can(mid):
    opc=k
    for i in a:
        if i<=mid:
            continue
        opc-=(math.ceil(i/mid)-1)


    if opc>=0:
        return True
    return False


t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    l=1
    r=1e9
    res=-1
    while l<=r:
        mid=l+(r-l)//2
        if can(mid):
            r=mid-1
            res=mid
        else:
            l=mid+1
    
    print(int(res))
