n,x=map(int,input().split())
a=list(map(int,input().split()))
new_a=[0]*n
for i in range(n):
    new_a[i]=(a[i],i)
l=0
r=n-1
new_a.sort()
f=False
while l<r:
    v=new_a[l][0]+new_a[r][0]
    if v==x:
        f=True
        break
    elif v>x:
        r-=1
    elif v<x:
        l+=1
print(new_a[r][1]+1,new_a[l][1]+1) if f else print("IMPOSSIBLE")
