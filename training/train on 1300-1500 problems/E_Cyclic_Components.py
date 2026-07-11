import sys
sys.setrecursionlimit(200005)


def dfs(v):
    visited[v]=True
    path.append(v)
    for i in per[v]:
        if not visited[i]:
            dfs(i)
        


n,m=map(int,input().split())
per=[[] for _ in range(n+1)]
visited=[False]*(n+1)

for i in range(m):
    x,y=map(int,input().split())
    per[x].append(y)
    per[y].append(x)


res=0
for i in range(1,n+1):
    if not visited[i]:
        path=[]
        cyc=True
        dfs(i)
        for i in path:
            if len(per[i])!=2:
                cyc=False
                break
        if cyc:
            res+=1

print(res)
