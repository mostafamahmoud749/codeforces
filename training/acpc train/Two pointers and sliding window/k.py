n,m,k=map(int,input().split())
a=list(map(int,input().split()))
ops=[0]*m
for i in range(m):
    l,r,d=map(int,input().split())
    ops[i]=(l,r,d)
dops=[0]*m
for i in range(k):
    x,y=map(int,input().split())
    for j in range(x,y+1):
        dops[j-1]+=1
for i in range(m):
    l,r,d=ops[i]
    if dops[i]>0:
        v=d*dops[i]
        for j in range(l, r+1):
            a[j-1]=a[j-1]+v
print(*a)