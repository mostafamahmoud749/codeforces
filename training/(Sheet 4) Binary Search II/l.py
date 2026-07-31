def can(mid):
    cres=0
    for i in a:
        cres+=mid//i
    if cres>=t:
        return True
    return False

n,t=map(int,input().split())
a=list(map(int,input().split()))
res=-1
l=1
r=10**18

while l<=r:
    mid=l+(r-l)//2
    if can(mid):
        r=mid-1
        res=mid
    else:
        l=mid+1
print(res)