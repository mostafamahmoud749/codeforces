import sys
sys.setrecursionlimit(200000)

def dfs(v):
    visited[v]=True
    cres=a[v-1]
    for i in per[v]:
        if not visited[i]:
            cres=min(cres,dfs(i))
    return cres

n,m=map(int,input().split())
a=list(map(int,input().split()))
per=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for i in range(m):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)

res=0
for i in range(1,n+1):
    if not visited[i]:
        res+=dfs(i)
print(res)