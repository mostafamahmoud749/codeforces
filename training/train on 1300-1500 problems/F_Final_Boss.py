import math
def can(mid):
    dmg=0
    for i in range(n):
        dmg+=math.ceil((mid/c[i]))*d[i]
    if dmg>=h:
        return True 
    else: 
        return False
t=int(input())
for _ in range(t):
    h,n=map(int,input().split())
    d=list(map(int,input().split()))
    c=list(map(int,input().split()))
    l=0
    r=(2*(10**5))**2
    res=0
    while l<=r:
        mid=l+(r-l)//2
        if can(mid):
            res=mid
            r=mid-1
        else:
            l=mid+1
    print(res)