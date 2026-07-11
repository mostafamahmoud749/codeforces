import sys
sys.setrecursionlimit(200005)

def dfs(v,d):
    visited[v]=True
    depth[v]=d
    s[v]=1
    for i in per[v]:
        if not visited[i]:
            dfs(i,d+1)
            s[v]+=s[i]


n,k=map(int,input().split())
per=[[] for _ in range(n+1)]
visited=[False]*(n+1)
depth=[0]*(n+1)
s=[0]*(n+1)

for _ in range(n-1):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)

dfs(1,0)

res=[]

for i in range(1,n+1):
    res.append(depth[i]-s[i]+1)
res.sort(reverse=True)

print(sum(res[:k]))