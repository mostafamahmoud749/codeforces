from collections import deque

n,m,k,s=map(int,input().split())
goods=list(map(int,input().split()))

adj=[[] for _ in range(n+1)]

kt=[[] for _ in range(k+1)]

for i in range(len(goods)):
    kt[goods[i]].append(i+1)

for i in range(m):
    x,y=map(int,input().split())
    adj[x].append(y)
    adj[y].append(x)

alld=[[] for _ in range(k+1)]

for i in range(1,k+1):
    ls=kt[i]
    l=[-1]*(n+1)

    if ls==[]:
        alld[i]=l
        continue

    for j in ls:
        l[j]=0
    q=deque(ls)

    while q:
        v=q.popleft()
        for u in adj[v]:
            if l[u]==-1:
                l[u]=l[v]+1
                q.append(u)
    
    alld[i]=l

res=[]
for i in range(1,n+1):
    d=[]
    for j in range(1,k+1):
        if alld[j][i]!=-1:
            d.append(alld[j][i])
    if len(d)>=s:
        d.sort()
        res.append(sum(d[:s]))
print(*res)

