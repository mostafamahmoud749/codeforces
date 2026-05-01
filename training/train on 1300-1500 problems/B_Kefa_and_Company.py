n,d=map(int,input().split())
a=[0]*n
for i in range(n):
    x,y=map(int,input().split())
    a[i]=[x,y]
a.sort()
l=0
r=0
res=0
cres=0
while r<=n-1:
    cres+=a[r][1]
    while a[r][0]-a[l][0]>=d:
        cres-=a[l][1]
        l+=1
    res=max(res,cres)
    r+=1
print(res)