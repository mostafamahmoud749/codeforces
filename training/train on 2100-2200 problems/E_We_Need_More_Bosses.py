def dfs(v,l):
    visited[v]=True
    for i in per[v]:
        if i!=l:
            deg[i]+=1
        if not visited[i]:
            dfs(i,v)


n,m=map(int,input().split())
per=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for _ in range(m):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)


deg=[0]*(n+1)

s=1
for i in range(1,n+1):
    if len(per[i])==1:
        s=i
        break

dfs(s,-1)

print(deg.count(1))