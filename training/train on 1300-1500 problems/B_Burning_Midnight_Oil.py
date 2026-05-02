def v(mid):
    sumv=mid
    i=1
    while mid//(k**i)>0:
        sumv+=mid//(k**i)
        i+=1
    return sumv
n,k=map(int,input().split())
res=0
l=1
r=n
while l<=r:
    mid=l+(r-l)//2
    if v(mid)>=n:
        res=mid
        r=mid-1
    else:
        l=mid+1
print(res)