n,m,k=map(int,input().split())
a=list(map(int,input().split()))
ops=[0]*m
for i in range(m):
    l,r,d=map(int,input().split())
    ops[i]=(l,r,d)
dops=[0]*(m+2)
for i in range(k):
    x,y=map(int,input().split())
    dops[x-1]+=1
    dops[y]-=1
for i in range(1, m):
    dops[i] += dops[i-1]
diff_a = [0]*(n+2)
for i in range(m):
    l,r,d=ops[i]
    if dops[i]>0:
        v=d*dops[i]
        diff_a[l-1]+= v
        diff_a[r]-= v
curr = 0
for i in range(n):
    curr+=diff_a[i]
    a[i]+=curr
print(*a)