def can(mid):
    smid=str(mid)
    summid=0
    for i in smid:
        summid+=int(i)
    return True if mid-summid>=s else False

n,s=map(int,input().split())
l=1
r=n
res=0

while l<=r:
    mid=l+(r-l)//2
    if can(mid):
        res=mid
        r=mid-1
    else:
        l=mid+1

print(n-res+1) if res!=0 else print(0) 
