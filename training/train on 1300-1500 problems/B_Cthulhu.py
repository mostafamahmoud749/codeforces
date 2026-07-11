def dfs(v,l):
    global cycle
    visited[v]=True
    for i in per[v]:
        if not visited[i]:
            dfs(i,v)
        elif visited[i] and i!=l:
            cycle=True


n,m=map(int,input().split())
visited=[False]*(n+1)
per=[[] for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)

cycle=False
s=True
dfs(1,-1)
for i in range(1,n+1):
    if not visited[i]:
        s=False
        break

if s and cycle and n==m:
    print("FHTAGN!")
else:
    print("NO")