n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=[0]*n
for i in range(n):
    c[i]=a[i]-b[i]
c.sort()
out=0
for i in range(n-1):
    l=i+1
    r=n-1
    res=-1
    while l<=r:
        mid=l+(r-l)//2
        if c[i]+c[mid]>0:
            res=mid
            r=mid-1
        else:
            l=mid+1
    if res!=-1:
        out+=n-res
print(out)