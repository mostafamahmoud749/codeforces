def can(mid):
    global cost
    b=[a[i]+(i+1)*mid for i in range(n)]
    b.sort()
    curs=s
    i=0
    while i<mid:
        curs-=b[i]
        i+=1
    if curs<0:
        return False
    else:
        cost=curs
        return True
n,s=map(int,input().split())
a=list(map(int,input().split()))
l=0
r=n
res=0
cost=0
while l<=r:
    mid=l+(r-l)//2
    if can(mid):
        res=mid
        l=mid+1
    else:
        r=mid-1
print(res,s-cost)